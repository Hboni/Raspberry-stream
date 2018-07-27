from PyQt4 import QtCore, QtGui

class ServerUI(QtGui.QWidget):

    def __init__(self):

        super(ServerUI, self).__init__()

        self.setupUI()

    def setupUI(self):

        self.main_layout = QtGui.QVBoxLayout(self)

        self.head_layout = QtGui.QHBoxLayout()
        self.head_label = QtGui.QLabel("Raspberry-stream : Server")
        self.head_layout.addWidget(self.head_label)

        self.main_layout.addLayout(self.head_layout)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    w = ServerUI()
    w.show()

    sys.exit(app.exec_())