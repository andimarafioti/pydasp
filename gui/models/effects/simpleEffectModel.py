# coding: utf-8
from inspect import getargspec

from gui.models.generics.editableBoxModel import EditableBoxModel
from gui.models.generics.model import Model
from gui.presenters.effects.simpleEffectPresenter import SimpleEffectPresenter

__author__ = 'Andres'


class SimpleEffectModel(Model):
	INITIALIZE = 10

	def __init__(self, effect, parent=None):
		super(SimpleEffectModel, self).__init__(parent)
		self.editableBoxModels = []
		self._setAttributes(effect)
		self.subject.notify(self.INITIALIZE, self.editableBoxModels)

	def _setAttributes(self, effect):
		init_args, _, _, init_values = getargspec(effect.__init__)

		if len(init_args) - 1 != len(init_values):
			raise Exception("All values should have defaults in order to use a Default View")

		for i in range(len(init_args) - 1):
			self.editableBoxModels.append(EditableBoxModel(effect, init_args[i+1], init_values[i]))

	def _getPresenterInstance(self):
		return SimpleEffectPresenter(self)
