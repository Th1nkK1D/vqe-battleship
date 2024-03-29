# Variational Quantum Eigensolver (VQE) for Battleship Puzzle with Qiskit

**Withee Poositasai**, Computer Engineering, King Mongkmut's University of Technology Thonburi (KMUTT), Thailand

with **Prof. Hsi-Sheng Goan**, Department of Physics, National Taiwan University (NTU), Taiwan

The research was conducted under **MOST GASE Q+ Summer Program 2019** from 17 June to 27 July 2019

## Abstract

Quantum computer have a potential to solve NP problem which are difficult for classical computer. By mapping problem corresponded cost function into Ising harmiltonian, the problem then can be solved by quantum optimization algorithm. In this research, I studied variational quantum eigensolver (VQE), which is a gate-based hybrid optimization algorithm method purposed by IBM, and used it to solve simple battleship puzzle in a simulation with Qiskit, IBM’s Python library for quantum computing. The result show that the correct solution can be obtain if the puzzle size is not big enough and entanglement in variational form doesn’t show a positive effect in this problem.

## Table of Content

1. Introduction
2. Variational Quantum Eigensolver (VQE)
3. Simple Battleship Puzzle
4. Simulation
5. Result
6. Conclusion

## 1. Introduction

There are computational problems that are difficult to solve by classical computer. And it is impossible when the problem size is big enough. We call this kind of problem as NP (None-deterministic polynomial time). Even though it is difficult to solved but the solution of those problem can be verified easily, using cost function. Energy function, sometime called cost function, is use to evaluate how bad of the solution is. The less energy, the better corresponded solution. Which mean if we can find the solution that give minimum value, zero if the energy function is normallized, that would be our best solution to the corresponding problem. And, we can call the problem we want to find the solution that will give a minimum cost as an “Optimization problem”.

Optimization algorithm, algorithms that used to solve optimization problem, play an important role in computational field. It can be used in many field such as forecasting, image processing and artificial intelligence. With a limitation on classical computer and enormous pace on quantum computing development now a day, many researchers start to pay an attention on quantum optimization algorithm. Chemistry and combinatorial problems, which both are NP problem, are the main focuses. In this research, I focused on “Variational quantum eigensolver”

## 2. Variational Quantum Eigensolver (VQE)

Variational quantum eigensolver (VQE) is a hybrid algorithm, it use computing power from both quantum computer and classical computer. Main purpose of VQE is to find the quantum state that give the minimum energy according to the Ising Hamiltonian.

