# coding: utf-8
from fx.effectsContainer import EffectsContainer
from gui.models.generics.model import Model
from gui.presenters.addEffectMenuPresenter import AddEffectMenuPresenter

__author__ = 'Andres'


class AddEffectMenuModel(Model):
	INITIALIZE = 10

	def __init__(self, pos, parent=None):
		super(AddEffectMenuModel, self).__init__(parent)
		self.pos = pos
		self.effects = EffectsContainer.availableEffects()
		self.subject.notify(self.INITIALIZE)

	def _getPresenterInstance(self):
		return AddEffectMenuPresenter(self)
