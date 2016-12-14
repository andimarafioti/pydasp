from gui.utils.observer import Subject

__author__ = 'Andres'


class Model(object):
	SHOW_VIEW = 0
	CLOSE_VIEW = 1

	def __init__(self, parent=None):
		self._parent = parent

		self.subject = Subject(self)

		self.presenter = self._getPresenterInstance()

	def parent(self):
		return self._parent

	def close(self):
		self.subject.notify(Model.CLOSE_VIEW)

	def closeModel(self):
		self.subject.clearObservers()

	def showView(self):
		self.subject.notify(Model.SHOW_VIEW)

	def _getPresenterInstance(self):
		raise NotImplementedError("Subclass responsibility")

	def onNotify(self, emitter, event, args):
		pass
