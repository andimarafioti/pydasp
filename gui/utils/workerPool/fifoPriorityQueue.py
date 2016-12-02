# coding: utf-8
import heapq
from Queue import PriorityQueue

__author__ = 'Andres'


class FIFOPriorityQueue(PriorityQueue):
	def _init(self, maxsize):
		PriorityQueue._init(self, maxsize)
		self._counter = 0

	def _put(self, prioritized_item, heappush=heapq.heappush):
		priority = prioritized_item[0]
		data = prioritized_item[1]
		item = (priority, self._counter, data)
		self._counter += 1
		PriorityQueue._put(self, item, heappush)

	def _get(self, heappop=heapq.heappop):
		_, _, item = PriorityQueue._get(self, heappop)
		return item
