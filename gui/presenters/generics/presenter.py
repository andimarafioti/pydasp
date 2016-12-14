import threading

from PySide import shiboken
from PySide.QtCore import QObject, Signal
from PySide.QtGui import QApplication

from gui.models.generics.model import Model
from gui.utils.workerPool.workerPool import WorkerPool

__author__ = 'Andres'


class Presenter(QObject):
	WorkerPool = WorkerPool()
	WorkerPool.start()

	CreateView = Signal()

	def __init__(self, model):
		super(Presenter, self).__init__()

		self.moveToThread(QApplication.instance().thread())
		self.CreateView.connect(self._createView)

		self.model = model
		self.model.subject.addObserver(self)

		self.view = None

		self._tasks = []

		self._createViewEvent = threading.Event()
		self.CreateView.emit()
		self._createViewEvent.wait()

	def showView(self):
		self.view.Show.emit()

	def closeView(self):
		for task in self._tasks:
			Presenter.WorkerPool.cancelTask(task)

		if shiboken.isValid(self.view):
			self.view.Close.emit()

	def onViewClosed(self):
		pass

	def onNotify(self, emitter, event, args):
		if emitter is self.model:
			if event is Model.SHOW_VIEW:
				self.showView()
			elif event is Model.CLOSE_VIEW:
				self.closeView()

	def _createView(self):
		self.view = self._getViewInstance()
		self._createViewEvent.set()

	def _getViewInstance(self):
		raise NotImplementedError("Subclass responsibility")
