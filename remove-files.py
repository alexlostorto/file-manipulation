import os

# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
PREFIX = 'test'
SUFFIX = '.py'
USE_PREFIX = True
USE_SUFFIX = True


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

    def removeFiles(path):
        assert os.path.isdir(ROOT)
        files = [f for f in os.listdir(ROOT) if os.path.isfile(os.path.join(path, f)) if checkName(f)]

        print("---FILES---")
        for file in files:
            print(file)

        if yesNo("Delete files (y/n): "):
            for file in files:
                os.remove(os.path.join(ROOT, file))
            print(f"Deleted {len(files)} files")

        input("Press ENTER to exit")

    assert os.path.isdir(ROOT)

    while True:
        dirs = [d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d))]

        if len(dirs) == 0:
            print("\nRunning script\n")
            removeFiles(os.path.join(ROOT))
            break

        # Choose directory
        for i in range(len(dirs)):
            print(f"{i+1}) {dirs[i]}")

        dir = getInput(dirs, "Choose directory (press ENTER to choose CWD): ")

        if not dir:
            print("Running script\n")
            removeFiles(os.path.join(ROOT))
            break

        print(f"You chose '{dirs[dir-1]}'\n")
        ROOT = os.path.join(ROOT, dirs[dir-1])


if __name__ == '__main__':
    main()
