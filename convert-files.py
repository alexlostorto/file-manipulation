import os

from lib.inputs import yesNo, getInput
from lib.files import traverse
from lib.convert import conversions


# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
PREFIX = ''
SUFFIX = '.mp4'


def convertFiles(path):
    assert os.path.isdir(path)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) if str(f).startswith(PREFIX) and str(f).endswith(SUFFIX)]
    
    # Choose conversion
    for i in range(len(conversions.keys())):
        print(f"{i+1}) {list(conversions.keys())[i]}")

    choice = getInput(conversions.keys(), "Choose file extension to convert to: ")
    extension = list(conversions.keys())[choice-1]
    converter = conversions[extension]

    print(f"You chose '{extension}'\n")

    print("---FILES---")
    for file in files:
        print(file)

    if yesNo("Compress files (y/n): "):
        count = 0
        for file in files:
            try:
                converter(path, file)
                count += 1
            except Exception as e:
                print(e)
        print(f"\nConverted {count} files\n")

    input("Press ENTER to exit")


def main():
    assert os.path.isdir(ROOT)

    sourceDir = traverse(ROOT, "Choose source directory (press ENTER to choose CWD): ")

    convertFiles(sourceDir)


if __name__ == '__main__':
    main()