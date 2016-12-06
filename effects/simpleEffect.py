# coding: utf-8
from gui.models.effects.simpleEffectModel import SimpleEffectModel

__author__ = 'Andres'


class simpleEffect(object):
	def process(self, signal):
		raise NotImplementedError("Subclass Responsibility")

	def getModel(self):
		return SimpleEffectModel(self)
