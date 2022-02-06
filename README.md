# RAW deleter
This is a simple python script, that scans a folder for JPG and RAW files and deletes all RAW files, for which no corresponding JPG file exists.

# Workflow
1. Shoot with your camera in JPG and RAW, save all files to a folder.
2. Quickly go through all the JPG files and delete the images, you don't want to keep, e.g. *img002.JPG*.
3. Now run the script inside this folder. It will delete *img002.ARW*, because there is no corresponding JPG file with the same name.

| Step 1     | Step 2         | Step 3         |
| ---------- | -------------- | -------------- |
| img001.ARW | img001.ARW     | img001.ARW     |
| img001.JPG | img001.JPG     | img001.JPG     |
| img002.ARW | img002.ARW     | ~~img002.ARW~~ |
| img002.JPG | ~~img002.JPG~~ | ~~img002.JPG~~ |
| img003.ARW | img003.ARW     | img003.ARW     |
| img003.JPG | img003.JPG     | img003.JPG     |

# Requirements
- Python 3 installed

## Recommended
- [send2trash](https://pypi.org/project/Send2Trash/) installed. Without this, the script will delete the files permanently. With [send2trash](https://pypi.org/project/Send2Trash/) installed, it will send them to the Trash instead. You will get a warning if the send2trash package could not be imported.

# Usage
- Copy *raw_deleter.py* into the folder with your images.
- Open a terminal within this folder and run the command `python raw_deleter.py`.
- By default, it will scan for *.JPG* and *.ARW* files (standard for Sony cameras). If your file endings are different, e.g. *.jpg* and *.CR2*, run the command `python raw_deleter.py -j '.jpeg' -r '.cr2'`.
- If you want to use a different folder, run `python raw_deleter.py -f 'path/to/other/folder`
- Once the script has scanned the folder and found some files to delete, you can `delete` or `print` the found files or `exit` without doing anything by typing out the corresponding word.
- Run `python raw_deleter.py -h` to get a help message.

![showcase](showcase.gif)