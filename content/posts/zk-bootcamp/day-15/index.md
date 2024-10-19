---
title: "Day 15"
weight: 15
---

## Day 15
### Overview of Proving Systems
In this lesson, we repeated some parts from the previous ones, like the history of ZKP, trusted setup, SNARK vs STARK, etc. 

STARK uses FRI as a commitment scheme, which stands for Fast Reed-Solomon IOP of Proximity. They have a much larger proof size (like 100 kB), which is not feasible if we talk about L1 Ethereum, but a transparent setup due to the chosen commitment scheme, plus the post-quantum security.

During the lesson, I also discovered that Boojum is meant to be a fusion of STARK and SNARK. Specifically, big brains from zkSync want to make proofs of the EVM execution as STARKs and then prove these STARKs with SNARK to make the proofs more succinct. I have my doubts about the effectiveness of such an approach because I think we still have to make the trusted setup for the SNARK part, and it won't be post-quantum secure. But probably there's a good explanation.
If you want to read more, check the official announcement: https://zksync.mirror.xyz/HJ2Pj45EJkRdt5Pau-ZXwkV2ctPx8qFL19STM5jdYhc

UPD. I asked Porter about this, and he said that we indeed have to run the trusted setup. Also, he mentioned that there's no real point in post-quantum security for zk-rollups at the moment due to the fact that we use ECDSA anyway, and it is not secure in the post-quantum world.

#### Halo 2
It is a proving system that combines PLONK, recursion from Halo 1, and the Inner Product Argument commitments scheme.
You can find the documentation on the official site: https://halo2.dev

#### Mina
A pretty interesting blockchain that works entirely on ZKP without L1.

