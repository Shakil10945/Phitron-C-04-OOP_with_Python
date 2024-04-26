"""My Camera application
Author: Shakil Khan
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2

class Window(QWidget):
    """Main app window"""
    def __init__(self):
        super().__init__()

        #variables for app window
        self.window_width = 640
        self.window_height = 400

        #image variables 
        self.img_width = 640
        self.img_height = 400

        #setup the window
        self.setWindowTitle("My Camera APP")
        self.setGeometry(500,200, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        self.ui()

    def ui(self):
        """Contains all the ui things"""

        #image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0,self.img_width, self.img_height)
        
        self.show()

    def update(self):
        """update frame"""
        pass
    
    def save_image(self):
        """save the image from camera"""
        pass

    def record(self):
        """record video"""
        pass


#run
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
