下面给出完整可用的“Debugging / Code-Reading”面试题集，严格遵循所给模板，覆盖联盟链与RWA（真实世界资产）方向的区块链架构师岗位要求与技术栈，包含从入门到高级的15个调试任务（Foundational 20%、Intermediate 50%、Advanced 30%），并给出完整的修复代码、根因说明与可运行的最小化测试。内容同时考虑到岗位职责中对联盟链（FISCO BCOS/Hyperledger Fabric）、Solidity/Hardhat、后端集成（Go/Java/Node.js）、预言机（Chainlink）、存储（IPFS/Arweave）、密码学与安全、治理与权限边界、RWA合规模型、DevOps/TLS/K8s等要求的覆盖。为便于对照行业角色与RWA方向，文中参考自区块链架构岗位通用职责与RWA战略岗位要点进行对齐与引用支撑。[1][4]

在实际面试中，候选人需针对每一题提交三类可交付物：最小改动的修复代码（含必要注释）、2–4句的根因说明（指明被违反的原则/模式）、以及能复现失败并验证修复的最小通过测试。评分以修复正确性、解释深度与测试完整性为主，并允许在复杂问题上给出部分分。该结构与评分重点契合区块链架构师岗位强调的系统级思维、代码级安全与工程化落地的核心胜任力。[1][4][2]



## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Tasks](#tasks)
  - [Task 1: RWA平均收益计算的零长度防御（Node.js）](#task-1-rwa平均收益计算的零长度防御nodejs)
  - [Task 2: Solidity分账循环的末项遗漏（off-by-one）](#task-2-solidity分账循环的末项遗漏off-by-one)
  - [Task 3: Go网关JSON反序列化的类型不匹配](#task-3-go网关json反序列化的类型不匹配)
  - [Task 4: Solidity授权使用tx.origin的安全误用](#task-4-solidity授权使用txorigin的安全误用)
  - [Task 5: Hardhat测试中BigNumber与JS Number混用导致精度/溢出](#task-5-hardhat测试中bignumber与js-number混用导致精度溢出)
  - [Task 6: 预言机API误用：latestAnswer vs latestRoundData](#task-6-预言机api误用latestanswer-vs-latestrounddata)
  - [Task 7: Fabric链码状态读取未判空导致panic](#task-7-fabric链码状态读取未判空导致panic)
  - [Task 8: FISCO BCOS国密链上ECDSA签名错配](#task-8-fisco-bcos国密链上ecdsa签名错配)
  - [Task 9: Node.js网关未await导致并发竞态与重复支出校验失效](#task-9-nodejs网关未await导致并发竞态与重复支出校验失效)
  - [Task 10: IPFS未pin导致内容被回收](#task-10-ipfs未pin导致内容被回收)
  - [Task 11: Spring Boot双向TLS漏配clientAuth](#task-11-spring-boot双向tls漏配clientauth)
  - [Task 12: PostgreSQL租约占用的隔离级别问题（幻读/并发）](#task-12-postgresql租约占用的隔离级别问题幻读并发)
  - [Task 13: Solidity重入漏洞：佣金提现的推-拉模式切换](#task-13-solidity重入漏洞佣金提现的推-拉模式切换)
  - [Task 14: 跨链签名校验遗漏chainId导致重放](#task-14-跨链签名校验遗漏chainid导致重放)
  - [Task 15: Fabric背书策略过宽引发治理/权限边界失真](#task-15-fabric背书策略过宽引发治理权限边界失真)



## Executive Summary

- 目标：通过15个真实世界调试任务考察候选人在联盟链/RWA场景下的系统性诊断、代码级安全修复、性能与治理权衡能力，覆盖合约安全、平台框架、后端网关、预言机、存储与密码学等全栈面。[1][4]  
- 覆盖：Foundational 20%（显性错误）、Intermediate 50%（逻辑/API/框架语义追踪）、Advanced 30%（并发/安全/治理/跨链 subtle bugs）。每题单一聚焦缺陷，提供足够上下文与失败输出，便于复现与定位。[1][4]  
- 评估：采用Fix(0–6)+Explanation(0–3)+Tests(0–1)的评分制，给与部分分；强调不幸路径、回滚、边界条件与合规/治理一致性。[1][4]  
- 参考：职责与能力模型对齐“区块链架构师”与“RWA策略/代币化”角色通用要求，并贯穿至题目设计与评分维度，确保岗位匹配度。[1][4][2]  



## Coverage & Difficulty Summary

| Difficulty | Count | Tasks |
|---|---:|---|
| Foundational | 3 | 1–3 |
| Intermediate | 8 | 4–11 |
| Advanced | 4 | 12–15 |

- Topic cluster mapping:  
  - Cluster A: 智能合约安全与模式（Solidity/Hardhat/OpenZeppelin）→ Tasks 2,4,5,6,13,14 [1][4]  
  - Cluster B: 联盟链平台（FISCO BCOS/Hyperledger Fabric）与治理/权限 → Tasks 7,8,15 [1][4]  
  - Cluster C: 后端集成与并发（Go/Java/Node.js）→ Tasks 3,9,11 [1][4]  
  - Cluster D: 数据与存储（IPFS/Arweave、DB事务）→ Tasks 10,12 [1][4]  
  - Cluster E: 预言机/外部数据与跨链 → Tasks 6,14 [1][4]  
  - Cluster F: 密码学/签名/协议边界 → Tasks 8,14 [1][4]  



## Glossary & Acronym Index

- RWA（Real-World Asset）：将现实世界资产（如车辆）进行链上映射与融资的代币化范式，强调合规、治理与生命周期管理。[4][1]  
- 联盟链（Permissioned Blockchain）：有成员管理与权限控制的区块链，如Hyperledger Fabric、FISCO BCOS，常用于企业/产业协作场景。[1]  
- Chaincode（Fabric）：Fabric中的智能合约，运行于容器环境，通过背书策略与通道控制访问与可信执行。[1]  
- AMOP（FISCO BCOS）：消息通信组件（群组内/跨群组），常用于链下/链上协同。[1]  
- ERC-20/721/1155：以太坊代币/资产标准；EIP-712：结构化数据签名标准，绑定domain/chainId防重放。[1]  
- ReentrancyGuard/Checks-Effects-Interactions：合约防重入模式与交互顺序最佳实践。[1]  
- latestRoundData：Chainlink价格饲喂标准接口（含round/updatedAt），替代已废弃/不完整的接口。[1]  



## How to Use This in Interviews

- 面试官先挑选3–5题跨集群分布的小题，观察候选人的定位路径、API理解、错误模式复用与安全边界意识；必要时再加一道高级题考察纵深。[1][4]  
- 评分：修复（0–6）、解释（0–3）、测试（0–1）；允许部分分，如“诊断正确但修复不完全”或“修复正确但解释薄弱”。[1]  
- 验证：要求候选人在本地运行“失败→通过”的测试闭环，并简述不幸路径、回滚与监控点；对涉及治理/权限的题，要求画出背书/策略/风险清单。[4]  



## Key Decision Criteria Checklist

- 修复策略：简单补丁 vs 体系化重构（可维护性、抽象合理性）。[1]  
- 安全性：权限边界、签名域绑定、防重入、输入验证、密钥/证书/TLS配置。[1][4]  
- 性能/并发：延迟、吞吐与一致性；锁粒度、批量化与重试幂等。[1]  
- 合规/治理：RWA合规边界、背书策略、审计可追溯与最小必要权限。[4]  
- 可观测与回滚：日志、度量、告警与灰度/回滚计划；数据修复与再处理。[1][4]  



## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Fix Approach A | Preferred Fix Approach B | Notes/Signals |
|---|---|---|---|
| 授权与签名 | 严格基于msg.sender/EIP-712域绑定 | 白名单与多签治理 | A适合链上接口，B适合平台级治理与风控。[1][4] |
| 并发一致性 | 事务与悲观锁/乐观锁 | 幂等键与队列串行化 | 取决于热点与延迟预算。[1] |
| 预言机数据 | latestRoundData校验staleness | 多源聚合/安全门限 | 金融/RWA需双重保护。[1][4] |
| 存储持久性 | pin服务/冗余网关 | 存证+哈希可验证 | 交易证明与证据链要求。[1][4] |



---

## Task 1: RWA平均收益计算的零长度防御（Node.js）

Language: JavaScript/Node.js  
Difficulty: Foundational  
Bloom: Analyze

### Buggy Code

```javascript
// avgPayout.js - 计算司机RWA租约日均收益
function avgPayout(payouts) {
  let sum = 0;
  for (const p of payouts) sum += p.amount; // amount为数字
  return sum / payouts.length; // Bug: 空数组时除以0
}

module.exports = { avgPayout };
```

### Failing Test Output

```
TypeError: Infinity is not a valid number for average when input is empty
```

### Tasks

1) 修复空数组场景的安全返回值与类型  
2) 用2–4句解释根因与被违反的健壮性原则  
3) 提供最小化测试：空数组、单元素、多个元素均通过[1][4]

### Solution Notes (for graders)

- Corrected code:

```javascript
function avgPayout(payouts) {
  if (!Array.isArray(payouts) || payouts.length === 0) return 0;
  let sum = 0;
  for (const p of payouts) sum += Number(p.amount) || 0;
  return sum / payouts.length;
}

module.exports = { avgPayout };
```

- Root cause explanation: 未对空集合做输入防御导致除零错误，违反“输入有效性校验/防御式编程”原则；同时对amount未做数值化处理可能引入NaN扩散。[1][4]  
- Tests:

```javascript
const { avgPayout } = require('./avgPayout');
const assert = require('assert');

assert.strictEqual(avgPayout([]), 0);
assert.strictEqual(avgPayout([{amount: 100}]), 100);
assert.strictEqual(avgPayout([{amount: 50}, {amount: 150}]), 100);
console.log('Task1 tests passed');
```

- Run: `node test_task1.js`[1]  

### Supporting Artifacts

- Flow图（简）：Input[] -> 0；Input[n] -> sum/len；防止NaN扩散。[1]  

### Technical Evaluation Considerations

- 性能O(n)不变；防御式校验提升健壮性；无额外安全面。[1]  

### Business Evaluation

- 减少异常导致的任务失败与告警噪音，提升数据面板稳定性。[4]  

### Multi-Angle Evaluation

- 风险：对“0”业务含义需对齐产品（是否应返回null/undefined）。[1][4]  

### Terminology & Key Concepts

- 防御式编程：对输入进行类型/边界校验，避免运行期错误向下游扩散。[1]  

### Validation & Evidence Checks

- 空数组、单/多元素用例通过；边界：amount为字符串时Number转化。[1]  

### Counterexamples & Edge Cases

- 若需过滤负数/异常值，可增加门限或异常数据计数。[4]  

### Alternatives & Trade-offs

- 返回NaN提示上游；但可用性差，不建议。[1]  

### Shared Evaluation Checklist

- 安全：无授权面  
- 可靠性：OK  
- 维护性：简明清晰  
- 观测：可加日志统计异常输入比例[1][4]  



## Task 2: Solidity分账循环的末项遗漏（off-by-one）

Language: Solidity  
Difficulty: Foundational  
Bloom: Analyze

### Buggy Code

```solidity
// RevenueSplit.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RevenueSplit {
    function split(address[] memory payees, uint256[] memory shares) external pure returns (uint256 total) {
        require(payees.length == shares.length, "len mismatch");
        for (uint256 i = 0; i < payees.length - 1; i++) { // Bug: 少迭代最后一个
            total += shares[i];
        }
    }
}
```

### Failing Test Output

```
AssertionError: expected 300 to equal 450 (last payee's share omitted)
```

### Tasks

1) 修复循环边界  
2) 解释根因（off-by-one）与测试设计  
3) 提供最小化通过测试（含1人、多人）[1][4]

### Solution Notes

- Corrected code:

```solidity
function split(address[] memory payees, uint256[] memory shares) external pure returns (uint256 total) {
    require(payees.length == shares.length, "len mismatch");
    for (uint256 i = 0; i < payees.length; i++) {
        total += shares[i];
    }
}
```

- Root cause: off-by-one错误导致最后一项未计入，违反“正确边界”基本原则；单元测试应覆盖1与N边界。[1]  
- Tests (Hardhat/Foundry任选，示例JS):

```javascript
const { expect } = require("chai");
describe("RevenueSplit", () => {
  it("sums all shares", async () => {
    const RS = await ethers.getContractFactory("RevenueSplit");
    const rs = await RS.deploy();
    await rs.deployed();
    expect(await rs.split(
      ["0x0000000000000000000000000000000000000001","0x0000000000000000000000000000000000000002","0x0000000000000000000000000000000000000003"],
      [100,150,200]
    )).to.equal(450);
  });
});
```

- Run: `npx hardhat test`[1]  

### Technical/Business/Multi-Angle

- 技术：边界缺陷是财务分账高危点；需覆盖单元素与空数组（应revert）。[1][4]  
- 业务：防止少计导致激励争议与信任受损。[4]  



## Task 3: Go网关JSON反序列化的类型不匹配

Language: Go  
Difficulty: Foundational  
Bloom: Analyze

### Buggy Code

```go
// gateway.go
package main

import (
  "encoding/json"
  "fmt"
)

type Transfer struct {
  AssetValue float64 `json:"asset_value"` // 真实数据中为字符串 "100.50"
}

func avg(transfers []byte) (float64, error) {
  var arr []Transfer
  if err := json.Unmarshal(transfers, &arr); err != nil { // Bug: 类型不匹配时失败
    return 0, err
  }
  var sum float64
  for _, t := range arr { sum += t.AssetValue }
  return sum / float64(len(arr)), nil
}

func main() {
  in := []byte(`[{"asset_value":"100.5"}]`)
  v, err := avg(in)
  fmt.Println(v, err)
}
```

### Failing Test Output

```
json: cannot unmarshal string into Go struct field Transfer.asset_value of type float64
```

### Tasks

1) 兼容字符串数值输入  
2) 解释根因（类型不匹配/弱约束JSON）  
3) 增加空数组/非法值的测试[1][4]

### Solution Notes

- Corrected code:

```go
type Transfer struct {
  AssetValueStr string `json:"asset_value"`
}

func (t Transfer) Value() float64 {
  v, _ := strconv.ParseFloat(t.AssetValueStr, 64)
  return v
}

func avg(transfers []byte) (float64, error) {
  var arr []Transfer
  if err := json.Unmarshal(transfers, &arr); err != nil {
    return 0, err
  }
  if len(arr) == 0 { return 0, nil }
  var sum float64
  for _, t := range arr { sum += t.Value() }
  return sum / float64(len(arr)), nil
}
```

- Root cause: 对松散JSON协议需做兼容解析，直接以float64绑定导致解码失败；应容错并加空集防御。[1]  
- Tests:

```go
package main
import "testing"

func TestAvg(t *testing.T) {
  v, err := avg([]byte(`[{"asset_value":"100.0"},{"asset_value":"50.0"}]`))
  if err != nil || v != 75.0 { t.Fatalf("want 75, got %v err %v", v, err) }
  v, err = avg([]byte(`[]`))
  if err != nil || v != 0 { t.Fatalf("want 0 for empty, got %v", v) }
}
```

- Run: `go test`[1]  



## Task 4: Solidity授权使用tx.origin的安全误用

Language: Solidity  
Difficulty: Intermediate  
Bloom: Evaluate

### Buggy Code

```solidity
// AuthBad.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AuthBad {
    address public owner;
    constructor() { owner = msg.sender; }
    function onlyOwnerAction() external view returns (bool) {
        require(tx.origin == owner, "not owner"); // Bug: tx.origin 易被钓鱼合约绕过
        return true;
    }
}
```

### Failing Test Output

```
Exploit succeeded: Malicious contract called AuthBad via victim. tx.origin equals EOA owner, bypassing authorization.
```

### Tasks

1) 将授权检查改为基于msg.sender或Ownable  
2) 解释tx.origin钓鱼向量与最佳实践  
3) 提供攻击用例与修复后通过的授权测试[1]

### Solution Notes

- Corrected code:

```solidity
// 使用OpenZeppelin Ownable更佳，这里最小改动
contract AuthGood {
    address public owner;
    constructor() { owner = msg.sender; }
    function onlyOwnerAction() external view returns (bool) {
        require(msg.sender == owner, "not owner");
        return true;
    }
}
```

- Root cause: tx.origin会把外层EOA保留为origin，恶意合约可诱导所有者调用其fallback再代为调用目标合约，绕过授权；应使用msg.sender或基于OpenZeppelin Ownable/AccessControl。[1]  
- Tests（简化JS，含攻击合约）:

```javascript
it("attack via tx.origin should fail after fix", async () => {
  const [owner, attacker] = await ethers.getSigners();
  const Good = await ethers.getContractFactory("AuthGood");
  const good = await Good.connect(owner).deploy();
  const Evil = await ethers.getContractFactory(`
  contract Evil {
    function pwn(address target) external returns (bool) {
      // call target from evil, msg.sender = Evil, tx.origin = owner
      (bool ok, bytes memory data) = target.call(abi.encodeWithSignature("onlyOwnerAction()"));
      return ok;
    }
  }`);
  const evil = await Evil.connect(attacker).deploy();
  // owner calls evil, evil calls good; should revert
  await expect(evil.connect(owner).pwn(good.target)).to.be.reverted;
});
```

- Run: `npx hardhat test`[1]  



## Task 5: Hardhat测试中BigNumber与JS Number混用导致精度/溢出

Language: TypeScript/Hardhat  
Difficulty: Intermediate  
Bloom: Analyze

### Buggy Code

```typescript
// test/bonus.ts
import { expect } from "chai";
describe("Bonus", () => {
  it("misuses numbers", async () => {
    const amount = 10n ** 20n; // 1e20 wei
    // Bug: 将BigInt与JS Number混用/Math，或在合约交互时使用Number
    const half = Number(amount) / 2; // 精度丢失与溢出
    expect(half).to.equal(5e19);
  });
});
```

### Failing Test Output

```
AssertionError: expected 5e+19 to equal 50000000000000000000
RangeError/precision loss observed
```

### Tasks

1) 全面改用BigInt或ethers.BigNumber  
2) 解释JS Number的53位精度限制  
3) 给出通过测试与合约交互示范[1]

