import os

from lib.inputs import yesNo
from lib.files import traverse


# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
PREFIX = ''
SUFFIX = '.py'


def checkName(fileName):
    fileName = str(fileName)
    
    return fileName.startswith(PREFIX) and fileName.endswith(SUFFIX)
    

def removeFiles(path):
    assert os.path.isdir(path)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) if checkName(f)]

    print("---FILES---")
    for file in files:
        print(file)

    if yesNo("Delete files (y/n): "):
        for file in files:
            os.remove(os.path.join(path, file))
        print(f"Deleted {len(files)} files")

    input("Press ENTER to exit")


def main():
    assert os.path.isdir(ROOT)

    sourceDir = traverse(ROOT, "Choose source directory (press ENTER to choose CWD): ")

    removeFiles(sourceDir)


if __name__ == '__main__':
    main()
