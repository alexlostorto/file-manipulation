<h1 align="center">File Manipulation</h1>

This repository includes scripts to create, delete or edit multiple files at a time.

```python
# List of scripts
move-files.py
remove-dupes.py
remove-files.py
```

## Scripts

#### Remove Dupes

1. Traverses through all files in the specified directory.

```python
for root, _, files in os.walk(ROOT):
```

2. Remove file using the os python module if it is already in the file list.

```python
if fileNameCut in FILE_NAMES:
    print("THIS FILE ALREADY EXISTS")
    os.remove(ROOT+'/'+fileNameCut)
```

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
