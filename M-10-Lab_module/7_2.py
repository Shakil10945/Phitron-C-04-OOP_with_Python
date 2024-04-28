import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QColor
from PyQt5.QtCore import QTimer
import cv2
import datetime

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

        #load icon
        self.camera_icon = QIcon(cap_icon_path)
        self.rec_icon = QIcon(rec_icon_path)
        self.stop_icon = QIcon(stop_icon_path)

        #setup the window
        self.setWindowTitle("My Camera APP")
        self.setGeometry(500,200, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        #setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.get_time()  # Call get_time to initialize self.dt
        self.ui()

    def ui(self):
        """Contains all the ui things"""

        #layout
        grid = QGridLayout()
        self.setLayout(grid)

        #image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0,self.img_width, self.img_height)

        #capture button
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        self.capture_btn.setStyleSheet("border-radius: 30, border: 2px solid black; border-width: 3px")
        self.capture_btn.setFixedSize(60, 60)
        self.capture_btn.clicked.connect(self.save_image)

        #record button
        self.rec_btn = QPushButton(self)
        self.rec_btn.setIcon(self.rec_icon)
        self.rec_btn.setStyleSheet("border-radius: 30, border: 2px solid black; border-width: 3px")
        self.rec_btn.setFixedSize(60, 60)
        self.rec_btn.clicked.connect(self.record)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
        
        #add things to the layout
        grid.addWidget(self.capture_btn, 0, 0)
        grid.addWidget(self.image_label, 0, 1,2,3)
        grid.addWidget(self.rec_btn, 1,0)

        self.show()

    def update(self):
        """update frame"""
        _,self.frame = self.cap.read()

        if self.recording:  # Check if recording is in progress
            self.draw_red_circle()  # Draw red circle on the frame

        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width

        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_frame))
    
    def save_image(self):
        """save the image from camera"""
        print("he called me")
        self.get_time()  # Update self.dt
        cv2.imwrite(f"{self.dt}.jpg", self.frame)

    def record(self):
        """record video"""
        print('recording starts.........')
        self.recording = True  # Set recording flag to True

    def get_time(self):
        now = datetime.datetime.now()
        self.dt = now.strftime("%m-%d-%y, %H-%M-%S")
        print(self.dt)

    def draw_red_circle(self):
        """Draw a red circle on the frame"""
        # Calculate center and radius of the circle
        center = (self.img_width // 2, self.img_height // 2)
        radius = min(self.img_width, self.img_height) // 4

        # Draw the red circle on the frame
        cv2.circle(self.frame, center, radius, (0, 0, 255), -1)

#run
cap_icon_paths = 77
cap_icon_path = 'E:\Phitron-1\OOP & Python Programming\M-10-Lab_module\cam\capture.png'
rec_icon_path = 'E:\Phitron-1\OOP & Python Programming\M-10-Lab_module\cam/video.png'
stop_icon_path = 'E:\Phitron-1\OOP & Python Programming\M-10-Lab_module\cam/stop_video.png'

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())