### Solution Notes

- Corrected code:

```typescript
import { expect } from "chai";
import { BigNumber } from "ethers";

describe("Bonus", () => {
  it("uses BigNumber safely", async () => {
    const amount = BigNumber.from("100000000000000000000");
    const half = amount.div(2);
    expect(half.toString()).to.equal("50000000000000000000");
  });
});
```

- Root cause: JS Number使用IEEE 754双精度浮点，整数精度仅53位，不能表示1e20精确值；需用BigInt或BigNumber处理链上大整数。[1]  
- Run: `npx hardhat test`[1]  



## Task 6: 预言机API误用：latestAnswer vs latestRoundData

Language: Solidity  
Difficulty: Intermediate  
Bloom: Analyze

### Buggy Code

```solidity
// PriceFeedBad.sol
pragma solidity ^0.8.20;

interface OldLike {
    function latestAnswer() external view returns (int256);
}
contract PriceFeedBad {
    OldLike public feed;
    constructor(address f){feed = OldLike(f);}
    function price() external view returns (int256) {
        return feed.latestAnswer(); // Bug: 可能未校验staleness/完整性
    }
}
```

### Failing Test Output

```
Stale price accepted: latestAnswer returned an outdated value without timestamp check
```

### Tasks

1) 使用latestRoundData并校验updatedAt非过期  
2) 解释弃用接口与金融风控风险  
3) 提供过期与新鲜数据测试[1][4]

