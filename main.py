import sys
import requests
import json
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QTimer
import library


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(800, 800)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        country = input('Introduce el pais: ')
        self.get_openweather(country)

    def get_openweather(self, ciudad):
        URL = 'https://api.openweathermap.org/data/2.5/weather?q='
        KEY = 'bbc1a18c60774bea36411894174f12fe'

        api_url = URL + ciudad + '&APPID=' + KEY
        response = requests.get(api_url)

        try:
            ciudad_data = json.loads(response.text)
            # print(ciudad_data)
            description = ciudad_data['weather'][0]['description']
            print(description)
            icon = ciudad_data['weather'][0]['icon']
            print(icon)
            temp = ciudad_data['main']['temp']
            print(temp)
            country = ciudad_data['sys']['country']
            print(country)
            name = ciudad_data['name']
            print(name)

            self.dibuja_figura(description, icon, temp, country, name)
        except:
            print('No se encontro la ciudad')

    def dibuja_figura(self, description, icon, temp, country, name):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        if icon[0:2] == '01':
            print('clear sky')
            figura = library.Circulo(
                painter, 400, 400, 100, temp, country, name)
            figura.dibujar(Qt.GlobalColor.yellow)
        elif icon[0:2] == '02':
            print('few clouds')
            figura = library.Cuadrado(
                painter, 400, 400, 100, temp, country, name)
            figura.dibujar(Qt.GlobalColor.blue)
        elif icon[0:2] == '03':
            print('scattered clouds')
            figura = library.Rectangulo(
                painter, 400, 400, 100, 200, temp, country, name)
            figura.dibujar(Qt.GlobalColor.green)
        elif icon[0:2] == '04':
            print('broken clouds')
            figura = library.Triangulo(
                painter, 400, 400, 100, temp, country, name)
            figura.dibujar(Qt.GlobalColor.red)
        elif icon[0:2] == '09':
            print('shower rain')
            figura = library.Pentagono(
                painter, 400, 400, 100, temp, country, name)
            figura.dibujar(Qt.GlobalColor.black)

        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
