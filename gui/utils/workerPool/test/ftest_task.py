from unittest import TestCase
from utils.workerPool.task import Task

__author__ = 'Jules'


class TestTask(TestCase):

    def testTasksCanRunFunctionsWithoutParameters(self):
        global functionWasRan
        functionWasRan = False

        def setFunctionWasRan():
            global functionWasRan
            functionWasRan = True

        task = Task(setFunctionWasRan)

        task.run()

        self.assertTrue(functionWasRan)

    def testTasksCanRunFunctionsWithParameters(self):
        global functionWasRan
        functionWasRan = False

        def setFunctionWasRanTo(value):
            global functionWasRan
            functionWasRan = value

        task = Task(setFunctionWasRanTo, (True,))

        task.run()

        self.assertTrue(functionWasRan)
