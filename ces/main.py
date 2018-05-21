import sys

from qtpy import QtWidgets

from ces.app.app import CESApp


def main():
    # prepare application
    app = QtWidgets.QApplication(sys.argv)

    addExceptionHook()

    # start application
    ces = CESApp()
    ces.showMaximized()

    sys.exit(app.exec_())


def addExceptionHook():
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook


if __name__ == '__main__':
    main()