![Goal of VQE](https://latex.codecogs.com/gif.latex?min&space;\langle&space;\psi(\theta)|&space;H&space;|&space;\psi(\theta)&space;\rangle)

Where Harmiltonian (H) represent a cost function in [Ising model](https://en.wikipedia.org/wiki/Ising_model) form. For example:

![Ising Hamiltonian](https://latex.codecogs.com/gif.latex?H(\sigma)&space;=&space;-&space;\sum_{ij}&space;J_{ij}&space;\sigma_i&space;\sigma_j&space;-&space;\mu&space;\sum_{j}&space;h_j&space;\sigma_j)

Sigma is representing electron spin which can be either -1 or 1. This is equivalent to Pauli-Z operator in quantum computing theory. Eigenvalues of Pauli-Z are 1 and -1 which represent 2 possible observable 

VQE algorithm is working as following steps:

![How VQE work?](https://grove-docs.readthedocs.io/en/latest/_images/VQE.png)

1. Classical computer decide a set of initial parameters (&theta;) and send it to quantum computer.
2. Quantum computer prepare the state (&Psi;) with the variational form using &theta;.
3. Each term of Ising Hamiltonian is used to measure the state 
4. All measurement results are sent back to classical computer to get an energy summation.
5. New &theta; is decided by classical optimization algorithm which expected to decrease next iteration energy.
6. Keep iterating until the energy is converged. Final state (&Psi;) is corresponding to the solution.

## 3. Simple Battleship Puzzle

Many chemical and combinatorial problems were purposed that it can be solved by VQE but I want to do some experiment with problem that no one have done it before.

There is a puzzle called Battleship, one of my favourite puzzle and there is a research paper proving that this problem is NP. Anyway, the original battleship puzzle is very complicated and it needed a lot of resources. For a game with W x H grid size and S number of ship, W x H x S number of qubits are required. We don’t have quantum computer with that high amount of qubits yet. Moreover, a simulation on classical computer would only allow 18 qubit as a maximum.

So I made a simplified version of battleship puzzle with following rules:
1. There is only 1 ship size, which is 1x1 and the number of ship that can be used is not limited.
2. Ship can be placed anyway on the board with maximum 1 ship on each cells.
3. Number of the ships in each row and column must satisfy the pre-defined value.

Example of simple 3x3 battleship game with correct solution:

```
Simple Battleship
size: 3 x 3 

| x |   |   | 1
| x | x | x | 3
| x | x |   | 2
  3   2   1   
```

The cost function of my simple battleship puzzle would be:

![Simple battleship cost function](https://latex.codecogs.com/gif.latex?E(x)&space;=&space;\sum_i&space;\bigg(&space;\sum_j&space;x_{ij}&space;-&space;R_i\bigg)^2&space;&plus;&space;\sum_j&space;\bigg(\sum_i&space;x_{ij}&space;-&space;C_j&space;\bigg)^2)

Where i is row index, j is column index, x indicate whether that cell contain a ship (0 or 1), R is a set of defined number of ship in each row and C is a set of defined number of ship in each column.

Then, it can be mapped  to following Ising hamiltonian:

![Simple battleship ising hamiltonian](https://latex.codecogs.com/gif.latex?H(Z)&space;=&space;\sum_{ij}&space;\big[&space;(1-R_i-C_j)&plus;(R_i&plus;C_j-1)Z_{ij}&space;\big]&space;&plus;&space;\sum_i&space;\bigg[&space;\frac12&space;\sum_{j<k}&space;\big(&space;1&space;-&space;Z_{ij}&space;-&space;Z_{ik}&space;&plus;&space;Z_{ij}Z_{ik}\big)&space;&plus;&space;R_i^2&space;\bigg]&space;&plus;&space;\sum_j&space;\bigg[&space;\frac12&space;\sum_{i<k}&space;\big(&space;1&space;-&space;Z_{ij}&space;-&space;Z_{kj}&space;&plus;&space;Z_{ij}Z_{kj}&space;\big)&space;&plus;C_j^2&space;\bigg])

## 4. Simulation

Now everything is ready for a simulation. IBM provide [Qiskit library](https://qiskit.org/) which allow us to create a quantum circuit and run it on either a simulation or the real IBM quantum computer using Python language. There are many algorithms that already implemented in Qiskis Aqua package, including VQE. So I wrote a Battleship class representing simple battleship problem and it has a method to generate a list of qubits operation according to each term in the Ising hamiltonian. I also overrides some method in Qiskit’s VQE class to keep track of the energy in each iteration. Then I ran a simulation with several grid sizes and variational form depths at maximum 651 iterations.

```
VQE Result
- Running time: 118.97 sec
- Evaluation count: 651
- Final energy: 0.0
- Solution: 1011

Simple Battleship
size: 2 x 2 

| x | x | 2
|   | x | 1
  1   2   
```

[Open simulation Jupyter Notebook (simple-battleship.ipynb)](https://github.com/Th1nkK1D/vqe-battleship/blob/master/simple-battleship.ipynb)

## 5. Result

It’s turn out that only 2x2 and 3x3 puzzle size can be solved. As we can see from the left figure, the energy converge to 0 while the 4x4 puzzle size does not. As the puzzle size increase, the number of qubit operations that need to be evaluated from each hamiltonian term is exponentially increased, as well as the runtime according to the right figure. So it is difficult for problem to be solved as the size is getting bigger.

For the variational form depth (level of entanglement), the more entanglement we added, the more difficult for energy to converge. So for the 3x3 puzzle size, only variational form without entanglement can lead us to the correct solution. That could be because the solution of the combinatorial problem is just a normal state, neither a superposition nor mix state. So entanglement don’t have a positive effect on this problem, and maybe for other combinatorial problems as well.

[Open experiments result Jupyter Notebook (test-cases-comparison.ipynb)](https://github.com/Th1nkK1D/vqe-battleship/blob/master/test-cases-comparison.ipynb)

Anyway, it is not clear if this method can outperform other classical algorithms. Many papers suggest that it can outperform classical computer on chemistry problem which is involving the real quantum mechanics system. But for the combinatorial problem, it is still take an exponential growth of run time when the problem size is increased.

## 6. Conclusion

Quantum computer have a potential to solve NP problem, such as combinatorial problem, if an Ising hamiltonian representing problem energy can be constructed. From the simulation with variational quantum eigensolver (VQE) on simple battleship puzzle, the correct solution can be obtained if the problem size is not too large. Anyway, according to limitations we have in the real quantum computer and classical computer simulation, it is still arguable if the quantum computer can outperform classical computer on optimization problems or not.

## Special Thanks
- Pei-kai Tsai and Yao-ting Lin for helpful discussions
- Min-chi Lee for taking care of me during the lab stay
- MOST GASE staffs for making this program happended
- Everyone else for being my good company!

## References
- [The Ising model: teaching an old problem new tricks](https://www.dwavesys.com/sites/default/files/weightedmaxsat_v2.pdf)
- [Ising formulations of many NP problems](https://arxiv.org/abs/1302.5843)
- [A variational eigenvalue solver on a quantum processor](https://arxiv.org/abs/1304.3061)
- [Quantum optimization using variational algorithms on near-term quantum devices](http://home.agh.edu.pl/~kozlow/fizyka/obliczenia%20kwantowe/Moll_2018_Quantum_Sci._Technol._3_030503.pdf)
- [Performance of hybrid quantum/classical variational heuristics for combinatorial optimization](https://arxiv.org/abs/1805.12037)
- [Qiskit Official Tutorial](https://nbviewer.jupyter.org/github/Qiskit/qiskit-tutorials/blob/master/qiskit/start_here.ipynb)
- [Quantum Algorithm Implementations for Beginners](https://arxiv.org/abs/1804.03719)
- [Battleships As Decidability Problem](https://pdfs.semanticscholar.org/b623/82bcebee19a7cfeb1cfc18e6b1b05c680dfb.pdf)
- [Solving the Battleship Puzzle as an Integer Programming Problem](https://pubsonline.informs.org/doi/pdf/10.1287/ited.1100.0047)
