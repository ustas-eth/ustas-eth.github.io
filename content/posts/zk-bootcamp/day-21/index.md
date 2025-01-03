---
title: "Day 21"
weight: 121
---

### Formal Verification
Today's topic was about verifying the correctness of a proving system or a circuit with formal verification. This technique is increasingly popular and has stronger guarantees than static analysis or fuzzing.

Projects and tools:
- [Veridise](https://veridise.com/zk/) is a company that maintains different security tools. [Picus](https://github.com/Veridise/Picus) is one of them. It implements the &QED^2&, which checks the uniqueness property (under-constrained signals) of ZKP circuits.
- [Aleo Vanguard](https://github.com/Veridise/vanguard-aleo), another tool by Veridise for Leo/Aleo programs.
- [Horus](https://www.nethermind.io/horus) by Nethermind provides formal verification for the StarkNet smart contracts.
- [Ecne](https://0xparc.org/blog/ecne) is a tool for R1CS verification.
- [Kestrel Labs](https://www.kestrel.edu/research/fv-of-r1cs/).
- [Coda](https://github.com/Veridise/Coda), verification of Circom.

### Fiat-Shamir Security
Weak Fiat-Shamir transformation can affect the soundness of many proving systems. The problem is that some implementations don't include all the required parameters in the FS hash computation. Read more about it in the [Trail of Bits disclosure](https://blog.trailofbits.com/2022/04/18/the-frozen-heart-vulnerability-in-plonk/) of the vulnerability.

### Folding Schemes
Previously, to include recursion into our SNARK, we had to have a verifier as a part of the circuit. Folding schemes allow us to take the verification out of it completely. This allows us to aggregate proofs in order to optimize our SNARK.

A common approach is to use inner and outer circuits similar to the [described before](#presentation-by-emily-and-alexandre-from-linea) scheme by Linea. The inner circuit will provide fast proving and the outer will make the proof small.

Projects:
- Nova
- Sangria
- Protostar
- Supernova
- Hypernova

