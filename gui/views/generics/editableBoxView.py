# coding: utf-8
from PySide.QtCore import Signal
from PySide.QtGui import QLabel
from PySide.QtGui import QLineEdit
from PySide.QtGui import QVBoxLayout

from gui.views.generics.view import View

__author__ = 'Andres'


class EditableBoxView(View):
	Initialize = Signal(object, object)

	def __init__(self, presenter, parent=None):
		super(EditableBoxView, self).__init__(presenter, parent)
		self.nameLabel = QLabel(self)
		self.valueEdit = QLineEdit(self)

		self.setLayout(QVBoxLayout())
		self.layout().addWidget(self.nameLabel)
		self.layout().addWidget(self.valueEdit)

		self.Initialize.connect(self._initialize)
		self.valueEdit.editingFinished.connect(self._onFinishedEditingValue)

	def _initialize(self, name, value):
		self.nameLabel.setText(name)
		self.valueEdit.setText(str(value))

	def _onFinishedEditingValue(self):
		self.presenter.finishedEditingValue(self.valueEdit.text())
