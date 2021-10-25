# <center>CS 511 midterm exam note</center>

## concurrent programming
- The study of systems of interacting computer programs which
share resources and run concurrently, i.e. at the same time
- Parallelism
  - Occurring physically at the same time
- Concurrency
  - Occurring logically at the same time, but could be implemented without real parallelism
- If P has m instructions and Q has n instructions, then there are (m+n)!/(m!n!)
## mutual exclusion
### atomic operation
An operation is atomic if it cannot be interleaved at a lower level of abstraction
- Atomic operations are the smallest units in terms of which a path can be constituted
- In order to reason about concurrency at the source level, we need to know what is assumed atomic at the source level
  - Following Ben-Ari: we assume throughout this course that all (single-line) statements are atomic
  - In particular, assignments such as `counter = counter+1` are assumed atomic
### LCR(limited critical reference)
A program satisfies the Limited Critical Reference (LCR) property if every statement contains at most one critical reference
### MEP(mutual exclusion problem)
1. Mutex: At any point in time, there is at most one thread in the critical section
2. Absence of livelock: If various threads try to enter the critical section, at least one of them will succeed
3. Free from starvation: A thread trying to enter its critical section will eventually be able to do so
### await
    `while(cond){} == await (!cond)`
**await: false to loop, true to continue next excution**
### attempt 1 take truns
```
int turn = 1;
Thread . start { // P
    // non - critical section
    await (turn ==1);
    // CRITICAL SECTION
    turn = 2;
    // non - critical section
}
Thread . start { // Q
    // non - critical section
    await (turn ==2);
    // CRITICAL SECTION
    turn = 1;
    // non - critical section
}
```
mutex: yes, absence live lock: yes, Free from startvation:no(a process could remain indefinitely in its non-critical section)
### Dekker's Algorithm
