__author__ = 'Jules'


class Task(object):
	def __init__(self, function, argTuple=()):
		super(Task, self).__init__()
		self._function = function
		self._argTuple = argTuple

	def run(self):
		self._function(*self._argTuple)


class StopWorkerTask(Task):
	def __init__(self):
		super(Task, self).__init__()
		self._function = self
		self._argTuple = None

	def __name__(self):
		return "STOP_WORKER_TASK"