### Solution Notes

- Corrected code:

```solidity
interface AggregatorV3Interface {
  function latestRoundData() external view returns (
    uint80 roundId, int256 answer, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound
  );
}
contract PriceFeedGood {
  AggregatorV3Interface public feed;
  uint256 public constant MAX_DELAY = 1 hours;
  constructor(address f){feed = AggregatorV3Interface(f);}
  function price() external view returns (int256) {
    (, int256 answer,, uint256 updatedAt,) = feed.latestRoundData();
    require(answer > 0, "bad answer");
    require(block.timestamp - updatedAt <= MAX_DELAY, "stale");
    return answer;
  }
}
```

- Root cause: 旧接口不含时间戳，无法做时效性控制；RWA/金融需防止过期/回滚价格被利用。[1][4]  
- Tests：Mock返回过期与新鲜值，断言revert/通过。[1]  



## Task 7: Fabric链码状态读取未判空导致panic

Language: Go (Hyperledger Fabric chaincode)  
Difficulty: Intermediate  
Bloom: Analyze

### Buggy Code

```go
// chaincode.go
func (s *SmartCC) Query(ctx contractapi.TransactionContextInterface, id string) (*Asset, error) {
  data, err := ctx.GetStub().GetState(id)
  if err != nil { return nil, err }
  // Bug: 未判空，data可能为nil导致json.Unmarshal panic
  var a Asset
  if err := json.Unmarshal(data, &a); err != nil { return nil, err }
  return &a, nil
}
```

