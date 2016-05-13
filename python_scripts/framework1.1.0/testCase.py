#class for a testcase object
#holds a step, an expected, a result and any conditions of that result

class testCase():

	def __init__(self, step, expected, result, result_conditions):
		self.step = step
		self.expected = expected
		self.result = result
		self.result_conditions = result_conditions