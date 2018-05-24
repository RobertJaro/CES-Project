import glob
from os import path

from PyQt5.uic import compileUi

if __name__ == '__main__':
    for file in glob.glob("**/*.ui", recursive=True):
        compileUi(open(file, "r"), open(path.basename(file).replace(".ui", ".py"), "w"))
