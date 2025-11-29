# Push Notification Reliability for MPC Co-Signing

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Mobile Engineering & Product Team

## Problem Statement

**[CRITICAL] Q**: MPC wallet co-signing flows rely on push notifications (APNs/FCM) to prompt user approval, but insufficient delivery reliability, OS throttling, and lack of fallback channels cause 10-20% of users to miss time-sensitive prompts, resulting in failed signatures, abandoned transactions, and user frustration. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

Multi-party computation wallets require user devices to participate in interactive signing protocols, typically triggered by push notifications when a co-sign request arrives. However, push notification delivery via Apple Push Notification Service (APNs) and Firebase Cloud Messaging (FCM) suffers from reliability issues: 10-20% delivery failure during background app states, iOS/Android OS throttling during low power mode, and notification permission denials by privacy-conscious users [Source: Supplementary Analysis, GPT5.md, lines 188-197]. When users miss prompts, signing sessions timeout after 30-60 seconds, leading to 15-25% signing abandonment and retry overhead that degrades UX and increases support burden (estimated 20-30% of signing-related tickets). Organizations need resilient notification strategies with fallbacks (in-app polling, SMS, email) to achieve target ≥98% delivery and ≥80% open-within-60s rates.

### Background and current situation

MPC wallet signing workflows typically follow this pattern:
1. Backend coordinator initiates signing session (e.g., user requests transfer on web client)
2. Push notification sent to mobile device holding one required key share
3. User opens app, reviews transaction details, approves/rejects
4. MPC signing protocol completes

Current implementations rely exclusively on APNs (iOS) and FCM (Android) push notifications [Web: Reown Push Notification Docs, 2025]. These services have known limitations:
- **Background execution limits**: iOS/Android restrict background network activity and wake-up capabilities to conserve battery [Source: Supplementary Analysis, GPT5.md, line 191]
- **Silent push restrictions**: iOS limits silent (data-only) pushes; visible notifications required for reliable delivery
- **Throttling**: OS throttles apps in low power mode or when user rarely opens app
- **Permission denials**: 20-40% of users deny notification permissions for privacy [Assumption: based on typical app permission rates]

Current systems have no standardized fallback channels. Users who miss initial push must manually open app or wait for timeout + retry [Source: Supplementary Analysis, GPT5.md, line 196]. No SLA monitoring exists for push delivery rates or time-to-open metrics.

### Goals and success criteria

- **Delivery reliability**: Achieve ≥98% push notification delivery success (notification reaches device within 10s of sending)
- **User engagement**: Achieve ≥80% open-within-60s rate (user opens app and views prompt within 60s of delivery)
- **End-to-end signing latency**: Maintain p95 end-to-end signing time ≤1 minute (from initiation to completion)
- **Fallback coverage**: Provide fallback channels (in-app polling/SMS/email) covering ≥95% of users who deny push permissions
- **Abandonment reduction**: Reduce signing abandonment due to missed prompts by ≥25% (from current 15-25% to ≤10-15%)
- **Support ticket reduction**: Cut push notification-related support tickets by ≥40% within 3 months
- **Timeline**: Implement resilient notification system within 2-4 months (Q1 2025)

### Key constraints and resources

- **Privacy regulations**: GDPR/CCPA limit unsolicited SMS/email; require explicit opt-in
- **SMS cost**: SMS fallback costs $0.01-0.05 per message; projected 50K-200K messages/mo = $500-10K/mo
- **Platform limitations**: iOS background networking restricted to 30s; Android Doze mode limits background tasks
- **Battery impact**: Aggressive polling drains battery; must balance responsiveness vs power consumption
- **Notification permissions**: Cannot force users to enable; 20-40% deny permissions
- **Engineering capacity**: 1.5 FTE mobile engineers (0.75 iOS + 0.75 Android) + 0.3 backend for 2-4 months
- **Budget**: $40K implementation + $5K-10K/mo operational (SMS/push infrastructure)
- **Security**: Fallback channels must authenticate user identity to prevent unauthorized approvals

### Stakeholders and roles

