---
title: "Day 16"
weight: 16
---

## Day 16
### SNARK implementation
As mentioned on [Day 13](#day-13), SNARKs comprise a probabilistic proof and a commitment scheme. They usually require a setup where we establish a) the program that will be proved and b) some randomness.

The randomness is useful both in interactive and non-interactive proofs. We use it to keep the system sound because otherwise, the Prover can craft malicious proofs. The system won't be sound if the values we use to create randomness are known. That's why it's important to create ceremonies with many independent participants. If at least one of them is honest, the system is good to go. And this is the reason why we would want to use STARKs because they don't require such a ceremony.

STARKs also require randomness, but there's no toxic waste like in SNARKs; no secret values in the setup. This is why we call them transparent.

#### Polynomial checking
We can express the gate constraints as follows:

```math
L := \sum_{i=1}^{m} * ci * Li, 

R := \sum_{i=1}^{m} * ci * Ri, 

O := \sum_{i=1}^{m} * ci * Oi, 
```

Where L is the left input of a gate, R is the right one, and O is the output. And the polynomial $`P`$ that contains all the constraints will be:

```math
P := L * R − O
```

In other words, all the lefts multiplied by all the rights minus all the outputs should be zero.

The Verifier will create a target polynomial from the roots, something like:

```math
V(x) := (x − 1) * (x − 2)...
```

$`P`$ is $`V`$ multiplied by some number, and it also should be equal to zero if the constraints are met. In such a case, the Verifier can divide $`P`$ by $`V`$, and there will be no remainder.

The above also means there's some polynomial $`P'`$ such that $`P = P' * V`$, and the Verifier can pick random (remember about the trusted setup?) $`z`$ values and ask the Prover or the oracle to check if the statement $`P(z) = P'(z) * V(z)`$ still holds.

The degree of $`P`$ is at most $`2(d - 1)`$; $`L`$, $`R`$, $`O`$ at most $`d - 1`$; $`V`$ at most $`d - 2`$

#### Trace tables
Check out [this great article by Scroll](https://scroll.io/blog/proofGeneration). You'll find examples of the trace tables and more math there.

#### [Fiat-Shamir heuristic](https://en.wikipedia.org/wiki/Fiat%E2%80%93Shamir_heuristic)
This is the final operation of any SNARK or STARK that makes them non-interactive. The basic principle is that instead of a random value from the Verifier (which is why the proofs are interactive), the Prover takes a hash of several parameters. It is similar to how we use keccak in Solidity sometimes when we want to verify some data or get pseudo-randomness.

I recommend you to check the Wiki because it has quite an illustrative example.

Similar to the keccak in smart contracts (permit signature), the Prover can manipulate parameters if they are not included in the hash.

