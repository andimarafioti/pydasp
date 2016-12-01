# coding: utf-8
import numpy as np

from effects.simpleEffect import simpleEffect

__author__ = 'Andres'


class Maximizer(simpleEffect):
	def __init__(self, initial_value, average_length):
		self.averages = np.array([initial_value])
		self.average_length = average_length

	def process(self, audio):
		np.append(self.averages, audio.max())
		processed_audio = audio/self.averages[-self.average_length:].mean()
		return processed_audio
