import os
import shutil
from datetime import datetime

from lib.inputs import yesNo
from lib.files import traverse, getFiles, checkPath


# Absolute path to the directory you want to search from
ROOT = r"C:\Users\[Users]\[directory]"
OVERWRITE = False
PREFIX = ''
SUFFIX = ''


def convertToDatetime(unixTime):
    date = datetime.utcfromtimestamp(unixTime).strftime("%Y-%m-%d %H:%M:%S")
    return (date[5:7], date[0:4])


def organiseFiles(source, destination):
    assert os.path.isdir(source)
    assert os.path.isdir(destination)
    files = getFiles(source, prefix=PREFIX, suffix=SUFFIX)

    print("---FILES---")
    for file in files:
        print(file)

    if yesNo("Organise files (y/n): "):
        for file in files:
            month, year = convertToDatetime(os.path.getmtime(file))
            if OVERWRITE:
                destinationPath = os.path.join(destination, year, month, file)
            else:
                destinationPath = os.path.join(destination, year, month)
            checkPath(destinationPath)
            shutil.move(os.path.join(source, file), destinationPath)
        print(f"Moved {len(files)} files")

    input("Press ENTER to exit")


def main():
    assert os.path.isdir(ROOT)

    sourceDir = traverse(ROOT, "Choose source directory (press ENTER to choose CWD): ")
    destinationDir = traverse(ROOT, "Choose destination directory (press ENTER to choose CWD): ")

    organiseFiles(sourceDir, destinationDir)


if __name__ == '__main__':
    main()
