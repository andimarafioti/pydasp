import logging
import traceback
from threading import Thread, current_thread

from utils.workerPool.task import StopWorkerTask

__author__ = 'Jules'

logger = logging.getLogger('[WORKER POOL]')


class PoolWorker(Thread):
	STOP_TASK = StopWorkerTask()

	def __init__(self, tasksQueue, canceledTasks):
		super(PoolWorker, self).__init__()
		self.setDaemon(True)
		self._tasksQueue = tasksQueue
		self._canceledTasks = canceledTasks

	def run(self):
		logger.info("PoolWorker <%s> started.", current_thread().ident)
		while True:
			task = self._tasksQueue.get(block=True)

			if task is PoolWorker.STOP_TASK:
				self._tasksQueue.task_done()
				logger.info("PoolWorker task stopped, empty: %s", self._tasksQueue.empty())
				break

			if task in self._canceledTasks:
				self._tasksQueue.task_done()
				logger.debug("PoolWorker <%s> canceled call: %s%s", current_thread().ident, task._function.__name__,
							 str(task._argTuple))
				continue

			logger.debug("PoolWorker <%s> is about to call: %s%s", current_thread().ident, task._function.__name__,
						 str(task._argTuple))

			try:
				task.run()
			except Exception:
				logger.warning("PoolWorker <%s> catched an exception calling: %s%s", current_thread().ident,
							   task._function, str(task._function))
				logger.debug(traceback.format_exc())

				traceback.print_exc()

			logger.debug("PoolWorker <%s> called: %s%s", current_thread().ident, task._function.__name__,
						 str(task._argTuple))

			self._tasksQueue.task_done()

		logger.warning("PoolWorker <%s> STOPPED", current_thread().ident)
