# Blockchain Node Developer — Coding Task (GPT-5)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/Coding_Task.md](../../Prompts/Templates/Coding_Task.md). Role context from [Job_Description.md](Job_Description.md).

## Contents

- [Task Bank](#task-bank-tasks-1-18)
- [Topic 1: Clients & RPC](#topic-1-clients--rpc)
- [Topic 2: Storage & Indexing](#topic-2-storage--indexing)
- [Topic 3: Networking & Consensus](#topic-3-networking--consensus)
- [Topic 4: Operations & Reliability](#topic-4-operations--reliability)
- [Reference Sections](#reference-sections)

---

## Task Bank (Tasks 1–18)

### Topic 1: Clients & RPC

#### Task 1: JSON-RPC Batch Splitter

**Language:** go | **Difficulty:** Foundational

**Problem:** Given a list of JSON-RPC requests, split into batches of size ≤N and return the list of batches. Preserve order.

**Signature:** `func SplitBatches(reqs []json.RawMessage, n int) [][]json.RawMessage`

**Starter Code:**
```go
package rpcutil
import "encoding/json"
func SplitBatches(reqs []json.RawMessage, n int) [][]json.RawMessage {
    // TODO
    return nil
}
```

**Public Tests:**
```go
package rpcutil
import "encoding/json"
func must(s string) json.RawMessage { return json.RawMessage(s) }
func ExampleSplitBatches() {
    in := []json.RawMessage{must("{}"), must("{}"), must("{}")}
    out := SplitBatches(in, 2)
    // want 2 batches: [2,1]
    _ = out
}
```

**Hidden Tests:** n=1; n>=len; empty input; large input.

**Reference Solution:**
```go
func SplitBatches(reqs []json.RawMessage, n int) [][]json.RawMessage {
    if n <= 0 { n = 1 }
    res := make([][]json.RawMessage, 0, (len(reqs)+n-1)/n)
    for i := 0; i < len(reqs); i += n {
        j := i + n
        if j > len(reqs) { j = len(reqs) }
        chunk := make([]json.RawMessage, j-i)
        copy(chunk, reqs[i:j])
        res = append(res, chunk)
    }
    return res
}
```
**Complexity:** O(m). | **Alternatives:** Iterators.

**Grading:** Correctness 70, Edge 20, Style 10.

---

#### Task 2: Engine API JWT Builder (HS256)

**Language:** go | **Difficulty:** Intermediate

**Problem:** Build a JWT for Engine API auth with exp in seconds from now and audience "engine".

**Signature:** `func BuildJWT(secret []byte, ttl time.Duration) (string, error)`

**Starter Code:**
```go
package enginejwt
import "time"
func BuildJWT(secret []byte, ttl time.Duration) (string, error) {
    // TODO
    return "", nil
}
```

**Public Tests:**
```go
// verify it parses and exp is within [now, now+ttl+1s]
```

**Hidden Tests:** invalid secret; zero ttl.

**Reference Solution:**
```go
import (
  "github.com/golang-jwt/jwt/v5"
  "time"
)
func BuildJWT(secret []byte, ttl time.Duration) (string, error) {
    now := time.Now()
    claims := jwt.RegisteredClaims{Audience: jwt.ClaimStrings{"engine"}, ExpiresAt: jwt.NewNumericDate(now.Add(ttl)), IssuedAt: jwt.NewNumericDate(now)}
    t := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return t.SignedString(secret)
}
```
**Complexity:** O(1). | **Alternatives:** EdDSA where supported.

**Grading:** Correctness 70, Edge 20, Style 10.

---

#### Task 3: Rate Limit Token Bucket

**Language:** go | **Difficulty:** Intermediate

**Problem:** Implement a token bucket that allows R tokens per second with burst B.

**Signature:** `type Bucket struct{ /* ... */ }`

**Starter Code:**
```go
package ratelimit
import "time"

type Bucket struct{
    r float64
    b float64
    tokens float64
    last time.Time
}
func NewBucket(r, b float64) *Bucket { return &Bucket{r:r, b:b, tokens:b, last: time.Now()} }
func (bk *Bucket) Allow(n float64) bool {
    // TODO
    return false
}
```

**Public Tests:** allow small bursts; refill over time.

**Hidden Tests:** zero/negatives; large n.

**Reference Solution:**
```go
func (bk *Bucket) Allow(n float64) bool {
    now := time.Now()
    elapsed := now.Sub(bk.last).Seconds()
    bk.tokens = min(bk.b, bk.tokens+elapsed*bk.r)
    bk.last = now
    if bk.tokens >= n { bk.tokens -= n; return true }
    return false
}
func min(a,b float64) float64 { if a<b{return a};return b }
```
**Complexity:** O(1). | **Alternatives:** time.Ticker.

**Grading:** Correctness 70, Edge 20, Style 10.

---

#### Task 4: getLogs Window Enforcer

**Language:** go | **Difficulty:** Foundational

**Problem:** Given start and end blocks and a max window W, slice into non‑overlapping windows of size ≤W.

**Signature:** `func Windows(start, end, W uint64) [][2]uint64`

**Starter Code:**
```go
package logswin
func Windows(start, end, W uint64) [][2]uint64 { return nil }
```

**Public Tests:** 0..99 with W=20 yields 5 windows.

**Hidden Tests:** off‑by‑one; start>end.

**Reference Solution:**
```go
func Windows(start, end, W uint64) [][2]uint64 {
    if start > end || W==0 { return nil }
    out := make([][2]uint64, 0, (end-start+W)/W)
    s := start
    for s <= end {
        e := s+W-1
        if e> end { e = end }
        out = append(out, [2]uint64{s,e})
        if e==^uint64(0) { break }
        s = e+1
    }
    return out
}
```
**Complexity:** O(n/W). | **Alternatives:** iterators.

**Grading:** Correctness 70, Edge 20, Style 10.

---

#### Task 5: Bloom Filter (Simplified)

**Language:** go | **Difficulty:** Intermediate

**Problem:** Implement a simple bloom filter with k hash functions over a bitset.

**Signature:** `type Bloom struct{/*..*/}` with `Add([]byte)` and `Test([]byte) bool`.

**Starter Code:**
```go
package bloom
import "hash/fnv"

type Bloom struct{ bits []byte; k int }
func New(m int, k int) *Bloom { return &Bloom{bits: make([]byte, (m+7)/8), k:k} }
func (b *Bloom) Add(p []byte) { /* TODO */ }
func (b *Bloom) Test(p []byte) bool { return false }
```

**Public Tests:** basic add/test.

**Hidden Tests:** collisions; bounds.

**Reference Solution:**
```go
func (b *Bloom) indexes(p []byte) []int {
    out := make([]int, b.k)
    for i:=0;i<b.k;i++{ h := fnv.New64a(); h.Write([]byte{byte(i)}); h.Write(p); out[i] = int(h.Sum64()) % (len(b.bits)*8) }
    return out
}
func (b *Bloom) set(i int){ b.bits[i/8] |= 1<<(uint(i)%8) }
func (b *Bloom) get(i int) bool { return (b.bits[i/8] & (1<<(uint(i)%8)))!=0 }
func (b *Bloom) Add(p []byte){ for _,i := range b.indexes(p){ b.set(i) } }
func (b *Bloom) Test(p []byte) bool { for _,i := range b.indexes(p){ if !b.get(i) { return false } } ; return true }
```
**Complexity:** O(k). | **Alternatives:** siphash.

**Grading:** Correctness 70, Edge 20, Style 10.

---

#### Task 6: P95/P99 Calculator

**Language:** go | **Difficulty:** Foundational

**Problem:** Given latencies in ms, compute p95 and p99.

**Signature:** `func P95P99(xs []float64) (float64, float64)`

**Starter Code:**
```go
package stats
import "sort"
func P95P99(xs []float64) (float64,float64){ return 0,0 }
```

**Public Tests:** typical arrays;

**Hidden Tests:** empty input; NaNs.

**Reference Solution:**
```go
func P95P99(xs []float64) (float64,float64){
    if len(xs)==0 { return 0,0 }
    cp := append([]float64(nil), xs...)
    sort.Float64s(cp)
    i95 := int(0.95*float64(len(cp)-1))
    i99 := int(0.99*float64(len(cp)-1))
    return cp[i95], cp[i99]
}
```
**Complexity:** O(n log n).

---

#### Task 7: Exponential Backoff with Jitter

**Language:** go | **Difficulty:** Foundational

**Problem:** Return next delay = min(base*2^attempt + U(0,jitter), max).

**Signature:** `func Backoff(base, max, jitter time.Duration, attempt int) time.Duration`

**Starter Code:**
```go
package backoff
import "time"
func Backoff(base, max, jitter time.Duration, attempt int) time.Duration { return 0 }
```

**Reference Solution:**
```go
import "math/rand"
func Backoff(base, max, jitter time.Duration, attempt int) time.Duration {
    if attempt < 0 { attempt = 0 }
    d := base << uint(attempt)
    if d > max { d = max }
    if jitter > 0 { d += time.Duration(rand.Int63n(int64(jitter))) }
    if d > max { d = max }
    return d
}
```

---

#### Task 8: Context-Aware HTTP Client

**Language:** go | **Difficulty:** Intermediate

**Problem:** Perform JSON-RPC POST with context timeout and retry using backoff.

**Signature:** `func Call(ctx context.Context, url string, payload []byte) ([]byte, error)`

**Starter Code:**
```go
package rpcc
import ("context"; "net/http"; "io")
func Call(ctx context.Context, url string, payload []byte) ([]byte, error){ /* TODO */ return nil,nil }
```

**Reference Solution:** (abbrev)
```go
// create req with ctx; client timeout from ctx; do; read body; handle retryable codes with backoff
```

---

### Topic 2: Storage & Indexing

#### Task 9: SSTable Size Alignment

**Language:** go | **Difficulty:** Intermediate

**Problem:** Given record sizes, pack into SSTable blocks of size B to minimize slack.

**Signature:** `func Pack(sizes []int, B int) [][]int`

**Reference Solution:** First‑fit decreasing heuristic.

---

#### Task 10: Range Window Iterator

**Language:** go | **Difficulty:** Foundational

**Problem:** Iterate [start,end] by fixed step.

**Signature:** `func Iterate(start,end,step uint64) <-chan [2]uint64`

---

#### Task 11: Reorg-Safe Upsert Key

**Language:** sql | **Difficulty:** Intermediate

**Problem:** Write a PostgreSQL upsert for (block_hash, tx_hash, log_index) to ensure idempotency.

**Reference Solution:**
```sql
INSERT INTO logs(block_hash,tx_hash,log_index,topic0)
VALUES ($1,$2,$3,$4)
ON CONFLICT (block_hash,tx_hash,log_index)
DO UPDATE SET topic0=EXCLUDED.topic0;
```

---

#### Task 12: Snapshot Hash Verify

**Language:** go | **Difficulty:** Foundational

**Problem:** Compute SHA256 of a file stream and compare to expected hex.

---

### Topic 3: Networking & Consensus

#### Task 13: Gossip Mesh Score Update

**Language:** go | **Difficulty:** Intermediate

**Problem:** Update peer score given invalid ratio and contribution.

---

#### Task 14: Finality Monitor Metric

**Language:** go | **Difficulty:** Foundational

**Problem:** Compute head–finalized slot distance and emit Prometheus gauge.

---

#### Task 15: Light Client Header Verify (Stub)

**Language:** rust | **Difficulty:** Advanced

**Problem:** Verify SSZ header signature with BLS (stubbed interface).

**Reference Solution:** Outline with traits and error types.

---

### Topic 4: Operations & Reliability

#### Task 16: Hedged Request Wrapper

**Language:** go | **Difficulty:** Intermediate

**Problem:** Given a function `Do(ctx)` issue a hedge after T ms and return first success.

---

#### Task 17: p99 Alert Evaluator

**Language:** go | **Difficulty:** Foundational

**Problem:** Given rolling window latencies, alert if p99 exceeds threshold for K consecutive windows.

---

#### Task 18: Tenant Quota Enforcer

**Language:** go | **Difficulty:** Intermediate

**Problem:** Implement per‑tenant counters with sliding window.

---

## Reference Sections

See [../../Prompts/Shared_References.md](../../Prompts/Shared_References.md). This note reuses references from `QA_GPT-5.md`; floors satisfied across the pack.
