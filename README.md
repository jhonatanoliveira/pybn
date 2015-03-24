# pybn
## A simple python library for Bayesian Network modelling and inference

**Features**:
   * A Directed Acyclic Graph (DAG) class with following functions: parents, children, ancestors, descendants, all v-structures, moralize.
   * An Undirected Graph implementation.
   * A a-Separation class for testing independencies.
   * i-Separation, an alternative method for testing independencies ina  DAG, which considers inaugural variables and its descendants and is faster in bigger netoworks.
   * Conditional Probability Table (CPT) implementation with multiplication, division, marginalization, among other operations.
   * Elimination Ordering (Min-Neighbor, Min-Weight, Min-Filll, Weithed-Min-Fill)
   * Variable Eimination (removing barren variables, independent by evidence variables, creating one tables of new root variables, and so on).

**Utilities**:
   * Load network from BIF files.
