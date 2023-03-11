import os
import re

# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"


def main():
    global ROOT

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

    while True:
        dirs = [d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d))]

        if len(dirs) == 0:
            print("\nRunning script\n")
            removeDupes(os.path.join(ROOT))
            break

        # Choose directory
        for i in range(len(dirs)):
            print(f"{i+1}) {dirs[i]}")

        dir = getInput(dirs, "Choose directory (press ENTER to choose CWD): ")

        if not dir:
            print("Running script\n")
            removeDupes(os.path.join(ROOT))
            break

        print(f"You chose '{dirs[dir-1]}'\n")
        ROOT = os.path.join(ROOT, dirs[dir-1])


if __name__ == '__main__':
    main()
