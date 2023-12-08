import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiArea, QMenuBar, QAction, QMdiSubWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

class FormMain(QMainWindow):
  
  def __init__(self):
    super().__init__()
    loadUi('form/form_main.ui', self)
    
    self.setWindowTitle('Aplikasi Perpustakaan Kelompok 12')
    self.setWindowIcon(QIcon('ICON/library_logo.png'))
    
    # membuat Mdi
    self.mdi = QMdiArea()
    self.setCentralWidget(self.mdi)
    
    # menu bar
    self.menu_bar = QMenuBar()
    
    administrator = self.menu_bar.addMenu('Administrator')
    data = self.menu_bar.addMenu('Data')
    transaksi = self.menu_bar.addMenu('Transaksi')
    user = self.menu_bar.addMenu('User')
    
    # sub menu
    dataUser = QAction(QIcon('ICON/account.png'), 'Registrasi Pengguna', self)
    administrator.addAction(dataUser)
    
    dataMember = QAction(QIcon('ICON/member.png'), 'Data Anggota', self)
    dataBook = QAction(QIcon('ICON/book.png'), 'Data Buku', self)
    data.addAction(dataMember)
    data.addAction(dataBook)
    
    dataLoan = QAction(QIcon('ICON/loan_transaction.png'), 'Transaksi Peminjaman', self)
    transaksi.addAction(dataLoan)
    
    logout = QAction(QIcon('ICON/logout.png'),'Logout', self)
    exitApp = QAction(QIcon('ICON/exit.png'),'Keluar', self)
    user.addAction(logout)
    user.addAction(exitApp)
    
    self.setMenuBar(self.menu_bar)
    
    # trigger
    logout.triggered.connect(self.logoutUser)
    exitApp.triggered.connect(self.keluar)
    
  # fungsi tampilan dialog konfirmasi
  def jendelaACC(self, pesan):
    msgbox = QMessageBox()
    msgbox.setWindowTitle('Aplikasi Perpustakaan')
    msgbox.setIconPixmap(QIcon('ICON/question.png').pixmap(40, 40))
    # msgbox.setIcon(QMessageBox.Question)
    msgbox.setWindowIcon(QIcon('ICON/library_logo.png'))
    msgbox.setText(pesan)
    msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
    return msgbox.exec()
  
  # fungsi untuk logout
  def logoutUser(self):
    dialog_acc = self.jendelaACC('Apakah anda yakin untuk logout ?')
    if dialog_acc == QMessageBox.Ok:
      pass
    
  # fungsi keluar dari aplikasi
  def keluar(self):
    dialog_acc = self.jendelaACC('Apakah anda yakin untuk keluar dari aplikasi ?')
    if dialog_acc == QMessageBox.Ok:
      pass
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = FormMain()
  window.show()
  sys.exit(app.exec_())