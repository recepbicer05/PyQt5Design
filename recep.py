import serial                   # PySerial Kütüphanesi, seri portu kulllanabilmek için
import serial.tools.list_ports  # Bağlı portların tespiti için
from time import *              # Zamanla ilgili kütüphane
import sys                      # Sistem komutlarının çalıştırılabilmesi için

from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from drecep import *



app = QApplication([])
MainWindow = QtWidgets.QMainWindow()
ui = Ui_ServoMotorController() # class ismi
ui.setupUi(MainWindow)
MainWindow.show()



def port_ac():
    port = str(ui.port.currentText())

    baud = str(ui.baudrate.currentText())

    global ser

    try:

        ser = serial.Serial(port, baudrate=baud, timeout=0)

        if ser.is_open:
            ui.statusbar.showMessage(" " * 1 + " Port açıldı...", 1500)

            global timer1
            timer1 = QtCore.QTimer()




    except:

        ui.statusbar.showMessage(" " * 1 + " Port açılamadı !!! Lütfen sensörün bağlı olduğu portu seçiniz !!!", 1500)


def port_kapat():
    try:

        global ser

        # port = str(ui.port.currentText())
        # baud = str(ui.baudrate.currentText())
        # ser = serial.Serial(port, baudrate=baud, timeout=0)

        timer1.stop()

        if ser.is_open:
            ser.close()

            print("Port kapatıldı...")

            # ui.statusbar.showMessage(" "*1 + " Port kapatıldı...", 1500)


    except:

        ui.statusbar.showMessage(" " * 1 + "Açık port bulunamadı...", 1500)







ui.openport.clicked.connect(port_ac)
ui.pushButton_2.clicked.connect(port_kapat)
sys.exit(app.exec_())