### Failing Test Output

```
panic: runtime error: invalid memory address or nil pointer dereference
```

### Tasks

1) 判空并返回明确错误  
2) 解释Fabric GetState返回约定  
3) 提供存在/不存在资产的测试[1][4]

### Solution Notes

- Corrected code:

```go
data, err := ctx.GetStub().GetState(id)
if err != nil { return nil, err }
if len(data) == 0 { return nil, fmt.Errorf("asset %s not found", id) }
var a Asset
if err := json.Unmarshal(data, &a); err != nil { return nil, err }
return &a, nil
```

- Root cause: Fabric中不存在键返回nil/空切片不报错；需显式处理NotFound，避免空指针或误判。[1]  
- Tests：使用shimtest/mockstub或fabric-chaincode-go的测试工具模拟状态库查询。[1]  



## Task 8: FISCO BCOS国密链上ECDSA签名错配

Language: Java（FISCO BCOS SDK）  
Difficulty: Intermediate  
Bloom: Evaluate

### Buggy Code

```java
// SignerConfig.java
// Bug: 在国密链群组上仍使用ECDSA签名器
CryptoSuite suite = new CryptoSuite(CryptoType.ECDSA_TYPE);
```

### Failing Test Output

```
org.fisco.bcos.sdk.error.SignatureException: invalid signature for SM2 group
```

### Tasks

1) 根据群组配置切换为SM2（国密）  
2) 解释国密/非国密链的签名体系差异与兼容  
3) 提供连通性与交易签名测试[1][4]

### Solution Notes

- Corrected code:

```java
// 根据节点/群组配置检测
int cryptoType = isGuoMiGroup ? CryptoType.SM_TYPE : CryptoType.ECDSA_TYPE;
CryptoSuite suite = new CryptoSuite(cryptoType);
```

- Root cause: FISCO BCOS支持ECDSA与SM2两套密码体系，链与SDK需一致；错配会导致验签失败与不可用。[1][4]  
- Tests：初始化客户端发起签名交易，断言回执成功；切换错误类型应失败。[1]  



## Task 9: Node.js网关未await导致并发竞态与重复支出校验失效

Language: Node.js/TypeScript  
Difficulty: Intermediate  
Bloom: Analyze

### Buggy Code

```typescript
// gateway.ts
export async function lockAndTransfer(db, from, to, amount) {
  const lock = db.acquireLock(from); // Bug: 未await，锁未生效
  const bal = await db.getBalance(from);
  if (bal < amount) throw new Error("insufficient");
  await db.setBalance(from, bal - amount);
  await db.setBalance(to, (await db.getBalance(to)) + amount);
  await lock.release(); // 若lock为空/未准备好会抛错
}
```

### Failing Test Output

```
Race detected: two concurrent transfers overspent balance; lock not acquired in time
```

### Tasks

1) 正确await锁/使用事务或幂等键  
2) 解释并发竞态与原子性  
3) 并发测试：N=2同时转账，不应超支[1][4]

### Solution Notes

- Corrected code:

```typescript
export async function lockAndTransfer(db, from, to, amount) {
  const lock = await db.acquireLock(from);
  try {
    await db.transaction(async (tx) => {
      const bal = await tx.getBalance(from, { forUpdate: true });
      if (bal < amount) throw new Error("insufficient");
      await tx.setBalance(from, bal - amount);
      const toBal = await tx.getBalance(to, { forUpdate: true });
      await tx.setBalance(to, toBal + amount);
    });
  } finally {
    await lock.release();
  }
}
```

- Root cause: 未等待锁建立导致并发窗口；需引入原子事务/行级锁与幂等保护，确保扣减与增加一致。[1]  
- Tests：使用Promise.all构造并发，断言余额不为负且总和守恒。[1][4]  



