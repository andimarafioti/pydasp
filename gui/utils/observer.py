# -*- coding: utf-8 -*-
import logging
from _weakrefset import WeakSet
from threading import RLock

from utils.auxFunctions import stringFor

logger = logging.getLogger("[OBSERVER]")
logger.setLevel(logging.INFO)


class Subject:
	def __init__(self, parent):
		self.parent = parent
		self._observers_lock = RLock()
		self._observers = WeakSet()

	def addObserver(self, observer):
		with self._observers_lock:
			self._observers.add(observer)

		logger.debug("%s is being observed by %s", stringFor(self.parent), stringFor(observer))

	def removeObserver(self, observer):
		with self._observers_lock:
			try:
				self._observers.remove(observer)
			except KeyError:
				logger.error("Tried to remove observer %s twice from %s", stringFor(observer), stringFor(self.parent))

	def clearObservers(self):
		with self._observers_lock:
			self._observers.clear()

		logger.debug("%s observers were cleaned.", stringFor(self.parent))

	def notify(self, event, *args):
		with self._observers_lock:
			observers = list(self._observers)

		for obs in observers:
			logger.debug("%s is about to notify %s to %s", stringFor(self.parent), event, stringFor(obs))
			obs.onNotify(self.parent, event, args)
