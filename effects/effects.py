# coding: utf-8
from effects.simpleLimiter import Limiter
from effects.simpleMaximizer import Maximizer

__author__ = 'Andres'


class Effects(object):
	@classmethod
	def availableEffects(cls):
		return [Limiter, Maximizer]