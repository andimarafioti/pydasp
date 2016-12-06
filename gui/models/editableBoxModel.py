# coding: utf-8
from gui.models.model import Model
from gui.presenters.editableBoxPresenter import EditableBoxPresenter

__author__ = 'Andres'


class EditableBoxModel(Model):
	INITIALIZE = 10

	def __init__(self, effect,  name, value, parent=None):
		super(EditableBoxModel, self).__init__(parent)
		self.effect = effect
		self.name = name
		self.value = value
		self.initialize()

	def initialize(self):
		self.subject.notify(self.INITIALIZE, self.name, self.value)

	def _getPresenterInstance(self):
		return EditableBoxPresenter(self)

	def valueChanged(self, value):
		setattr(self.effect, self.name, float(value))
