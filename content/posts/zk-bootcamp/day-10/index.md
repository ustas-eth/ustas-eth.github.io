---
title: "Day 10"
weight: 10
---

## Day 10
### Privacy in Layer 2 and presentation by Josh Crites from Aztec!
> One of the largest remaining challenges in the Ethereum ecosystem is privacy ... In practice, using the entire suite of Ethereum applications involves making a significant portion of your life public for anyone to see and analyze. - Vitalik Buterin

It is important to differentiate the terms of Privacy, Confidentiality, and Anonymity.

There are different approaches to privacy:
- Obfuscation
- Hardware assistance
- Fully Homomorphic Encryption
- Commitment schemes and nullifiers (like zCash and Tornado Cash)

Some of the projects that are developing private solutions in Web3:
- Aztec
- Zama
- Namada
- Obscuro
- Penumbra
- Anoma

Josh did the second part of the lesson. 

Private execution on blockchains like Aztec, Aleo, Mina, and Miden:
1. Simulate a transaction on localhost
2. Create the ZKP proof of this transaction
3. Send the proof and state difference to the network
4. The Sequencer will check the proof and create a rollup proof

Aztec uses the UTXO model like Bitcoin because they say it is impossible to use the account model like Ethereum to create a private blockchain. Thus, they don't try to implement zkEVM but rather use their own VM.

![Transaction lifecycle on Aztec](media/txlifeaztec.png)

Noir is a Rust-like language that's used to write programs on Aztec. Interestingly, it uses a language-wide trusted setup, so you don't have to run it on your own.

