# coding: utf-8
from PySide.QtCore import Signal
from PySide.QtCore import Qt
from PySide.QtGui import QMenu

__author__ = 'Andres'


class EsttelaMenu(QMenu):
	def __init__(self, parent=None, item_color="rgb(51, 51, 51)", background_color="rgb(245, 245, 245)"):
		super(EsttelaMenu, self).__init__(parent)

		self.item_color = item_color
		self.background_color = background_color

		style_string = "QMenu {{ \
							font: 'Roboto Light'; \
							font-size: 14px; \
							padding: 0px, 0px, 0px, 0px; \
						    background-color: {}; \
						}} \
						 \
					  	QMenu::icon {{ \
							position: absolute; \
							right: 1px; \
							left: 9px; \
						}} \
						QMenu::item {{ \
							color: {}; \
							padding-top: 3px; \
							padding-bottom: 3px; \
							padding-right: 27px; \
							padding-left: 27px; \
						}} \
						 \
						QMenu::separator {{ \
						    height: 1px; \
						    background: rgb(230, 230, 230); \
						    margin-left: 2px; \
						    margin-right: 2px; \
						}} \
						QMenu::item:selected {{ \
						    background-color: rgb(37, 191, 161); \
							color: rgb(246, 246, 246); \
						}}".format(self.background_color, self.item_color)

		self.setAttribute(Qt.WA_StyledBackground)
		self.setStyleSheet(style_string)


class AddEffectMenuView(EsttelaMenu):
	Initialize = Signal(object, object)

	def __init__(self, presenter, parent=None):
		super(AddEffectMenuView, self).__init__(parent)
		self.presenter = presenter
		self.setAttribute(Qt.WA_StyledBackground)

		self.Initialize.connect(self._initialize)

	def _initialize(self, effects_names_list, pos):
		for effect_name in effects_names_list:
			self.addAction(effect_name, self.presenter.crash)
		self.move(pos)
		self.show()
