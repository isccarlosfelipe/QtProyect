import math
from multimethod import multimethod
from PyQt6 import QtGui
from PyQt6.QtCore import Qt


class Geometica:

    def __init__(self, painter: QtGui.QPainter, x, y):
        self.x = x
        self.y = y
        self.painter = painter
        print(
            f"Se ha creado una figura geometrica en la posicion ({self.x},{self.y})")

    def moverse(self):
        self.x += 10
        self.y += 10
        print(
            f"Se ha movido la figura geometrica a la posicion ({self.x},{self.y})")


class Circulo(Geometica):

    def __init__(self, painter: QtGui.QPainter, x, y, radio, temp, country, name):
        super().__init__(painter, x, y)
        self.radio = radio
        self.temp = temp
        self.country = country
        self.name = name

    @multimethod
    def dibujar(self):
        self.painter.drawEllipse(
            self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)

    @multimethod
    def dibujar(self, color: Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawEllipse(
            self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)
        self.painter.drawText(self.x - 10, self.y + 5, self.name)


class Cuadrado(Geometica):

    def __init__(self, painter: QtGui.QPainter, x, y, lado, temp, country, name):
        super().__init__(painter, x, y)
        self.lado = lado
        self.temp = temp
        self.country = country
        self.name = name

    @multimethod
    def dibujar(self):
        self.painter.drawRect(self.x, self.y, self.lado, self.lado)

    @multimethod
    def dibujar(self, color: Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawRect(self.x, self.y, self.lado, self.lado)
        self.painter.drawText(self.x - 10, self.y + 5, self.name)


class Rectangulo(Geometica):

    def __init__(self, painter: QtGui.QPainter, x, y, base, altura, temp, country, name):
        super().__init__(painter, x, y)
        self.base = base
        self.altura = altura
        self.temp = temp
        self.country = country
        self.name = name

    @multimethod
    def dibujar(self):
        self.painter.drawRect(self.x, self.y, self.base, self.altura)

    @multimethod
    def dibujar(self, color: Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawRect(self.x, self.y, self.base, self.altura)
        self.painter.drawText(self.x - 10, self.y + 5, self.name)


class Triangulo(Geometica):

    def __init__(self, painter: QtGui.QPainter, x, y, lado, temp, country, name):
        super().__init__(painter, x, y)
        self.lado = lado
        self.temp = temp
        self.country = country
        self.name = name

    @multimethod
    def dibujar(self, color: Qt.GlobalColor):
        self.painter.setBrush(color)
        path = QtGui.QPainterPath()
        path.moveTo(self.x, self.y)  # Punto superior
        path.lineTo(self.x + self.lado, self.y)  # Punto derecho
        path.lineTo(self.x + self.lado / 2,
                    self.y - (self.lado * (3 ** 0.5) / 2))  # Punto inferior
        self.painter.drawText(self.x - 10, self.y + 5, self.name)
        path.closeSubpath()
        self.painter.drawPath(path)


class Pentagono(Geometica):

    def __init__(self, painter: QtGui.QPainter, x, y, lado, temp, country, name):
        super().__init__(painter, x, y)
        self.lado = lado
        self.temp = temp
        self.country = country
        self.name = name

    @multimethod
    def dibujar(self, color: Qt.GlobalColor):
        self.painter.setBrush(color)
        path = QtGui.QPainterPath()
        angle = 72  # 360 grados / 5 lados = 72 grados
        for i in range(5):
            x = self.x + self.lado * math.cos(math.radians(angle * i))
            y = self.y + self.lado * math.sin(math.radians(angle * i))
            if i == 0:
                path.moveTo(x, y)
            else:
                path.lineTo(x, y)
        self.painter.drawText(self.x - 10, self.y + 5, self.name)
        path.closeSubpath()
        self.painter.drawPath(path)
