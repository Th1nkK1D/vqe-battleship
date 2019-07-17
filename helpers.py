def getSolutionFromResult(result):
  return max(result['min_vector'], key=result['min_vector'].get)

def printResultSummary(result, shift):
  print("VQE Result")
  print("- Running time: %.2f sec" % result['eval_time'])
  print("- Evaluation count:", result['eval_count'])
  print("- Final energy:", result['energy'] + shift)
  print("- Solution:", getSolutionFromResult(result))
