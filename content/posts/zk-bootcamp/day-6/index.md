---
title: "Day 6"
weight: 6
---

## Day 6
### Agnostic Layer 2 Transaction Lifecycle
More Rust things like traits, generics, vectors, iterators, and shadowing.

On the previous day, we concentrated on OP Stack, but it is only fair to mention ZK Stack by zkSync and Madara by StarkNet:
https://blog.matter-labs.io/introducing-the-zk-stack-c24240c2532a
https://starkware.co/resource/harnessing-the-beast-madara-and-the-revolution-of-starknet-appchains/

Generally speaking, L2s follow a similar design.
![Mental Model for Layer 2s](media/mentalmodel.png)

As you can see, Users send their transactions to the Sequencer, which executes these, batch, compresses, and submits to L1. The final component is an L1 smart contract that verifies the outputs of the Sequencer.

Differences between ZKP and Optimistic visualized:
![Differences between ZKP and Optimistic](media/diffZKPOP.png)

