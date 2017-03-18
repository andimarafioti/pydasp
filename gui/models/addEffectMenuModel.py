# coding: utf-8
from fx.effectsContainer import EffectsContainer
from fx.simpleLimiter import Limiter
from fx.simpleMaximizer import Maximizer
from gui.models.generics.model import Model
from gui.presenters.addEffectMenuPresenter import AddEffectMenuPresenter

__author__ = 'Andres'


class AddEffectMenuModel(Model):
	INITIALIZE = 10
	EFFECTS = [Limiter, Maximizer]

	def __init__(self, pos, parent=None):
		super(AddEffectMenuModel, self).__init__(parent)
		self.pos = pos
		self.subject.notify(self.INITIALIZE)

	def _getPresenterInstance(self):
		return AddEffectMenuPresenter(self)

	def effectSelected(self, effect):
		print "Effect selected: "
		print effect
