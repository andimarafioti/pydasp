# coding: utf-8
from gui.presenters.generics.presenter import Presenter
from gui.views.addEffectsMenuView import AddEffectMenuView

__author__ = 'Andres'


class AddEffectMenuPresenter(Presenter):
	def _getViewInstance(self):
		return AddEffectMenuView(self)

	def onNotify(self, emitter, event, args):
		super(AddEffectMenuPresenter, self).onNotify(emitter, event, args)
		if emitter is self.model:
			if event is self.model.INITIALIZE:
				effects_names = [effect.name() for effect in self.model.effects]
				self.view.Initialize.emit(effects_names, self.model.pos)

	def crash(self):
		print "CRAHS"
