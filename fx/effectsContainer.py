# coding: utf-8
from fx.simpleLimiter import Limiter
from fx.simpleMaximizer import Maximizer

__author__ = 'Andres'


class EffectsContainer(object):
	@classmethod
	def availableEffects(cls):
		return [Limiter, Maximizer]
