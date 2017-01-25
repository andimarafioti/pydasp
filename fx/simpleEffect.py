# coding: utf-8

__author__ = 'Andres'


class simpleEffect(object):
	def process(self, signal):
		raise NotImplementedError("Subclass Responsibility")

	@classmethod
	def name(self):
		raise NotImplementedError("Subclass Responsibility")

	def visitModel(self, visitor):  # This visitor avoids the effects backend from importing GUI stuff
		return visitor.visitSimpleEffectModel(self)
