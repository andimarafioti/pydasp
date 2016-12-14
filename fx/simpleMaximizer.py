# coding: utf-8
import numpy as np

from fx.simpleEffect import simpleEffect

__author__ = 'Andres'


class Maximizer(simpleEffect):
	NAME = "Maximizer"

	def __init__(self, initial_value=0.5, average_length=20):
		self.initial_value = initial_value
		self.averages = np.array([initial_value])
		self.average_length = average_length

	def process(self, audio):
		self.averages = np.append(self.averages, audio.max())
		processed_audio = audio/self.averages[-self.average_length:].mean()
		return processed_audio

	@classmethod
	def name(self):
		return self.NAME
