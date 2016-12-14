# coding: utf-8
from gui.presenters.generics.presenter import Presenter
from gui.views.mainView import MainView

__author__ = 'Andres'


class MainPresenter(Presenter):
	def __init__(self, model):
		super(MainPresenter, self).__init__(model)

	def _getViewInstance(self):
		return MainView(self)

	def addEffectsClicked(self, position):
		Presenter.WorkerPool.addHighPriorityTask(self.model.addEffectsClicked, position)