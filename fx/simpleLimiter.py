# coding: utf-8
import numpy as np

from fx.simpleEffect import simpleEffect

__author__ = 'Andres'

""" Based on this article: http://bastibe.de/2012-11-02-real-time-signal-processing-in-python.html
	Code can be found here: https://github.com/bastibe/simple-cython-limiter/blob/master/limiter_python.py """


class Limiter(simpleEffect):
	NAME = "Limiter"

	def __init__(self, attack_coeff, release_coeff, delay, threshold, dtype=np.float32):
		self.delay_index = 0
		self.envelope = 0
		self.gain = 1
		self.delay = delay
		self.threshold = threshold
		self.delay_line = np.zeros(delay, dtype=dtype)
		self.release_coeff = release_coeff
		self.attack_coeff = attack_coeff

	def process(self, signal):
		for i in np.arange(len(signal)):
			self.delay_line[self.delay_index] = signal[i]
			self.delay_index = (self.delay_index + 1) % self.delay

			# calculate an envelope of the signal
			self.envelope *= self.release_coeff
			self.envelope = max(abs(signal[i]), self.envelope)

			# have self.gain go towards a desired limiter gain
			if self.envelope > self.threshold:
				target_gain = (1+self.threshold-self.envelope)
			else:
				target_gain = 1.0
			self.gain = (self.gain*self.attack_coeff + target_gain*(1-self.attack_coeff))

			# limit the delayed signal
			signal[i] = self.delay_line[self.delay_index] * self.gain

		return signal

	@classmethod
	def name(self):
		return self.NAME
