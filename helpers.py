import numpy as np
import matplotlib.pyplot as plt

def getSolutionFromResult(result):
  return max(result['min_vector'], key=result['min_vector'].get)

def printResultSummary(result, shift):
  print("VQE Result")
  print("- Running time: %.2f sec" % result['eval_time'])
  print("- Evaluation count:", result['eval_count'])
  print("- Final energy:", result['energy'] + shift)
  print("- Solution:", getSolutionFromResult(result))

def plotEnergyHistory(history, shift):
  fig, ax = plt.subplots(figsize=(8,6))
  ax.plot(np.arange(0, len(history)), np.array(history) + shift)

  ax.set_title("VQE Ising Hamiltonian Energy", size=20)
  ax.set_ylabel("energy", fontsize=15)
  ax.set_xlabel("timestep", fontsize=15)

  plt.show()
