# coding: utf-8
from PySide.QtCore import QSize
from PySide.QtCore import Qt
from PySide.QtGui import QCursor
from PySide.QtGui import QGridLayout
from PySide.QtGui import QPixmap
from PySide.QtGui import QPushButton

from gui.views.generics.view import View

__author__ = 'Andres'


class MainView(View):
	def __init__(self, presenter, parent=None):
		super(MainView, self).__init__(presenter, parent=parent)
		self.setLayout(QGridLayout())

		addEffects = QPushButton(self)
		addEffects.isWordWrap = False
		addEffects.setFlat(True)
		addEffects.setCursor(Qt.PointingHandCursor)
		addEffects.setStyleSheet("QPushButton{outline:0; border-radius: 0px}")
		addEffects.setIcon(QPixmap("gui\\Add-Effects.jpg"))
		addEffects.setIconSize(QSize(300, 50))

		self.layout().addWidget(addEffects, 0, 0, 1, 1)
		self.setMinimumSize(QSize(640, 480))

		addEffects.clicked.connect(self.addEffectsClicked)

	def addEffectsClicked(self):
		self.presenter.addEffectsClicked(QCursor.pos())
