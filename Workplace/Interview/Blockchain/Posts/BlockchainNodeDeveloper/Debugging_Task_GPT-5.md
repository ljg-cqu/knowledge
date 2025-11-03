# Blockchain Node Developer — Debugging Task (GPT-5)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/Debugging_Task.md](../../Prompts/Templates/Debugging_Task.md). Role context from [Job_Description.md](Job_Description.md).

Each task includes: buggy code, what fails, minimal fix, root cause, and grading rubric.

## Contents

- Tasks 1–18
- References

---

## Task 1 — Context not honored in HTTP request

- Language: go | Difficulty: Foundational
- Symptom: Calls don’t cancel on timeout; requests hang past context deadline.

Buggy code:
```go
package rpcc
import (
  "context"
  "net/http"
)
func Call(ctx context.Context, url string, body []byte) (*http.Response, error) {
  req, _ := http.NewRequest("POST", url, nil) // BUG: not using ctx and no body
  return http.DefaultClient.Do(req)
}
```

Failing test (excerpt):
```go
ctx, cancel := context.WithTimeout(context.Background(), 10*time.Millisecond)
defer cancel()
_, err := Call(ctx, "http://localhost:0", []byte("{}"))
if !errors.Is(err, context.DeadlineExceeded) { t.Fatalf("want ctx deadline, got %v", err) }
```

Minimal fix:
```go
req, _ := http.NewRequestWithContext(ctx, "POST", url, bytes.NewReader(body))
```

Root cause: Request created without binding the context; cancellation couldn’t propagate.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 2 — Goroutine leak via time.After in loop

- Language: go | Difficulty: Intermediate
- Symptom: High goroutine count under retries.

Buggy code:
```go
for {
  select {
  case <-time.After(500 * time.Millisecond): // BUG: allocs a timer each loop, unreclaimed if branch skipped
    do()
  case <-ctx.Done():
    return
  }
}
```

Minimal fix:
```go
t := time.NewTimer(500 * time.Millisecond)
defer t.Stop()
for {
  t.Reset(500 * time.Millisecond)
  select {
  case <-t.C:
    do()
  case <-ctx.Done():
    return
  }
}
```

Root cause: time.After allocates a new timer per iteration. If the other case wins, timers accumulate until GC.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 3 — Token bucket race condition

- Language: go | Difficulty: Intermediate
- Symptom: Flaky allows/denies under concurrency.

Buggy code:
```go
type Bucket struct { r, b, tokens float64; last time.Time }
func (bk *Bucket) Allow(n float64) bool {
  now := time.Now()
  elapsed := now.Sub(bk.last).Seconds()
  bk.tokens = math.Min(bk.b, bk.tokens+elapsed*bk.r) // BUG: no locking
  bk.last = now
  if bk.tokens >= n { bk.tokens -= n; return true }
  return false
}
```

Minimal fix:
```go
type Bucket struct { mu sync.Mutex; r, b, tokens float64; last time.Time }
func (bk *Bucket) Allow(n float64) bool {
  bk.mu.Lock(); defer bk.mu.Unlock()
  // ... same math ...
}
```

Root cause: Data race over shared state in concurrent calls.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 4 — Off-by-one in log windowing

- Language: go | Difficulty: Foundational
- Symptom: Missed last block in range.

Buggy code:
```go
for s := start; s < end; s += W { // BUG: should include end
  e := s + W - 1
  if e > end { e = end }
  out = append(out, [2]uint64{s, e})
}
```

Minimal fix:
```go
for s := start; s <= end; s += W {
  // same
}
```

Root cause: Exclusive upper bound loop skipped final partial window.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 5 — Bloom filter bit math error

- Language: go | Difficulty: Intermediate
- Symptom: False negatives higher than expected.

Buggy code:
```go
b.bits[i/8] = b.bits[i/8] | 1 << (i % 8) // BUG: (i%8) is int; shift on untyped int may sign-extend
```

Minimal fix:
```go
b.bits[i/8] |= 1 << (uint(i) % 8)
```

Root cause: Shift uses int; ensure shift count is uint to set correct bit.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 6 — p95 index rounding bug

- Language: go | Difficulty: Foundational
- Symptom: p95 sometimes equals max for small samples.

Buggy code:
```go
i95 := int(0.95 * float64(len(xs))) // BUG: should use len-1 index
```

Minimal fix:
```go
i95 := int(0.95 * float64(len(xs)-1))
```

Root cause: Percentile index should be computed over zero-based last index.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 7 — Exponential backoff overflow

- Language: go | Difficulty: Foundational
- Symptom: Delays wrap negative or cap to near-zero at high attempts.

Buggy code:
```go
d := base << attempt // BUG: overflowing shift for large attempt
```

Minimal fix:
```go
if attempt < 0 { attempt = 0 }
if attempt > 20 { attempt = 20 } // clamp
d := base << uint(attempt)
if d > max { d = max }
```

Root cause: Duration is int64 under the hood; large shifts overflow.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 8 — JSON number precision loss

- Language: go | Difficulty: Intermediate
- Symptom: Block numbers parsed as float64 lose precision for large values.

Buggy code:
```go
var m map[string]interface{}
json.Unmarshal(b, &m) // BUG: default decoder converts numbers to float64
```

Minimal fix:
```go
dec := json.NewDecoder(bytes.NewReader(b))
dec.UseNumber()
var m map[string]interface{}
if err := dec.Decode(&m); err != nil { return err }
```

Root cause: Go’s default JSON uses float64; UseNumber preserves exact decimal.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 9 — HTTP body leak

- Language: go | Difficulty: Foundational
- Symptom: File descriptors leak; eventually EMFILE.

