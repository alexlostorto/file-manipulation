import os
import re

from lib.inputs import yesNo
from lib.files import traverse


# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"


def main():
    global ROOT

    def removeDupes(path):
        assert os.path.isdir(ROOT)

        files = [f for f in os.listdir(ROOT) if os.path.isfile(os.path.join(path, f))]

        dupFiles = []
        for file in files:
            position = re.search('\(\d+\).\w+', file)
            fileNameCut = re.sub('\(\d+\)', '', file)
            if position is not None and fileNameCut in files:
                dupFiles.append(file)

        if len(dupFiles) == 0:
            print("No duplicate files detected\n")
            input("Press ENTER to exit")
            return

        print("---FILES---")
        for file in dupFiles:
            print(file)

        if yesNo("Delete files (y/n): "):
            for file in dupFiles:
                os.remove(os.path.join(ROOT, file))
            print(f"Deleted {len(dupFiles)} files")

        input("Press ENTER to exit")

    assert os.path.isdir(ROOT)

    sourceDir = traverse(ROOT, "Choose source directory (press ENTER to choose CWD): ")

    removeDupes(sourceDir)


if __name__ == '__main__':
    main()
