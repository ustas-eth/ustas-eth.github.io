---
title: "Day 19"
weight: 19
---

## Day 19
### Plonk, part 2: Boojum
#### Customizable Constraint Systems
An interesting and new concept of generalization of the usual constraint systems:
![CCS](media/ccs.png)

#### [Plonky2](https://github.com/0xPolygonZero/plonky2)
It is a library by Polygon that allows us to create SNARKs with PLONK and FRI.
We've taken a quick example of how to make a circuit to prove a polynomial. Check out the corresponding homework; I'll make a Rust program with Plonky2 later.

#### Presentation of Boojum by Oles Holembovskyy from zkSync
The execution trace table has a size of ~$240$ columns with ~$2^{20}$ rows, which contain gates, lookup arguments, and copy-permutation arguments. Columns define how many variables a gate can have or how many gates can be placed in a row.

Check the repo: https://github.com/matter-labs/era-boojum

##### Copy-permutation arguments
They allow us to establish constant relations between cells and prove that these cells are equal.

##### Gates
Gates are polynomial equations over cells in one row. E.g., boolean check: $`x^2 - x = 0`$. Gate columns in the table can be of general purpose or specialized. The difference is in the performance and the use of available space. The specialized columns contain gates that apply to every row in the table (like a boolean check), while the general-purpose columns can contain different numbers of different gates.

Boojum has a list of available gates: boolean allocator, constant allocator, conditional select, reduction gate, U32 add, Poseidon, etc., similar to the instructions in a CPU.

##### Lookup columns
These columns are used to optimize the circuit. They also can be general or specialized, but in practice, they almost always are the latter. Boojum has a number of native lookup tables: binary operations, SHA256, range check, etc.

##### Boojum Gadgets
- Numeric types like Boolean, UInt8, UInt256. You can allocate new variables in the constraint system, put a value inside, and create a constraint. The types are optimized; e.g., they use lookup tables to check ranges of UInts.
- Poseidon hashes
- Keccak / SHA256
- Modulo arithmetic
- Elliptic curves
- Pairing

