import sys
 
from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
import sys
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # define the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    Info
    info = Info('Your count')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    #Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # execute all
    window.adjustFixedSize()
    window.show()
    app.exec()