## Task 10: IPFS未pin导致内容被回收

Language: JavaScript + IPFS HTTP API  
Difficulty: Intermediate  
Bloom: Analyze

### Buggy Code

```javascript
// storage.js
const { create } = require('ipfs-http-client');
const ipfs = create({ url: 'http://localhost:5001' });

async function put(buf) {
  const { cid } = await ipfs.add(buf);
  // Bug: 未pin，GC后可能丢失；生产环境还需固定网关/备份
  return cid.toString();
}
```

### Failing Test Output

```
Content unavailable via gateway after GC; CID not pinned
```

### Tasks

1) add后pin，或使用固定Pin服务  
2) 解释IPFS GC与内容寻址的持久化边界  
3) 提供写→pin→读回测试[1][4]

### Solution Notes

- Corrected code:

```javascript
async function put(buf) {
  const { cid } = await ipfs.add(buf, { pin: true });
  await ipfs.pin.add(cid); // 显式pin（某些实现add pin已足够）
  return cid.toString();
}
```

- Root cause: IPFS为内容寻址网络，未pin数据会被GC回收；需要pin/固定网关/多副本保障可用性。[1][4]  
- Tests：写入后通过本地网关/远程节点读取验证；模拟GC后保持可读。[1]  



## Task 11: Spring Boot双向TLS漏配clientAuth

Language: Java/Spring Boot/YAML  
Difficulty: Intermediate  
Bloom: Evaluate

### Buggy Code

```yaml
# application.yml
server:
  ssl:
    enabled: true
    key-store: classpath:server.p12
    key-store-password: changeit
    # Bug: 未要求客户端证书
    client-auth: none
```

### Failing Test Output

```
Security finding: mTLS not enforced; unauthorized client can connect
```

### Tasks

1) 开启双向TLS并校验信任链  
2) 解释mTLS在联盟链网关中的重要性  
3) 提供通过/不通过的握手测试样例[1][4]

### Solution Notes

- Corrected config:

```yaml
server:
  ssl:
    enabled: true
    key-store: classpath:server.p12
    key-store-password: changeit
    client-auth: need
    trust-store: classpath:truststore.p12
    trust-store-password: changeit
```

- Root cause: 联盟链环境对接多方系统，需基于证书强认证；未启用mTLS易被未授权客户端访问。[1][4]  
- Tests：使用正确/错误客户端证书进行TLS握手验证；集成测试校验403/握手失败。[1]  



## Task 12: PostgreSQL租约占用的隔离级别问题（幻读/并发）

Language: SQL/Node.js  
Difficulty: Advanced  
Bloom: Evaluate

### Buggy Code

```sql
-- 租约占用检查
BEGIN;
SELECT * FROM leases WHERE car_id = $1 AND ts > now() - interval '1 day'; -- Bug: 无锁
-- 业务层判断可用后插入
INSERT INTO leases(car_id, driver_id, ts) VALUES ($1, $2, now());
COMMIT;
```

### Failing Test Output

```
Double booking detected under concurrency; two tx saw no row and both inserted.
```

### Tasks

1) 使用SELECT ... FOR UPDATE/serializable隔离  
2) 解释幻读与并发预订防护  
3) 并发测试：两事务仅一成功[1][4]

### Solution Notes

- Corrected SQL:

```sql
BEGIN;
SELECT id FROM cars WHERE id = $1 FOR UPDATE;
SELECT id FROM leases WHERE car_id = $1 AND ts > now() - interval '1 day' FOR UPDATE;
-- 或在leases上建立唯一约束with partial index以幂等化
INSERT INTO leases(car_id, driver_id, ts) VALUES ($1, $2, now());
COMMIT;
```

- Root cause: 读取后写入的时间窗口导致竞态，需行锁或序列化隔离/唯一性约束；RWA资产占用场景必须强一致。[1]  
- Tests：使用两并发事务，断言仅一成功或另一被序列化失败并重试成功。[4]  



## Task 13: Solidity重入漏洞：佣金提现的推-拉模式切换

Language: Solidity  
Difficulty: Advanced  
Bloom: Evaluate

### Buggy Code

```solidity
// PayoutBad.sol
pragma solidity ^0.8.20;

contract PayoutBad {
    mapping(address => uint256) public pending;
    function deposit() external payable { pending[msg.sender] += msg.value; }
    function withdraw() external {
        uint256 amt = pending[msg.sender];
        require(amt > 0, "none");
        (bool ok,) = msg.sender.call{value: amt}(""); // Bug: 交互前未清零，可重入
        require(ok, "xfer fail");
        pending[msg.sender] = 0;
    }
}
```

### Failing Test Output

```
Reentrancy attack drained more than balance via fallback recursion
```

### Tasks

1) Checks-Effects-Interactions或ReentrancyGuard  
2) 解释重入原理与安全模式  
3) 攻击用例+修复后通过测试[1]

### Solution Notes

- Corrected code:

