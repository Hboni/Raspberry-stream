from PyQt4 import QtCore, QtGui

class ServerUI(QtGui.QWidget):

    def __init__(self):

        super(ServerUI, self).__init__()

        self.setupUI()

    def setupUI(self):

        self.main_layout = QtGui.QVBoxLayout()

        self.head_layout = QtGui.QHBoxLayout()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    w = ServerUI()
    w.show()

    sys.exit(app.exec_())