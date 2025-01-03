---
title: "Day 20"
weight: 120
---

### ZKML
You all know what ChatGPT or Bard is; no news here, I guess. You've probably also heard about how these models are trained. During the process, the neural networks of the machines are adjusted. Each node has its weight. Each iteration can change these weights.

#### Use cases
ZKML (**Z**ero-**K**nowledge **M**achine **L**earning) allows us to:
- Prove the match an input with an output in a succinct way.
- Make ML-as-a-service transparent. The providers of these services can add proofs to their API so the users can know a certain version of a model with the chosen parameters processed their input. Right now, the API is a black box from a user's perspective.
- Strengthen security with fraud/anomaly detection.
- Provide privacy for users. Their inputs can be hidden from the model. E.g., ZK proofs can be used to train a model from personal medical data without its disclosure.
- Create on-chain neural networks.

#### Efficiency
Currently, our ZK techniques are still not efficient enough to handle big models, but it is possible with smaller ones.
Read more in this article: https://medium.com/@ModulusLabs/chapter-5-the-cost-of-intelligence-da26dbf93307

#### The Ecosystem
Read more about each project [here](https://github.com/zkml-community/awesome-zkml).
![ZKML](zkml-../media/zkml-ecosystem.jpeg)

