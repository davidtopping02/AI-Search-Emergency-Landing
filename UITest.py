import sys
import io
import folium #pip install folium

#install PyQt5 and PyQtWebEngine
from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore
from PyQt5.QtGui import *

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m = None
        #setting up window size/title
        self.setWindowTitle('Plane Select')
        self.window_width, self.window_height = 400, 300
        self.setMinimumSize(self.window_width, self.window_height)

        #global style sheet (sorry for comic sans)
        self.setStyleSheet("font: 14pt Comic Sans MS")

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
        self.button = QPushButton("Search",self)
        self.button.resize(140,40)
        self.button.move(120,180)
        self.button.clicked.connect(self.show_map)

    def show_map(self,checked):
        if self.m is None:
            self.m = mapApp()
        self.m.show()


class mapApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Map View')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (0,0)
        aircraft_coords = (0,0)
        airport_coords = (1,1)
        lineCoords = [aircraft_coords,airport_coords]
        
        m = folium.Map(
            title = 'test',
            zoom_start=10,
            location = coordinate
        )

        aircraft = folium.Marker(
            location = aircraft_coords,
            icon = folium.Icon(color= 'lightgray', icon='plane', prefix='fa'),
        ).add_to(m)

        airport = folium.Marker(
            location = airport_coords,
            icon = folium.Icon(color= 'blue', icon='house', prefix='fa'),
        ).add_to(m)

        line = folium.PolyLine(
            locations=lineCoords,
            weight = 2,
            color = 'black',
        ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MainPage()
    myApp.show()

    sys.exit(app.exec_())