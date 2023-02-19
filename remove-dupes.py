import os

# Absolute path to the directory you want to search
ROOT = r"/storage/emulated/0/"
FILE_LIST = []
FILE_NAMES = []
SUFFIX = '.py'
USE_SUFFIX = False


def main():
    assert os.path.isdir(ROOT)
    for root, _, files in os.walk(ROOT):
        for file in files:
            # append the file name to the list if it ends with '.py'
            path = os.path.join(root, file)
            if file.endswith(SUFFIX) and USE_SUFFIX:
                FILE_LIST.append(path)
            elif not USE_SUFFIX:
                fileName = path[len(ROOT)+1:]
                FILE_LIST.append(path)
                print(fileName)
                fileNameCut = fileName.replace('(1)', "")
            if fileNameCut in FILE_NAMES:
                print("THIS FILE ALREADY EXISTS")
                os.remove(ROOT+'/'+fileNameCut)
            print()
            FILE_NAMES.append(fileName)

    # print all the file names
    # for name in FILE_NAMES:
    #     print(name)


if __name__ == '_main_':
    main()
