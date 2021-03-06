# coding: utf-8
from gui.models.addEffectMenuModel import AddEffectMenuModel
from gui.models.generics.model import Model
from gui.presenters.mainPresenter import MainPresenter

__author__ = 'Andres'


class MainModel(Model):
	def __init__(self, parent=None):
		super(MainModel, self).__init__(parent)

	def _getPresenterInstance(self):
		return MainPresenter(self)

	def addEffectsClicked(self, pos):
		AddEffectMenuModel(pos, parent=self)