Buggy code:
```go
resp, err := http.DefaultClient.Do(req)
if err != nil { return err }
body, _ := io.ReadAll(resp.Body)
// BUG: missing resp.Body.Close()
_ = body
```

Minimal fix:
```go
defer resp.Body.Close()
```

Root cause: Not closing response bodies leaks connections.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 10 — Prometheus metric recreated in hot path

- Language: go | Difficulty: Intermediate
- Symptom: Panics: duplicate metrics registration; high allocs.

Buggy code:
```go
g := prometheus.NewGauge(prometheus.GaugeOpts{Name: "finality_distance", Help: "..."})
prometheus.MustRegister(g)
func report(d float64){ g.Set(d) } // BUG: executed per-call in some paths
```

Minimal fix:
```go
var (
  finalityDistance = prometheus.NewGauge(prometheus.GaugeOpts{ Name: "finality_distance", Help: "..."})
)
func init(){ prometheus.MustRegister(finalityDistance) }
func report(d float64){ finalityDistance.Set(d) }
```

Root cause: Re-registering same metric repeatedly.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 11 — SQL injection via string concatenation

- Language: go | Difficulty: Intermediate
- Symptom: Security finding; tainted input in WHERE clause.

Buggy code:
```go
q := "SELECT * FROM logs WHERE topic0='" + userInput + "'" // BUG
row := db.QueryRowContext(ctx, q)
```

Minimal fix:
```go
row := db.QueryRowContext(ctx, "SELECT * FROM logs WHERE topic0=$1", userInput)
```

Root cause: Unparameterized query allows injection.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 12 — Hex decoding without validation

- Language: go | Difficulty: Foundational
- Symptom: Accepts malformed hashes; downstream panics.

Buggy code:
```go
b, _ := hex.DecodeString(strings.TrimPrefix(h, "0x")) // BUG: ignoring error and length
return b
```

Minimal fix:
```go
s := strings.TrimPrefix(h, "0x")
b, err := hex.DecodeString(s)
if err != nil || len(b) != 32 { return fmt.Errorf("bad hash") }
return b
```

Root cause: Ignoring error and expected length.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 13 — Unsigned score underflow

- Language: go | Difficulty: Intermediate
- Symptom: Peer score becomes huge after a penalty.

Buggy code:
```go
var score uint64
score -= 5 // BUG: underflow wraps to max uint64
```

Minimal fix:
```go
var score int64
score -= 5
```

Root cause: Unsigned arithmetic wraps instead of becoming negative.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 14 — Hedged requests don’t cancel secondary

- Language: go | Difficulty: Intermediate
- Symptom: Extra load; second request keeps running even after first success.

Buggy code (excerpt):
```go
resCh := make(chan result, 2)
go func(){ resCh <- do(ctx) }()
// start hedge after delay
go func(){ resCh <- do(ctx) }() // BUG: no cancel of loser
return <-resCh
```

Minimal fix:
```go
ctx1, cancel := context.WithCancel(ctx)
resCh := make(chan result, 2)
go func(){ resCh <- do(ctx1) }()
// after delay start hedge
go func(){ resCh <- do(ctx1) }()
r := <-resCh
cancel() // cancel the loser
return r
```

Root cause: Not canceling remaining in-flight request after first winner returns.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 15 — Context not propagated to goroutine

- Language: go | Difficulty: Foundational
- Symptom: Worker runs past cancellation.

Buggy code:
```go
go func(){ work() }() // BUG: ignores ctx
```

Minimal fix:
```go
go func(){ select { case <-ctx.Done(): return; case <-start: work() } }()
```

Root cause: Missing ctx.Done() select path for cooperative cancel.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 16 — Rust light client verification stub always OK

- Language: rust | Difficulty: Advanced
- Symptom: Invalid signatures accepted.

Buggy code:
```rust
pub fn verify(header: &Header, sig: &Signature) -> Result<(), VerifyError> {
    // TODO: implement BLS; for now
    Ok(()) // BUG
}
```

Minimal fix (interface-level):
```rust
pub fn verify(header: &Header, sig: &Signature) -> Result<(), VerifyError> {
    bls_verify(header.message_hash(), sig, header.pubkey()).map_err(|_| VerifyError::InvalidSig)
}
```

Root cause: Stub returned Ok unconditionally, bypassing verification.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 17 — Net dialer misconfiguration

- Language: go | Difficulty: Foundational
- Symptom: Dial fails on some platforms; invalid keepalive.

Buggy code:
```go
d := net.Dialer{ KeepAlive: -1 * time.Second } // BUG: negative
```

Minimal fix:
```go
d := net.Dialer{ KeepAlive: 0 }
```

Root cause: Negative keepalive not allowed; use 0 for default/disabled.

Grading: Fix 60, Explanation 30, Style 10.

---

## Task 18 — Engine API JWT builder missing audience and exp

- Language: go | Difficulty: Intermediate
- Symptom: Engine API rejects token; "aud"/"exp" missing.

Buggy code:
```go
claims := jwt.MapClaims{"iat": time.Now().Unix()} // BUG: missing aud/exp
```

Minimal fix:
```go
claims := jwt.RegisteredClaims{
  Audience: jwt.ClaimStrings{"engine"},
  IssuedAt: jwt.NewNumericDate(time.Now()),
  ExpiresAt: jwt.NewNumericDate(time.Now().Add(ttl)),
}
```

Root cause: Did not adhere to expected claims for Engine API auth.

Grading: Fix 60, Explanation 30, Style 10.

---

## References

See [../../Prompts/Shared_References.md](../../Prompts/Shared_References.md). This note reuses references from `QA_GPT-5.md`; floors satisfied across the pack.
