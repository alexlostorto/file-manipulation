import os
import shutil

from lib.inputs import yesNo
from lib.traverse import traverseFiles


# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
PREFIX = '.trashed'
SUFFIX = '.jpeg'
USE_PREFIX = False
USE_SUFFIX = False


def checkName(fileName):
    fileName = str(fileName)
    if not USE_PREFIX and not USE_SUFFIX:
        return True
    elif USE_PREFIX and fileName.startswith(PREFIX) and USE_SUFFIX and fileName.endswith(SUFFIX):
        return True
    elif USE_PREFIX and fileName.startswith(PREFIX) and not USE_SUFFIX:
        return True
    elif USE_SUFFIX and fileName.endswith(SUFFIX) and not USE_PREFIX:
        return True
    else:
        return False


def main():
    def moveFiles(source, destination):
        assert os.path.isdir(source)
        assert os.path.isdir(destination)
        files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f)) if checkName(f)]

        print("---FILES---")
        for file in files:
            print(file)

        if yesNo("Move files (y/n): "):
            for file in files:
                shutil.move(os.path.join(source, file), os.path.join(destination, file))
            print(f"Moved {len(files)} files")

        input("Press ENTER to exit")

    assert os.path.isdir(ROOT)

    sourceDir = traverseFiles(ROOT, "Choose source directory (press ENTER to choose CWD): ")
    destinationDir = traverseFiles(ROOT, "Choose destination directory (press ENTER to choose CWD): ")

    moveFiles(sourceDir, destinationDir)


if __name__ == '__main__':
    main()
