# coding: utf-8
from gui.presenters.generics.presenter import Presenter
from gui.views.effects.simpleEffectView import SimpleEffectView

__author__ = 'Andres'


class SimpleEffectPresenter(Presenter):
	def _getViewInstance(self):
		return SimpleEffectView(self)

	def onNotify(self, emitter, event, args):
		super(SimpleEffectPresenter, self).onNotify(emitter, event, args)
		if emitter is self.model:
			if event is emitter.INITIALIZE:
				view_list = [model.presenter.view for model in args[0]]
				self.view.Initialize.emit(view_list)
