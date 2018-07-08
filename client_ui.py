from PyQt4 import  QtCore, QtGui
from client import Client

class ClientUI(QtGui.QWidget):

    def __init__(self):

        super(ClientUI, self).__init__()

        self.setupUI()
        self.setupEvents()

    def setupUI(self):

        self.main_layout = QtGui.QVBoxLayout(self)

        self.title_layout = QtGui.QHBoxLayout()
        self.raspberry_picture = QtGui.QPixmap('pictures/raspberry.png')
        self.raspberry_picture = self.raspberry_picture.scaledToHeight(60)
        self.raspberry_label = QtGui.QLabel()
        self.raspberry_label.setPixmap(self.raspberry_picture)
        self.title_layout.addWidget(self.raspberry_label)

        self.title_label = QtGui.QLabel("Raspberry-stream client")
        title_font = QtGui.QFont()
        title_font.setBold(True)
        title_font.setPointSize(20)
        self.title_label.setFont(title_font)
        self.title_layout.addWidget(self.title_label)

        self.state_box = QtGui.QGroupBox()
        self.state_layout = QtGui.QHBoxLayout()
        self.state_label = QtGui.QLabel("Not connected")
        self.state_layout.addWidget(self.state_label)
        self.state_box.setLayout(self.state_layout)
        self.title_layout.addWidget(self.state_box)

        self.main_layout.addLayout(self.title_layout)

        # Parameters fillable content
        self.param_box = QtGui.QGroupBox("Parameters")
        self.param_layout = QtGui.QGridLayout()

        self.address_layout = QtGui.QHBoxLayout()
        self.address_label = QtGui.QLabel("Address : ")
        self.address_lineedit = QtGui.QLineEdit()
        self.param_layout.addWidget(self.address_label, 0, 0)
        self.param_layout.addWidget(self.address_lineedit, 0, 1)

        self.port_layout = QtGui.QHBoxLayout()
        self.port_label = QtGui.QLabel("Port : ")
        self.port_lineedit = QtGui.QLineEdit()
        self.param_layout.addWidget(self.port_label, 1, 0)
        self.param_layout.addWidget(self.port_lineedit, 1, 1)

        self.param_box.setLayout(self.param_layout)
        self.main_layout.addWidget(self.param_box)

        self.input_box = QtGui.QGroupBox("Inputs")
        self.input_layout = QtGui.QHBoxLayout()
        self.input_link_label = QtGui.QLabel("Stream address : ")
        self.input_layout.addWidget(self.input_link_label)
        self.input_link_lineedit = QtGui.QLineEdit()
        self.input_layout.addWidget(self.input_link_lineedit)
        self.input_box.setLayout(self.input_layout)
        self.main_layout.addWidget(self.input_box)

        self.button_layout = QtGui.QHBoxLayout()
        self.connect_button = QtGui.QPushButton("Connect")
        self.button_layout.addWidget(self.connect_button)
        self.send_button = QtGui.QPushButton("Send")
        self.button_layout.addWidget(self.send_button)
        self.cancel_button = QtGui.QPushButton("Cancel")
        self.button_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(self.button_layout)

    def setupEvents(self):
        self.connect_button.clicked.connect(self.connect_client)
        self.cancel_button.clicked.connect(self.close)


    def connect_client(self):
        print('connect')
        if self.connect_button.text() == 'Connect':
            param = self.check_param()
            print('param : ', param)
            if param:
                address = self.address_lineedit.text()
                port = self.port_lineedit.text()
                try:
                    self.client = Client(port, address)
                    self.client.connect()
                    self.state_label.setText('Connected')
                    self.connect_button.setText('Disconnect')
                    self._print_comment('')
                except:
                    self._print_comment("Error connecting")
                    pass

        elif self.connect_button.text() == 'Disconnect':
            self.client.send_message('fin')
            self.state_label.setText('Not connected')
            self.connect_button.setText('Connect')

    def _print_comment(self, message):
        self.comment_label.setText(message)

    def check_param(self):

        address = self.address_lineedit.text().split('.')
        if address != ['localhost']:
            if len(address) != 4:
                self._print_comment("Address parameter incorrect.")
                return 0

            for add in address:
                if not add.isnumeric():
                    self._print_comment("Address parameter incorrect.")
                    return 0

        if not self.port_lineedit.text().isnumeric():
            self._print_comment("Port parameter incorrect.")
            return 0

        return 1

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    w = ClientUI()
    w.show()

    sys.exit(app.exec_())