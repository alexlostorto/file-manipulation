import os
from lib.inputs import getInput


def traverse(root, question):
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


def checkPath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def getFiles(root, prefix, suffix):
    return [os.path.join(dirPath,f) for (dirPath, _, fileNames) in os.walk(root) for f in fileNames if str(f).startswith(prefix) and str(f).endswith(suffix)]
