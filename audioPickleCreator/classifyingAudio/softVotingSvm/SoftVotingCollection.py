

class SoftVotingCollection():
	def __init__(self, groupClassifiers):
		self.listGroupedClassifiers = groupClassifiers

	def predict(self, data):
		for groupedClassifier in self.listGroupedClassifiers:
			results = groupedClassifier.predictData(data)
			print("\n resutls\n")
			print(results)
			if(results["passed"] > results["failed"]):
				return 1

		return 0