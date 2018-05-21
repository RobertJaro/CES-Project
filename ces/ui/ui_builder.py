import glob

from PyQt5.uic import compileUi
from os.path import basename

if __name__ == '__main__':
    for file in glob.glob("**/*.ui", recursive=True):
        compileUi(open(file, "r"), open(basename(file).replace(".ui", ".py"), "w"))
