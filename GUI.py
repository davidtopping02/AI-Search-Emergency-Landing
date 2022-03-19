from emergencyLanding import *
from apiInterfaces import *
from aviationDataStructures import *
from searchDataStructures import *
from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
import sys
import io
import folium

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.m = None
        #setting up window size/title
        self.setWindowTitle('Plane Select')
        self.window_width, self.window_height = 400, 300
        self.setFixedSize(400,300)
        self.setMinimumSize(self.window_width, self.window_height)

        #setting icon
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        #global style sheet 
        self.setStyleSheet("font: 14pt Arial; ")

        #setting the background to a gradient (taken from https://wiki.python.org/moin/PyQt/Windows%20with%20gradient%20backgrounds)
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor(0, 255, 255))
        gradient.setColorAt(1.0, QColor(255, 255, 255))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        #adding label
        self.l1 = QLabel("Enter the flight number below", self)
        #self.l1.setFont(QFont('Times', 10))
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.resize(280,40)
        self.l1.move(60,20)

        #adding textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(60,100)
        self.textbox.setAlignment(QtCore.Qt.AlignCenter)
        self.textbox.resize(280,40)

        #adding button
        self.button = QPushButton("Search", self)
        self.button.resize(140,40)
        self.button.move(120,180)

        self.button.clicked.connect(self.button_pressed)

    def button_pressed(self):

            if self.textbox.text() is not None:
                coords = problem_search(self.textbox.text())

            if self.m is None:
                self.m = mapApp(coords)
                self.m.show()

            else:
                print("error with flight num")


class mapApp(QWidget):
    def __init__(self, coords=None):
        super().__init__()
        self.setWindowTitle('Map View')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        aircraft_coords = (coords[0][0], coords[0][1])
        airport_coords = (coords[1][0], coords[1][1])
        coordinate = aircraft_coords
        lineCoords = [aircraft_coords, airport_coords]

        m = folium.Map(
            title='test',
            zoom_start=10,
            location=coordinate
        )

        aircraft = folium.Marker(
            location=aircraft_coords,
            icon=folium.Icon(color='lightgray', icon='plane', prefix='fa'),
        ).add_to(m)

        airport = folium.Marker(
            location=airport_coords,
            icon=folium.Icon(color='blue', icon='house', prefix='fa'),
        ).add_to(m)

        line = folium.PolyLine(
            locations=lineCoords,
            weight=2,
            color='black',
        ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

def runGUI():

    # if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MainPage()
    myApp.show()

    sys.exit(app.exec_())

runGUI()