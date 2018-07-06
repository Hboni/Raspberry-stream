from PyQt4 import  QtCore, QtGui

class ClientUI(QtGui.QWidget):

    def __init__(self):

        super(ClientUI, self).__init__()

        self.main_layout = QtGui.QVBoxLayout(self)

        self.title_label = QtGui.QLabel("Raspberry-stream client")
        title_font = QtGui.QFont()
        title_font.setBold(True)
        title_font.setPointSize(20)
        self.title_label.setFont(title_font)
        self.main_layout.addWidget(self.title_label)

        self.connect_button = QtGui.QPushButton("Connect")
        self.main_layout.addWidget(self.connect_button)

        self.show()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    w = ClientUI()

    sys.exit(app.exec_())
