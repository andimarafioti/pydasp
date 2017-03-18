# coding: utf-8
from gui.presenters.generics.presenter import Presenter
from gui.views.addEffectsMenuView import AddEffectMenuView

__author__ = 'Andres'


class AddEffectMenuPresenter(Presenter):
	def _getViewInstance(self):
		return AddEffectMenuView(self, self.model.parent().presenter.view)

	def onNotify(self, emitter, event, args):
		super(AddEffectMenuPresenter, self).onNotify(emitter, event, args)
		if emitter is self.model:
			if event is self.model.INITIALIZE:
				effects_names_and_callback = [(effect.name(), self.callbackGenerator(effect)) for effect in self.model.EFFECTS]
				self.view.Initialize.emit(effects_names_and_callback, self.model.pos)

	def callbackGenerator(self, effect):
		def onEffectSelected():
			Presenter.WorkerPool.addHighPriorityTask(self.model.effectSelected, effect)
		return onEffectSelected

