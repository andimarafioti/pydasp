# coding: utf-8
from gui.models.effects.simpleEffectModel import SimpleEffectModel

__author__ = 'Andres'


class ModelsVisitor(object):
    def visitSimpleEfectModel(self, simpleEffect):
        return SimpleEffectModel(simpleEffect)
