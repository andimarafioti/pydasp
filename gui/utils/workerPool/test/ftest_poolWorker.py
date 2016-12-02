from _weakrefset import WeakSet
from threading import Event, current_thread
from unittest import TestCase

from utils.workerPool.fifoPriorityQueue import FIFOPriorityQueue
from utils.workerPool.poolWorker import PoolWorker
from utils.workerPool.task import Task

__author__ = 'Jules'


class TestPoolWorker(TestCase):
	def setUp(self):
		self.tasksQueue = FIFOPriorityQueue()
		self.canceledTasksQueue = WeakSet()
		self.poolWorker = PoolWorker(self.tasksQueue, self.canceledTasksQueue)

	def tearDown(self):
		self.tasksQueue.put((1, PoolWorker.STOP_TASK))

	def testWorkersStayAliveEvenIfTaskRaisesAnException(self):
		taskDoneEvent = Event()

		def setTaskDone():
			taskDoneEvent.set()

		def raiseException():
			raise Exception("Foo")

		self.poolWorker.start()

		self.tasksQueue.put((1, Task(raiseException)))
		self.tasksQueue.put((1, Task(setTaskDone)))

		workerKeptWorking = taskDoneEvent.wait(1)

		self.assertTrue(self.poolWorker.isAlive())
		self.assertTrue(workerKeptWorking)

	def testWorkersRunTasksFromTheirQueue(self):
		taskDoneEvent = Event()

		def setTaskDone():
			taskDoneEvent.set()

		self.poolWorker.start()

		self.tasksQueue.put((1, Task(setTaskDone)))

		taskDone = taskDoneEvent.wait(1)

		self.assertTrue(taskDone)

	def testWorkerThreadsRunAsDaemons(self):
		global isRunningAsDaemon
		isRunningAsDaemon = False

		def setIsRunningAsDaemon():
			global isRunningAsDaemon
			isRunningAsDaemon = current_thread().isDaemon()

		self.poolWorker.start()

		self.tasksQueue.put((1, Task(setIsRunningAsDaemon)))
		self.tasksQueue.join()

		self.assertTrue(isRunningAsDaemon)

	def testWorkersStopRunningWhenSTOP_TASKIsQueued(self):
		self.poolWorker.start()

		self.tasksQueue.put((1, PoolWorker.STOP_TASK))

		self.poolWorker.join(1)

		self.assertFalse(self.poolWorker.isAlive())

	def testWorkersDontStartRunningUntilToldTo(self):
		queue = FIFOPriorityQueue()
		canceledSet = WeakSet()
		poolWorker = PoolWorker(queue, canceledSet)

		self.assertFalse(poolWorker.isAlive())

		poolWorker.start()

		self.assertTrue(poolWorker.isAlive())

		queue.put((1, PoolWorker.STOP_TASK))
