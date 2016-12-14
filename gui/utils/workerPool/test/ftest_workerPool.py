from unittest import TestCase
from threading import Event, current_thread

from gui.utils.workerPool.workerPool import WorkerPool


class TestWorkerPool(TestCase):
	POOL_SIZE = 2

	def setUp(self):
		self.workerPool = WorkerPool(TestWorkerPool.POOL_SIZE)

	def tearDown(self):
		self.workerPool.stop()

	def testAddedTasksAreDone(self):
		taskDoneEvent = Event()

		def notifyTaskDone():
			taskDoneEvent.set()

		self.workerPool.start()
		self.workerPool.addTask(notifyTaskDone)

		eventWasSet = taskDoneEvent.wait(1)

		self.assertTrue(eventWasSet)

	def testIfSeveralTasksAreAddedThenTheyAreAllDone(self):
		events = [Event() for _ in range(20)]

		def setEvent(event):
			event.set()

		self.workerPool.start()
		for event in events:
			self.workerPool.addTask(setEvent, event)

		allEventsWereSet = True

		for event in events:
			allEventsWhereSet = allEventsWereSet and event.wait(3)

		self.assertTrue(allEventsWhereSet)

	def testAllThreadsInThePoolWork(self):
		workersCalled = []
		events = [Event() for _ in range(self.POOL_SIZE)]

		def taskFunction(previousEvent):
			workersCalled.append(current_thread())

			try:
				event = events.pop()
				self.workerPool.addTask(taskFunction, event)
				event.wait(5)
			except IndexError:
				previousEvent.set()

			previousEvent.set()

		self.workerPool.start()

		firstEvent = events.pop()

		self.workerPool.addTask(taskFunction, firstEvent)

		allEventsWhereSet = firstEvent.wait(10)

		self.assertTrue(allEventsWhereSet)
		self.assertEqual(TestWorkerPool.POOL_SIZE, len(set(workersCalled)))

	def testStoppingThePoolGuaranteesThatAllTasksWereDone(self):
		self.workerPool.start()
		tasksQueue = self.workerPool._tasksQueue
		self.workerPool.stop()

		self.assertTrue(tasksQueue.empty())

	def testStoppingThePoolTwiceDoesNothing(self):
		self.workerPool.start()
		self.workerPool.stop()
		self.workerPool.stop()

		self.assertFalse(self.workerPool.isRunning())

	def testPoolIsNotRunningWhenInstantiated(self):
		self.assertFalse(self.workerPool.isRunning())

	def testPoolIsRunningWhenStartIsCalled(self):
		self.workerPool.start()

		self.assertTrue(self.workerPool.isRunning())

	def testPoolIsNotRunningWhenStopIsCalled(self):
		self.workerPool.start()
		self.workerPool.stop()

		self.assertFalse(self.workerPool.isRunning())

	def testPoolSupportsTasksWithParameters(self):
		self.workerPool.start()
		global localVar1
		global localVar2
		global localVar3

		localVar1 = None
		localVar2 = None
		localVar3 = None

		def setValue(value1, value2, value3):
			global localVar1
			global localVar2
			global localVar3

			localVar1 = value1
			localVar2 = value2
			localVar3 = value3

		self.workerPool.addTask(setValue, "SUPER VALUE", "AMAIZING VALUE", "OSOM VALUE")

		self.workerPool.stop()

		self.assertIsNotNone(localVar1)
		self.assertIsNotNone(localVar2)
		self.assertIsNotNone(localVar3)
