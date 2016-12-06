# coding: utf-8
from gui.presenters.presenter import Presenter
from gui.views.editableBoxView import EditableBoxView

__author__ = 'Andres'


class EditableBoxPresenter(Presenter):
	def _getViewInstance(self):
		return EditableBoxView(self)

	def onNotify(self, emitter, event, args):
		super(EditableBoxPresenter, self).onNotify(emitter, event, args)
		if emitter is self.model:
			if event is emitter.INITIALIZE:
				self.view.Initialize.emit(args[0], args[1])

	def finishedEditingValue(self, value):
		Presenter.WorkerPool.addHighPriorityTask(self.model.valueChanged, value)
