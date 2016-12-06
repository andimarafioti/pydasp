# coding: utf-8
import locale
import sys
from PySide.QtGui import QApplication

from audioProcessor import AudioProcessor
from effects.simpleMaximizer import Maximizer

__author__ = 'Andres'

qt_app = QApplication(sys.argv)

locale.setlocale(locale.LC_ALL, "spanish")
# qt_app.setEffectEnabled(Qt.UI_AnimateCombo, False)
qt_app.setQuitOnLastWindowClosed(False)

maximizer = Maximizer()

ap = AudioProcessor(1024, 2, 44100, [maximizer])
ap.start()

model = maximizer.getModel()
model.showView()

qt_app.exec_()
sys.exit(0)