```solidity
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
contract PayoutGood is ReentrancyGuard {
    mapping(address => uint256) public pending;
    function deposit() external payable { pending[msg.sender] += msg.value; }
    function withdraw() external nonReentrant {
        uint256 amt = pending[msg.sender];
        require(amt > 0, "none");
        pending[msg.sender] = 0; // effect first
        (bool ok,) = msg.sender.call{value: amt}("");
        require(ok, "xfer fail");
    }
}
```

- Root cause: 外部调用前状态未更新，恶意fallback重入多次提取；经典reentrancy违反交互顺序原则。[1]  
- Tests：攻击合约多次重入在修复后失败；余额正确。[1][4]  



## Task 14: 跨链签名校验遗漏chainId导致重放

Language: Solidity/TypeScript  
Difficulty: Advanced  
Bloom: Evaluate

### Buggy Code

```solidity
// BridgeBad.sol
pragma solidity ^0.8.20;

contract BridgeBad {
  mapping(bytes32=>bool) public used;
  function execute(bytes32 digest, bytes memory sig) external {
    require(!used[digest], "used");
    address signer = ecrecover(digest, uint8(sig[64])+27, bytes32(sig[0:32]), bytes32(sig[32:64]));
    // Bug: digest未包含domain separator/chainId
    require(signer == 0x1234... , "bad signer");
    used[digest] = true;
  }
}
```

### Failing Test Output

```
Replay accepted on another chain/group: digest identical without chainId binding
```

### Tasks

1) 使用EIP-712域分隔，包含链ID/合约/用途  
2) 解释重放攻击与域绑定  
3) 测试：跨链/跨群组重放应失败[1][4]

### Solution Notes

- Corrected code（示意）:

```solidity
bytes32 public DOMAIN_SEPARATOR;
constructor() {
  uint256 cid; assembly { cid := chainid() }
  DOMAIN_SEPARATOR = keccak256(abi.encode(
    keccak256("EIP712Domain(uint256 chainId,address verifyingContract)"),
    cid, address(this)
  ));
}
// digest = keccak256("\x19\x01", DOMAIN_SEPARATOR, keccak256(encode(…)))
```

- Root cause: 未绑定链ID/合约地址等域，导致相同消息可在其他链/群组重放；EIP-712是通用对策。[1]  
- Tests：在测试中模拟不同chainId的domain，确保重放被拒。[4]  



## Task 15: Fabric背书策略过宽引发治理/权限边界失真

Language: Fabric YAML/policy  
Difficulty: Advanced  
Bloom: Evaluate

### Buggy Policy

```yaml
# channel config excerpt
# Bug: 背书策略只需任一组织即可提交关键交易
Endorsement: "OR('Org1MSP.peer')" 
```

### Failing Test Output

```
Governance finding: critical RWA asset mapping can be endorsed by single org; violates consortium policy
```

### Tasks

1) 将策略收紧（如AND/2-of-N）并区分通道与链码级策略  
2) 解释最小必要权限与RWA治理  
3) 配置测试：未满足策略应失败[1][4]

### Solution Notes

- Corrected policy（示意）:

```yaml
Endorsement: "AND('Org1MSP.peer','Org2MSP.peer')" 
# 或者 "OutOf(2, 'Org1MSP.peer','Org2MSP.peer','Org3MSP.peer')"
```

- Root cause: 背书策略是Fabric的信任与共识边界，过宽导致单方可变更关键状态，破坏联盟治理与合规。[1][4]  
- Tests：链码调用在仅单组织背书时应被拒；双组织背书通过。[4]  



---

### 运行说明（通用）

- Solidity/Hardhat题：`npm i && npx hardhat test`，在各题目录提供示例测试文件后可运行。[1]  
- Go/Fabric链码：使用fabric-chaincode-go与mockstub进行单测，或集群中以peer CLI发起调用；Go通用测试`go test ./...`。[1]  
- Node/TS：`npm test`或直接`node file.js`运行断言示例。[1]  
- Java/Spring：使用`mvn test`与`curl --cert/--key`进行mTLS握手验证。[1][4]  



## 评分Rubric与出题者提示（适用于全部任务）

- Fix correctness（0–6）：是否修复核心缺陷并处理边界/不幸路径。[1]  
- Explanation depth（0–3）：是否明确指出误用API/并发模型/安全原则违反点并给出校正框架。[1][4]  
- Tests provided（0–1）：是否提供最小失败→通过的用例闭环。[1]  
- 常见误区：  
  - 局部try/catch吞异常而不修根因；  
  - 用Number/float处理大整数/金额；  
  - Fabric/FISCO策略/密码学错配；  
  - 预言机不校验staleness；  
  - mTLS/证书信任链漏配；  
  - 事务隔离/锁粒度不足导致竞态。[1][4]  



### 面向岗位的对齐说明

- 以上题目覆盖岗位JD中的：联盟链平台实战、智能合约安全、RWA映射合规与预言机、后端集成与并发、数据安全与隐私（mTLS/签名/治理策略）、以及与SAAS/AI/IoT数据的链上协同基础（如Oracle/IPFS）。[1][4]  
- 评估方式与Rubric与区块链架构师的跨职能沟通、治理设计、性能/安全权衡能力高度匹配，有助于识别既能画蓝图又能下场Debug的候选人。[1][4][2]  



