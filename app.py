from PyQt5 import QtWidgets
import res

if __name__ == "__main__":
    import sys

    from app_ui import Ui_MainWindow

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
