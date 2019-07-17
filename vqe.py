from qiskit.aqua.algorithms import VQE

class VQEWithHistory(VQE):
  def _run(self):
    self._history = []
    
    return super()._run(), self._history

  def _energy_evaluation(self, parameters):
    mean_energy = super()._energy_evaluation(parameters)

    self._history.append(mean_energy)

    return mean_energy
