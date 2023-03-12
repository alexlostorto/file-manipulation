import os
import shutil

# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
PREFIX = '.trashed'
SUFFIX = '.jpeg'
USE_PREFIX = False
USE_SUFFIX = False


def main():
    def getInput(array, question):
        userInput = input(question)
        print()

        while True:
            # Check input is acceptable
            if userInput == '':
                return False
            elif not userInput.isdigit() or int(userInput) < 1 or int(userInput) > len(array):
                print(f"Input has to be a number 1-{len(array)}")
                userInput = input(question)
                continue
            else:
                # Chooses file
                userInput = int(userInput)
                return userInput

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

    def yesNo(question):
        userInput = input(question)
        print()

        while True:
            # Check input is acceptable
            if userInput == '':
                print(f"Don't leave me empty!")
            elif userInput.lower() in ['y', 'ye', 'yes', 'yeah']:
                return True
            elif userInput.lower() in ['n', 'no', 'nop', 'nope']:
                return False

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

    def traverseFiles(root, question):
        while True:
            dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]

            if len(dirs) == 0:
                return root

            # Choose directory
            for i in range(len(dirs)):
                print(f"{i+1}) {dirs[i]}")

            dir = getInput(dirs, question)

            if not dir:
                return root

            print(f"You chose '{dirs[dir-1]}'\n")
            root = os.path.join(root, dirs[dir-1])

    assert os.path.isdir(ROOT)

    sourceDir = traverseFiles(ROOT, "Choose source directory (press ENTER to choose CWD): ")
    destinationDir = traverseFiles(ROOT, "Choose destination directory (press ENTER to choose CWD): ")

    moveFiles(sourceDir, destinationDir)


if __name__ == '__main__':
    main()
