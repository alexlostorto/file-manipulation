import os
from pypdf import PdfMerger


directory = os.path.dirname(os.path.abspath(__file__))
pdfDirectory = os.path.join(directory, "PDFs")


def sortNumerically(names):
    fileNames = [names, []]
    for name in names:
        fileNames[1].append(int(''.join([c for c in name if c.isdigit()])))

    if (n := len(fileNames[1])) <= 1:
        return fileNames[0]
    
    for i in range(1, n):
        key = fileNames[1][i]
        key2 = fileNames[0][i]
        j = i - 1
        while j >= 0 and key < fileNames[1][j] :
            fileNames[1][j + 1] = fileNames[1][j]
            fileNames[0][j + 1] = fileNames[0][j]
            j -= 1
        fileNames[1][j + 1] = key
        fileNames[0][j + 1] = key2

    return fileNames[0]


def getPDFNames():
    assert os.path.isdir(pdfDirectory)
    files = [f for f in os.listdir(pdfDirectory) if os.path.isfile(os.path.join(pdfDirectory, f)) if f.endswith(".pdf")]
    files = sortNumerically(files)

    return files


def main():
    merger = PdfMerger()
    fileNames = getPDFNames()

    for pdf in fileNames:
        merger.append(os.path.join(pdfDirectory, pdf))

    print("---OUTPUT---")
    fileName = input("File Name: ")

    merger.write(os.path.join(directory, f"{fileName}.pdf"))
    merger.close()


if __name__ == '__main__':
    main()

