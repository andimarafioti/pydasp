import logging
from _weakrefset import WeakSet

from gui.utils.workerPool.poolWorker import PoolWorker
from gui.utils.workerPool.fifoPriorityQueue import FIFOPriorityQueue
from gui.utils.workerPool.task import Task

__author__ = 'Jules'

logger = logging.getLogger('[WORKER POOL]')
logger.setLevel(logging.INFO)


class WorkerPool(object):
	def __init__(self, poolSize=4):
		super(WorkerPool, self).__init__()

		self._isRunning = False

		self._tasksQueue = FIFOPriorityQueue()
		self._canceledTasks = WeakSet()
		self._workers = [PoolWorker(self._tasksQueue, self._canceledTasks) for _ in range(poolSize)]

	def start(self):
		logger.info("Starting WorkerPool...")

		for worker in self._workers:
			worker.start()

		self._isRunning = True

		logger.info("WorkerPool started.")

	def stop(self):
		logger.info("Stopping WorkerPool...")

		if not self._isRunning:
			logger.warning("Attempted to stop a WorkerPool twice.")
			return

		for _ in range(len(self._workers)):
			self._tasksQueue.put((5, PoolWorker.STOP_TASK))

		self._isRunning = False

		self._tasksQueue.join()

		logger.info("WorkerPool stopped.")

	def addTask(self, function, *args):
		if not self._isRunning:
			logger.debug("Task not added to (stopped) queue: %s%s", function.__name__, str(args))
			return

		logger.debug("Adding task to queue: %s%s", function.__name__, str(args))
		task = Task(function, args)
		self._tasksQueue.put((3, task))

		return task

	def addHighPriorityTask(self, function, *args):
		if not self._isRunning:
			logger.debug("HIGH PRIORITY task not added to (stopped) queue: %s%s", function.__name__, str(args))
			return

		logger.debug("Adding HIGH PRIORITY task to queue: %s%s", function.__name__, str(args))
		task = Task(function, args)
		self._tasksQueue.put((0, task))

		return task

	def addLowPriorityTask(self, function, *args):
		if not self._isRunning:
			logger.debug("LOW PRIRITY task not added to (stopped) queue: %s%s", function.__name__, str(args))
			return

		logger.debug("Adding LOW PRIORITY task to queue: %s%s", function.__name__, str(args))
		task = Task(function, args)

		self._tasksQueue.put((4, task))

		return task

	def cancelTask(self, task):
		logger.debug("Adding CANCELLATION for task: %s%s", task._function.__name__, str(task._argTuple))
		self._canceledTasks.add(task)

	def isRunning(self):
		return self._isRunning