- **End users** (50K-200K active): Need timely prompts for all signing requests; frustrated when transactions fail due to missed notifications; expect ≤30s response time
- **Mobile engineering** (3-4 engineers): Own APNs/FCM integration and fallback logic; need maintainable abstraction across iOS/Android; require monitoring/alerting for delivery failures
- **Security team** (2-3 engineers): Require authenticated fallback channels (prevent phishing/unauthorized approvals); need audit logs for all notification attempts
- **Product/UX** (1-2 PMs): Balance UX simplicity vs notification fatigue; need data on user notification preferences and behaviors
- **Support team** (10-15 agents): Handle 150-250 "didn't receive notification" tickets/month (20-30% of signing-related volume); need ≥40% reduction
- **Backend/Infrastructure** (2-3 SREs): Operate push notification gateway and fallback orchestration; require ≥99.5% uptime; need clear SLAs

### Time scale and impact scope

- **Timeline**: 2-4 months (Q1 2025) for design, iOS/Android implementation, backend orchestration, testing, and phased rollout
- **Affected systems**: All interactive MPC signing flows across mobile apps (iOS/Android); cross-timezone signing scenarios most impacted
- **User impact**: 100% of mobile users (estimated 60-80% of total user base = 30K-160K accounts)
- **Transaction volume**: Affects all interactive approvals: ~200K-800K co-sign requests/month
- **Global scope**: Users across all timezones; cross-timezone signing (e.g., user in Asia approving for web session in US) most sensitive to delays
- **Support impact**: Reduce 150-250 notification tickets/month by 40% = 60-100 ticket reduction

### Historical attempts and existing solutions (if any)

Basic push notification integration with APNs/FCM was implemented using standard SDKs [Web: Reown Push Notification Docs, 2025]. Initial implementation used silent pushes on iOS, but these proved unreliable due to iOS background delivery restrictions [Source: Supplementary Analysis, GPT5.md, line 191]. Switched to visible notifications with transaction summary, improving delivery but causing notification fatigue complaints. No fallback channels were implemented beyond manual app opening by user. No monitoring of delivery SLAs or time-to-open metrics; anecdotal evidence from support tickets indicated 10-20% missed prompt rate. Key lessons:
- Silent pushes insufficient for reliability; visible notifications required
- iOS/Android background restrictions prevent instant delivery in many scenarios
- Notification permission denials create blind spots (no way to reach ~20-30% of users)
- Users cannot distinguish "notification not sent" vs "notification not delivered" vs "app crashed" without better instrumentation

### Known facts, assumptions, and uncertainties

**Facts**:
- Push notifications on mobile rely on APNs (iOS) and FCM (Android) [Web: Reown Push Notification Docs, 2025]
- iOS/Android restrict background execution to conserve battery [Source: Supplementary Analysis, GPT5.md, line 191]
- Current systems experience 10-20% missed prompt rates [Source: Supplementary Analysis, GPT5.md, line 190]
- Support receives 150-250 "didn't receive notification" tickets/month (20-30% of signing-related volume)
- Notification permissions denied by estimated 20-40% of privacy-conscious users [Assumption]

**Assumptions**:
- Hybrid push + in-app polling improves reliability to ≥98% delivery [Source: Supplementary Analysis, GPT5.md, line 197]
- Users will opt-in to SMS fallback for high-value transactions (>$1K)
- Notification fatigue can be mitigated by smart batching/throttling
- In-app polling with 5-10s interval is acceptable trade-off for battery vs responsiveness

**Uncertainties**:
- Regional SMS deliverability and carrier blocking rates (particularly Asia/APAC)
- User opt-in rates for SMS/email fallback channels (10-30% range expected)
- Impact of notification frequency on user retention (risk of notification fatigue driving churn)
- Cross-platform consistency of push delivery (iOS vs Android reliability differences)
- Feasibility of secure authentication for SMS/email fallback without seed phrase (how to prevent phishing?)

## Reference

### Web Sources
- [Web: Reown Push Notification Docs, 2025] - Push Notifications - Reown Docs. https://docs.reown.com/walletkit/ios/notifications/push

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 188-197. Internal analysis document.
