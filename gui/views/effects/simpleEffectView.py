# coding: utf-8
from PySide.QtCore import Signal
from PySide.QtGui import QGridLayout

from gui.views.generics.view import View

__author__ = 'Andres'


class SimpleEffectView(View):
	Initialize = Signal(object)

	def __init__(self, presenter, parent=None):
		super(SimpleEffectView, self).__init__(presenter, parent=parent)

		self.setLayout(QGridLayout())

		self.Initialize.connect(self._initialize)

	def _initialize(self, views_list):
		row = -1
		for index, view in enumerate(views_list):
			column = index % 3

			if column == 0:
				row += 1

			self.layout().addWidget(view, row, column, 1, 1)
