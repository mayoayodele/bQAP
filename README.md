
# Solving Bi-objective Quadratic Assignment Problems using CQM
This project contains code for the paper titled 'Utilising Quantum Hybrid Solver for Bi-objective Quadratic Assignment Problems'.  

The bi-objective QAP is an extension of the classic QAP that incorporates two distinct objectives. The QAP involves assigning a set of facilities to a set of locations in a way that minimises the sum of the products between flows and distances. In the bi-objective variant, there are two such cost functions to minimise. The challenge in the bi-objective QAP is to find assignments that achieve a good balance between these two objectives. This requires navigating the trade-offs between both objectives to identify Pareto-optimal solutions,these are solutions for which no other solution is better in both objectives and therefore represent the best compromises available in the solution space.
An instance of the bi-objective QAP consists of a $2 \times n \times n$ flow matrix $H=[h_{kij}]$ and a $n \times n$ distance matrix $D=[d_{kl}]$. The two-way one-hot also known as permutation matrix representation is used in this implementation. The cost function of the bi-objective QAP is defined as



## Constraint Handling Methods


```math
a_1(x) = \left ( 1- \sum_{i=1}^n x_{i,j} \right )^2
```

```math
a_2(x) = \left ( 1- \sum_{i=1}^n x_{j,i} \right )^2
```

```math
g_1(x) = \sum_{j=1}^n a_1(x)
```

```math
g_2(x) = \sum_{j=1}^n a_2(x)
```



|                       | Vertical one-hot | Horizontal one-hot |Implementation of Constraints                                                                    |
| --------------------- | -----------------| ------------------ |-------------------------------------------------------------------------------------------------|
| tsp_cqm1/ qap_cqm1    | $g_1$            | $g_2$              |add_constraint( $g_1$ ), add_constraint( $g_2$ )                                                 |
| tsp_cqm2/ qap_cqm2    | $g_1$            | $g_2$              |add_constraint($g_1 + g_2$)                                                                      |
| tsp_cqm2/ qap_cqm2    | $g_1$            | add_discrete       |add_constraint($g_1$)                                                                            |
| tsp_cqm4/ qap_cqm4    | $a_1$            | $a_2$              |add_constraint($a_1i$), add_constraint($a_2i$) $\forall$ $i$ $\in$ {1,...,n}  |
| tsp_cqm5/ qap_cqm5    | $a_1$            |add_discrete        |add_constraint($a_1i$) $\forall$ $i$ $\in$ {1,...,n}  |



# References

1. Ayodele, M., 2024, July. Utilising Quantum Hybrid Solver for Bi-objective Quadratic Assignment Problems. In Proceedings of the Companion Conference on Genetic and Evolutionary Computation (GECCO '24 Companion). Association for Computing Machinery, New York, NY, USA, 2166–2174. https://doi.org/10.1145/3583133.3596312


2. Mayowa Ayodele, Richard Allmendinger, Manuel López-Ibáñez, Arnaud Liefooghe, and Matthieu Parizy. 2023. Applying Ising Machines to Multi-objective QUBOs. In Proceedings of the Companion Conference on Genetic and Evolutionary Computation (GECCO '23 Companion). Association for Computing Machinery, New York, NY, USA, 2166–2174. https://doi.org/10.1145/3583133.3596312
