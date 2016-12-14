# -*- coding: utf-8 -*-
import StringIO
import hashlib
import socket
from math import floor

from PySide.QtCore import QRectF, Qt, QByteArray, QIODevice, QBuffer
from PySide.QtGui import QPixmap, QMessageBox, QPainter, QImage

from models.esttelaServices import Esttela


def doNothing(*args):
	pass


def stringFor(anObject):
	return "<{} {}>".format(anObject.__class__.__name__, str(id(anObject)))


def transformToLists(*args):
	params = []
	for arg in args:
		if arg is not None and not isinstance(arg, list):
			params.append([arg])
		else:
			params.append(arg)

	return params


def inv_duration(duracion_string):
	l = duracion_string.split(":")
	l.reverse()
	i = 0
	total = 0
	for num in l:
		num = int(num)
		total += num * (60 ** i)
		i += 1
	return total


def secondsToRemainingTime(seconds):
	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)

	if h > 0:
		time_left = '%d:%02d:%02d' % (h, m, s)
	elif m > 0:
		time_left = '%d:%02d' % (m, s)
	else:
		time_left = '%ds' % (s)

	return time_left


def numberToText(numero):
	if numero < 1000:
		return str(numero)
	elif numero < 1000000:
		return "{}k".format(numero / 1000)
	else:
		return "{}m".format(numero / 1000000)


def textToNumber(text):
	if "k" in text:
		return int(text[:-1] * 1000)
	elif "m" in text:
		return int(text[:-1] * 1000000)
	else:
		return int(text)


def segundosAHora(time):
	hor = (int(time / 3600))
	minu = int((time - (hor * 3600)) / 60)
	seg = time - ((hor * 3600) + (minu * 60))
	if seg < 10:
		seg = "0" + str(seg)
	if hor == 0:
		return str(minu) + ":" + str(trunc(seg))
	else:
		return str(hor) + ":" + str(minu) + ":" + str(trunc(seg))


def trunc(seg):
	a = str(seg).split(".")
	return a[0]


def getPixmap(raw_image_data):
	pixmap = QPixmap()
	pixmap.loadFromData(raw_image_data)
	return pixmap


def songsTotalLength(songs):
	total_length = 0
	for song in songs:
		total_length += song.length()
	return total_length


def segundosAHoras(segundos):
	m, s = divmod(segundos, 60)
	h, m = divmod(m, 60)
	return "%02d:%02d" % (h, m)


def hasNone(list_dict_or_var):
	if list_dict_or_var is None:
		return True
	if isinstance(list_dict_or_var, list):
		if None in list_dict_or_var:
			return True
	if isinstance(list_dict_or_var, dict):
		if None in list_dict_or_var.values():
			return True
	return False


def hashString(string):
	try:
		hashed_string = hashlib.sha256(string).hexdigest()
	except UnicodeEncodeError:
		string = string.encode('utf-8')
		hashed_string = hashlib.sha256(string).hexdigest()
	return hashed_string


def obtenerImagenDesdeBinario(dato):
	file_imagen = StringIO.StringIO(dato)
	image_data = file_imagen.getvalue()
	file_imagen.close()
	if image_data == "None":
		image_data = None
	return image_data


def obtenerImagenDesdePath(path):
	file_imagen = StringIO.StringIO(open(path, 'rb').read())
	image_data = file_imagen.getvalue()
	file_imagen.close()
	if image_data == "None":
		image_data = None
	return image_data


def showOkDialog(message, parent=None):
	dialog = QMessageBox(parent)
	dialog.setWindowTitle(" ")
	dialog.setText(message)
	dialog.setStandardButtons(QMessageBox.Ok)
	dialog.exec_()


def getCompositeImageFrom(songs):
	'''
	Potencialmente bloqueante, usar con LazyLoader
	'''
	# return models.esttela.ModelLauncher.mainModel.dataAccess.playlists.getImage(self)	<- deprecado por ahora

	albums = set(song.album() for song in songs)
	composition = [album for album in albums if Esttela.dataAccess.albums.hasImageFor(album)]

	if len(composition) == 0:
		return Esttela.dataAccess.playlists.defaultImage()
	elif len(composition) == 1:
		return composition[0].image()
	else:
		image = QImage(128, 128, QImage.Format_RGB32)
		painter = QPainter()
		painter.begin(image)
		painter.fillRect(0, 0, 128, 128, Qt.white)
		if len(composition) == 2:
			tapa = QImage()
			tapa.loadFromData(composition[0].image())
			tapa = tapa.scaled(128, 128, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(0, 0, 128, 63), tapa, QRectF(0, 32, 128, 63))
			tapa = QImage()
			tapa.loadFromData(composition[1].image())
			tapa = tapa.scaled(128, 128, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(0, 64, 128, 65), tapa, QRectF(0, 32, 128, 65))
		elif len(composition) == 3:
			tapa = QImage()
			tapa.loadFromData(composition[0].image())
			tapa = tapa.scaled(128, 128, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(0, 0, 128, 63), tapa, QRectF(0, 32, 128, 63))
			tapa = QImage()
			tapa.loadFromData(composition[1].image())
			tapa = tapa.scaled(64, 64, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(0, 65, 63, 63), tapa, QRectF(0, 0, 64, 64))
			tapa = QImage()
			tapa.loadFromData(composition[2].image())
			tapa = tapa.scaled(64, 64, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(65, 65, 63, 63), tapa, QRectF(0, 0, 64, 64))
		else:
			tapa = QImage()
			tapa.loadFromData(composition[0].image())
			tapa = tapa.scaled(64, 64, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(0, 0, 63, 63), tapa, QRectF(0, 0, 64, 64))
			tapa = QImage()
			tapa.loadFromData(composition[1].image())
			tapa = tapa.scaled(64, 64, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(65, 0, 63, 63), tapa, QRectF(0, 0, 64, 64))
			tapa = QImage()
			tapa.loadFromData(composition[2].image())
			tapa = tapa.scaled(64, 64, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(0, 65, 63, 63), tapa, QRectF(0, 0, 64, 64))
			tapa = QImage()
			tapa.loadFromData(composition[3].image())
			tapa = tapa.scaled(64, 64, mode=Qt.SmoothTransformation)
			painter.drawImage(QRectF(65, 65, 63, 63), tapa, QRectF(0, 0, 64, 64))
		painter.end()

		ba = QByteArray()
		buffer = QBuffer(ba)
		buffer.open(QIODevice.WriteOnly)
		image.save(buffer, "PNG")

	return ba


def obtenerTodasLasIps(): return socket.gethostbyname_ex(socket.gethostname())[2]
