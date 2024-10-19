---
title: "Day 9"
weight: 9
---

## Day 9
### What's next in L2, part 2: L3s/Hyperchains
#### ZoKrates
Finally! ZK practice! Haha 🏴‍☠️

ZoKrates is a toolbox for on-chain zkSNARKs. You can install it in Remix and try to make some circuits, too. It supports Groth16, GM17, and Marlin.
Check out [this guide](https://medium.com/coinmonks/zokrates-zksnarks-on-ethereum-made-easy-8022300f8ba6). It is basically what we did in the lesson.

#### How L3 can be useful
The naïve idea is to make layers in recursion to scale the L1 blockchain in recursion. The truth is many mechanisms that are used in L2 cannot be repeated. The most useful utility of L3s is specific functionality like privacy.

I've spent part of the lesson discussing with Greg and Coogan. My perspective on the limitations of L4+ blockchain layers in terms of transaction fees and scalability is that they would be as constrained as L3 due to the inherent computational costs associated with processing transactions, so there's really no point in going further than L3.

#### Interoperability of L2s
One of the attractive ideas currently present is to avoid L1 when interacting between different L2 and instead send messages directly. Laurence outlined this is more complicated with Optimistic rollups like Arbitrum and Optimism.

![Direct interaction](media/directinteraction.png)

For example, the blockchains built on OP Stack (like Optimism and Base) are supposed to have this kind of interaction between them. I guess the costs of such interactions will be similar to L2 fees.

ZK Stack aims for an easy and customizable framework for L2 and L3 hyperchains that can also interact in between.

#### Proofs aggregation
There are several ways to aggregate several proofs of the same type into one to make verification more scalable:
1. Simple proof aggregation, where you make some kind of a Merkle tree from proofs combining P1 and P2 to get P1+P2
2. More complex layered aggregation

We will cover this topic later in the bootcamp.

