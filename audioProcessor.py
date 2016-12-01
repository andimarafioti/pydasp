# coding: utf-8
import threading

import numpy as np

__author__ = 'Andres'

import pyaudio
import time


class AudioProcessor(object):
	def __init__(self, frames_per_buffer, channels, rate, effects):
		self.p = pyaudio.PyAudio()
		self._effects = effects
		self.stream = self.p.open(format=pyaudio.paFloat32,
						channels=channels,
						rate=rate,
						frames_per_buffer=frames_per_buffer,
						input=True,
						output=True,
						stream_callback=self.callback)

	def callback(self, in_data, frame_count, time_info, status):
		data = np.fromstring(in_data, dtype=np.float32)
		# len(data)/frame_count = channels
		for effect in self._effects:
			effect.process(data)
		return data.tostring(), pyaudio.paContinue

	def setEffects(self, effects):
		self._effects = effects

	def start(self):
		thread = threading.Thread(target=self._start)
		thread.daemon = True
		thread.start()

	def _start(self):
		self.stream.start_stream()
		while self.stream.is_active():
			time.sleep(0.1)

	def stop(self):
		self.stream.stop_stream()

	def exit(self):
		self.stream.close()
		self.p.terminate()
