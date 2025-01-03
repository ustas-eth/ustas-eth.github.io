---
title: "Day 17"
weight: 117
---

### STARK implementation
STARKs, as was mentioned before, don't have toxic waste. This means we can make a transparent setup quick and easy. Also, they are quantum secure, but it is more like a nice topping. The fundamental security assumption of a STARK is a collision-resistant hash function, a well-known cryptographic primitive.

Cairo VM (Starknet) uses AIR (arithmetic intermediate representation) arithmetization, in opposite to the popular R1CS.

#### Computation integrity
It is one of the features of STARKs (and SNARKs). Computation integrity means we can prove that some algorithm/program/circuit/computation was executed correctly. In the context of Cairo and zkEVMs this property is more important than zero-knowledge, for example, because the data is public.

#### [Reed-Solomon error correction](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)
Reed–Solomon codes are a world-used technique that allows us to find and correct broken/lost bits of data in all the mighty Internet and computer world (CD/DVDs, QR codes, broadcast systems, storage systems like data centers) by adding redundant information.

#### FRI (Fast Reed-Solomon IOP of Proximity)
This is what STARK uses as a polynomial commitment scheme. Check [this video](https://www.youtube.com/watch?v=ySlibAm9IVM) by RISC Zero to learn more. FRI allows us to check if the commitment of a polynomial is of a low degree.

### Presentation by Henri Lieutaud from Starknet
I knew some things about Cairo and Starknet already, but the presentation was pretty solid and covered some of my blind spots. Henri shared a little of the history of Starkware company, which is interesting.
What's even cooler is that Cairo VM is actually an idea of a broader caliber than sole blockchains. Starknet is a validity rollup on L1, which is only one of the things that can be built with Cairo. You can make a usual computer program with the provable execution property. 

Compilation path: Cairo (higher language) -> Sierra (Safe Intermediate Representation) -> CASM (assembly) -> Validity Proofs

Starknet itself is not compatible with EVM. But there's another program in Cairo, [Kakarot](https://www.kakarot.org/), which implements EVM.

There's also SHARP (Shared Prover), which can take a Cairo program and generate proofs. It is used for Starknet and Starex, for example.
They've recently disclosed the source code of Stone, which can be run on a local machine to prove and verify Cairo 0 (Python) programs.

