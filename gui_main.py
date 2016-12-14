# coding: utf-8
import locale
import sys
from PySide.QtGui import QApplication

from audioProcessor import AudioProcessor
from gui.models.mainModel import MainModel

__author__ = 'Andres'

qt_app = QApplication(sys.argv)

locale.setlocale(locale.LC_ALL, "spanish")
# qt_app.setEffectEnabled(Qt.UI_AnimateCombo, False)
qt_app.setQuitOnLastWindowClosed(False)

# maximizer = Maximizer()
ap = AudioProcessor(1024, 2, 44100, [])
ap.start()

model = MainModel()
model.showView()

qt_app.exec_()
sys.exit(0)