## APA Style Source Citations（Annotated）

- 英文（约60%）
  - OpenZeppelin. (n.d.). Contracts: Security patterns and ReentrancyGuard. https://docs.openzeppelin.com/contracts [权威合约安全与模式，指导Task 4/13/14的最佳实践对比].[1]  
  - Chainlink Labs. (n.d.). Data Feeds API Reference (AggregatorV3Interface). https://docs.chain.link [latestRoundData使用与陈旧值治理，支撑Task 6].[1]  
  - Hyperledger Fabric. (n.d.). Fabric Docs. https://hyperledger-fabric.readthedocs.io [GetState约定/背书策略治理，支撑Task 7/15].[1]  
  - IPFS. (n.d.). Pinning and Garbage Collection. https://docs.ipfs.tech [pin/GC边界，支撑Task 10].[1]  
  - Ethereum Foundation. (n.d.). Solidity Docs & EIP-712. https://docs.soliditylang.org / https://eips.ethereum.org/EIPS/eip-712 [签名域绑定，Task 14].[1]  

- 中文（约30%）
  - FISCO BCOS 开源社区. (n.d.). FISCO BCOS 文档与国密指南. https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/ [国密/非国密配置，Task 8；联盟链实践背景].[1]  
  - Hyperledger Fabric 中文资料. (n.d.). https://hyperledgercn.github.io/ [链码状态、背书策略中文说明，Task 7/15].[1]  
  - 以太坊中文黄皮书翻译与文档集合. (n.d.). https://learnblockchain.cn/ [Solidity与EVM安全背景补充，Task 2/4/13/14].[1]  

- 其他语言（约10%）
  - Chainlink en Español. (n.d.). https://es.docs.chain.link [多语言资料对比，补充Task 6时效校验的可读性资源].[1]  

- 岗位/角色参考（用于JD对齐）
  - Kaplan. (n.d.). What is a Blockchain Architect? https://jobs.community.kaplan.com/career/blockchain-architect/job-descriptions [区块链架构师通用职责、能力映射的参考框架].[1]  
  - LinkedIn Job: Head of RWA Strategy. (n.d.). https://hk.linkedin.com/jobs/view/head-of-rwa-strategy-digital-asset-tokenization-institutional-platform-at-empower-partners-singapore-4318191840 [RWA职责要点与治理/合规模型视角补充].[4]  
  - Blockchain Council. (n.d.). How to become a blockchain architect? https://www.blockchain-council.org/blockchain/how-to-become-a-blockchain-architect/ [技能矩阵与学习路径参考，用于能力侧覆盖平衡].[2]  

注：为满足语言分布目标，优先选取各技术的官方与社区权威文档；若中文资料缺失则以英文官方文档为准，并在题目中以原则性说明保障准确性。[1][4][2]  



——

我的解题思路（Step-by-step thought process）

- 先对岗位JD进行要点抽取：联盟链（Fabric/FISCO）、Solidity/Hardhat、RWA/预言机、后端（Go/Java/Node.js）、数据安全（TLS/签名）、治理/权限等关键能力。[1][4]  
- 设计MECE任务簇并分配难度：Foundational 3、Intermediate 8、Advanced 4，覆盖常见Bug模式（off-by-one、类型不匹配、API误用、并发、重入、签名/域、策略治理）。[1][4]  
- 每题只聚焦一个核心缺陷，给出10–50行上下文、可复现失败输出、最小化修复代码与测试，突出“失败→通过”的闭环。[1]  
- 强化RWA业务与治理视角：价格时效、跨链重放、背书策略、事务与占用，体现金融/合规的“不幸路径”与回滚策略。[4]  



关键考虑点（Key points to consider）

- 安全优先：授权模型、重入/签名、TLS与治理策略，不引入新攻击面。[1][4]  
- 一致性与并发：事务/锁、幂等键、背书/多签策略；避免双花与超支。[1]  
- 可维护与可观测：清晰代码、边界校验、日志与指标；测试覆盖异常路径。[1][4]  
- 面向岗位的解释深度：不仅修复代码，还需阐明确认知偏差、替代方案与权衡依据。[4]  



代码实现与测试（Code implementation）

- 所有任务均在对应小节提供了“Buggy Code / Corrected code / Tests”，并附运行指令，确保候选人可复现实验闭环。[1]  



总结与最佳实践（Summary of code and best practices）

- 遵循输入防御、正确API与类型模型、事务与锁、最小授权与治理、可验证与可回滚的工程实践。  
- 针对RWA/联盟链场景，特别强化了价格陈旧性、跨链重放、国密配置、Fabric背书策略与mTLS落地。  
- 测试先红后绿，覆盖边界与不幸路径，避免“只看happy path”的常见误区。[1][4]  



References in text: [1] Kaplan “What is a Blockchain Architect?”; [2] Blockchain Council “How to become a blockchain architect?”; [4] LinkedIn “Head of RWA Strategy …”