<h1 align="center">File Manipulation</h1>

This repository includes scripts to create, delete or edit multiple files at a time.

```python
# List of scripts
move-files.py
remove-dupes.py
remove-files.py
```

## Functions

#### yesNo(question):

Takes a question as a parameter and prompts the user to input yes or no. This function returns either True for yes or False for no.

```python
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
```

#### getInput(array, question):

Takes an array of options and a question as parameters. This function numbers and logs all the options then prompts the user to make a choice. The option chosen by the user is returned as an integer value.

```python
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
```

## Scripts

#### Remove Dupes

1. Lists all files in the specified directory.

```python
files = [f for f in os.listdir(ROOT) if os.path.isfile(os.path.join(path, f))]
```

2. If the file matches the regex (e.g. (1) or (321)), and the file already exists in the directory, it is appended to the dupFiles list.

```python
dupFiles = []
for file in files:
    position = re.search('\(\d+\).\w+', file)
    fileNameCut = re.sub('\(\d+\)', '', file)
    if position is not None and fileNameCut in files:
        dupFiles.append(file)
```

3. If the user confirms the deletion of the files, use os.remove() to delete each file in dupFiles.

```python
if yesNo("Delete files (y/n): "):
    for file in dupFiles:
        os.remove(os.path.join(ROOT, file))
```

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
