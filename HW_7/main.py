from Classes import FileRenamer
from pathlib import Path

PREV_NAME_LETTERS_DIAP = (1, 3)
END_FILENAME = '_ok'
NUMS_COUNTER = 3
FILE_EXTENSION = '.sleem'
PATH = Path('Files')

file_renamer = FileRenamer(PREV_NAME_LETTERS_DIAP,
                           END_FILENAME,
                           NUMS_COUNTER,
                           FILE_EXTENSION,
                           PATH)


file_renamer.change()
