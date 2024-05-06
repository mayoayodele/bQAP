
# Solving Bi-objective Quadratic Assignment Problems using CQM
This project contains code for the paper titled 'Utilising Quantum Hybrid Solver for Bi-objective Quadratic Assignment Problems'.  

The bi-objective QAP is an extension of the classic QAP that incorporates two distinct objectives. The QAP involves assigning a set of facilities to a set of locations in a way that minimises the sum of the products between flows and distances. In the bi-objective variant, there are two such cost functions to minimise. The challenge in the bi-objective QAP is to find assignments that achieve a good balance between these two objectives. This requires navigating the trade-offs between both objectives to identify Pareto-optimal solutions,these are solutions for which no other solution is better in both objectives and therefore represent the best compromises available in the solution space.
An instance of the bi-objective QAP consists of a $2 \times n \times n$ flow matrix $H=[h_{kij}]$ and a $n \times n$ distance matrix $D=[d_{kl}]$. The two-way one-hot also known as permutation matrix representation is used in this implementation. The cost and constraint functions of the bi-objective QAP is defined as



 $$c(x) = \sum_{a=1}^{2} \lambda_a \cdot \left( \sum_{i=1}^{n}\sum_{j=1}^{n}\sum_{k=1}^{n}\sum_{l=1}^{n}h_{k,i,j}d_{k,l}x_{i,j}x_{j,l} \right)$$

 $$ g_{1,i}(x) = \sum_{j=1}^{n} x_{i,j}  \equiv 1\  \forall\  i \in { 1,\cdots ,n } $$

$$ g_{2,j}(x) = \sum_{i=1}^{n} x_{i,j}  \equiv 1\  \forall\  j \in \{ 1,\cdots ,n \}$$

# Problem Instances

The bi-objective instances as well as the Pareto optimal solutions can be found in https://eden.dei.uc.pt/~paquete/qap/


# Getting Started
## Install the requirements
  ```sh
   pip install -r requirements.txt
   ```
## Set parameters in config.yaml
 ```sh
   problem-name:  'qapStr.25.0.1' 
   scalarisation-method: 'uniform'
   number-of-weights: 10
   time-limit: 5
   ```

## Run the code
  ```sh
   python main.py
   ```
# Example
The plot below shows a run comparing all three aggregation methods. Each method was executed with exactly 10 scalarisation weights

problem instance __qapStr.25.0.1__
![plot](https://github.com/mayoayodele/bQAP/blob/main/plots/qapStr.25.0.1.png)

problem instance __qapStr.25.p75.1__
![plot](https://github.com/mayoayodele/bQAP/blob/main/plots/qapStr.25.p75.1.png)

problem instance __qapStr.25.n75.1__
![plot](https://github.com/mayoayodele/bQAP/blob/main/plots/qapStr.25.n75.1.png)

# Additional Notes
Although the methods presented in this work are general, this implementation uses the CQM solver. Installation information for this solver can be found in https://docs.ocean.dwavesys.com/en/stable/overview/install.html  

# References

1. Ayodele, M., 2024, July. Utilising Quantum Hybrid Solver for Bi-objective Quadratic Assignment Problems. In Proceedings of the Companion Conference on Genetic and Evolutionary Computation (GECCO '24 Companion). Association for Computing Machinery, New York, NY, USA. https://doi.org/10.1145/3638530.3664097


2. Mayowa Ayodele, Richard Allmendinger, Manuel López-Ibáñez, Arnaud Liefooghe, and Matthieu Parizy. 2023. Applying Ising Machines to Multi-objective QUBOs. In Proceedings of the Companion Conference on Genetic and Evolutionary Computation (GECCO '23 Companion). Association for Computing Machinery, New York, NY, USA, 2166–2174. https://doi.org/10.1145/3583133.3596312
