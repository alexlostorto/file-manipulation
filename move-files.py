import os
import shutil

from lib.inputs import yesNo
from lib.files import traverse


# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
PREFIX = '.trashed'
SUFFIX = '.jpeg'


def moveFiles(source, destination):
    assert os.path.isdir(source)
    assert os.path.isdir(destination)
    files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f)) if str(f).startswith(PREFIX) and str(f).endswith(SUFFIX)]

    print("---FILES---")
    for file in files:
        print(file)

    if yesNo("Move files (y/n): "):
        for file in files:
            shutil.move(os.path.join(source, file), os.path.join(destination, file))
        print(f"Moved {len(files)} files")

    input("Press ENTER to exit")


def main():
    assert os.path.isdir(ROOT)

    sourceDir = traverse(ROOT, "Choose source directory (press ENTER to choose CWD): ")
    destinationDir = traverse(ROOT, "Choose destination directory (press ENTER to choose CWD): ")

    moveFiles(sourceDir, destinationDir)


if __name__ == '__main__':
    main()
