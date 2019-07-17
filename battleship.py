import numpy as np
from qiskit.quantum_info import Pauli
from qiskit.aqua import Operator

class Battleship:
  def __init__(self, r, c):
    self.r = np.array(r)
    self.c = np.array(c)
    self.dim = np.array([len(r), len(c)])
    self.nqubit = np.multiply.reduce(self.dim)

  def _gridIndexToQubitNumber(self, i, j):
    return i * self.dim[1] + j

  def _getPauli(self, w, zList):
    xp = np.zeros(self.nqubit, dtype=np.bool)
    zp = np.zeros(self.nqubit, dtype=np.bool)

    for (i, j) in zList:
      zp[self._gridIndexToQubitNumber(i, j)] = True
    
    return [w, Pauli(zp, xp)]

  def getQubitOps(self):
    pauliList = []
    shift = np.sum(self.c**2) + np.sum(self.r**2)

    # sum ij term
    for i in range(self.dim[0]):
      for j in range(self.dim[1]):
        pauliList.append(self._getPauli(self.r[i] + self.c[j] - 1, [(i, j)]))
        shift += (1 - self.r[i] - self.c[j])

    # sum i j!=k term
    for i in range(self.dim[0]):
      for j in range(self.dim[1]):
        for k in range(j + 1, self.dim[1]):           
          pauliList.append(self._getPauli(-0.5, [(i, j)]))
          pauliList.append(self._getPauli(-0.5, [(i, k)]))
          pauliList.append(self._getPauli(0.5, [(i, j), (i, k)]))
          
          shift += 0.5

    # sum j i!=k term   
    for j in range(self.dim[1]):
      for i in range(self.dim[0]):
        for k in range(i + 1, self.dim[0]):
          pauliList.append(self._getPauli(-0.5, [(i, j)]))
          pauliList.append(self._getPauli(-0.5, [(k, j)]))
          pauliList.append(self._getPauli(0.5, [(i, j), (k, j)]))
          
          shift += 0.5
            
    return Operator(paulis=pauliList), shift
    