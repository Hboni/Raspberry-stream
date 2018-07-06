from PyQt4 import  QtCore, QtGui

class ClientUI(QtGui.QWidget):

    def __init__(self):

        super(ClientUI, self).__init__()

        self.main_layout = QtGui.QVBoxLayout(self)

        self.title_layout = QtGui.QHBoxLayout()
        self.title_label = QtGui.QLabel("Raspberry-stream client")
        title_font = QtGui.QFont()
        title_font.setBold(True)
        title_font.setPointSize(20)
        self.title_label.setFont(title_font)
        self.title_layout.addWidget(self.title_label)

        self.main_layout.addLayout(self.title_layout)

        # Parameters fillable content
        self.param_layout = QtGui.QVBoxLayout()

        self.address_layout = QtGui.QHBoxLayout()
        self.address_label = QtGui.QLabel("Address : ")
        self.address_lineedit = QtGui.QLineEdit()
        self.address_layout.addWidget(self.address_label)
        self.address_layout.addWidget(self.address_lineedit)

        self.port_layout = QtGui.QHBoxLayout()
        self.port_label = QtGui.QLabel("Port : ")
        self.port_lineedit = QtGui.QLineEdit()
        self.port_layout.addWidget(self.port_label)
        self.port_layout.addWidget(self.port_lineedit)

        self.param_layout.addLayout(self.address_layout)
        self.param_layout.addLayout(self.port_layout)

        self.main_layout.addLayout(self.param_layout)

        self.connect_button = QtGui.QPushButton("Connect")
        self.main_layout.addWidget(self.connect_button)

        self.show()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    w = ClientUI()

    sys.exit(app.exec_())
