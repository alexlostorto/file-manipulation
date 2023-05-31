import os

from lib.inputs import yesNo
from lib.files import traverse


# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
PREFIX = 'test'
SUFFIX = '.py'
USE_PREFIX = True
USE_SUFFIX = True


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
