---
title: "Day 13"
weight: 13
---

## Day 13
### What are ZK EVMs, part 3: Proving systems
Week 4, more than half of the bootcamp.

#### Polynomial Commitment Schemes
A simple example of a commitment scheme in Solidity is:
1. You make a keccak hash of some secret string, e.g., "hello".
2. Then you save it in a smart contract storage.
3. Anybody can see the hash and make some operations, knowing you can't change the underlying string.
4. After the operations have been done, you reveal the string. You don't have much choice but to reveal "hello", because any other string would produce another hash.

A polynomial commitment is similar to the hash of a private string: it is a short representation of that polynomial. Given such a commitment, as a Verifier, you can run a number of experiments to see if the Prover is truthful in its statements.

This gives us three useful properties:
- Prover cannot change the polynomial after a commitment.
- Verifier cannot compute the polynomial from a commitment itself.
- Commitments are more succinct.

Common commitment schemes are:
- FRI
- KZG
- IPA
- DARK

Check [this video](https://www.youtube.com/watch?v=bz16BURH_u8) to find out more.

Cool slide from the video:
![PCS comparison](media/pcscomp.png)

#### Interactive Oracle Proofs
Check [this](https://youtu.be/bGEXYpt3sj0?list=PLS01nW3Rtgor_yJmQsGBZAg5XM4TSGpPs&t=3920)

Different combinations of commitment schemes and interactive oracle proofs result in different proving systems with different characteristics: post-quantum security, transparency, good proof size, verification time, etc.

