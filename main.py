# coding: utf-8
import time

from audioProcessor import AudioProcessor
from effects.simpleLimiter import Limiter
from effects.simpleMaximizer import Maximizer

__author__ = 'Andres'

delay = 40  # samples
signal_length = 1  # second
release_coeff = 0.9999  # release time factor
attack_coeff = 0.9  # attack time factor
threshold = 0.4  # absolute gain

limiter = Limiter(attack_coeff=attack_coeff, release_coeff=release_coeff, delay=delay, threshold=threshold)
maximizer = Maximizer(initial_value=0.5, average_length=20)

ap = AudioProcessor(1024, 2, 44100, [limiter, maximizer])
ap.start()

time.sleep(5)
ap.setEffects([limiter])
time.sleep(5)
ap.setEffects([maximizer])
time.sleep(5)
ap.setEffects([limiter, maximizer])

while True:
	time.sleep(1)
