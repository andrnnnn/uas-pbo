from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class LoginForm(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle('login form')
    self.setGeometry(200, 200, 300, 150)
    
    self.usernameLabel = QLabel('username', self)
    self.usernameLabel.move(20, 20)
    self.usernameInput = QLineEdit(self)
    self.usernameInput.move(100, 20)
    
    self.passwordLabel = QLabel('password', self)
    self.passwordLabel.move(20, 50)
    self.passwordInput = QLineEdit(self)
    self.passwordInput.setEchoMode(QLineEdit.Password)
    self.passwordInput.move(100, 50)    
    
    self.showBtn = QPushButton('Show', self)
    self.showBtn.setCheckable(True)
    self.showBtn.move(230, 50)
    self.showBtn.clicked.connect(self.toggle)
    self.showBtn.clicked.connect(self.updateEye)
    
    self.passwordVisible = False
    
  def toggle(self):
    self.passwordVisible = not self.passwordVisible
    
    if self.passwordVisible:
      self.passwordInput.setEchoMode(QLineEdit.Normal)
    else:
      self.passwordInput.setEchoMode(QLineEdit.Password)
      
  def updateEye(self):
    if self.passwordVisible:
      self.showBtn.setText('Hide')
    else:
      self.showBtn.setText('Show')
      
app = QApplication([])
login = LoginForm()
login.show()
app.exec_()