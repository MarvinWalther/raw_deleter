import os
import argparse

try:
    from send2trash import send2trash
except:
    print("Warning! Library 'send2trash' couldn't be imported. Files will be deletet permanently.")
    send2trash = os.remove


def getDirFileList(path, extensions=('.png', '.jpg', '.jpeg')):
    List = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)) and f.endswith(extensions):
            List.append(os.path.join(path, f))
    return List


def progressbar(it, prefix="", size=50):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("%s|%s%s| %i/%i (%3.1f%%)\r" %(prefix, '█'*x, '-'*(size-x), j, count, 100*j/count), end='', flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n")



def main():
    parser = argparse.ArgumentParser(description='Deletes RAW images that are not present as JPG.')
    parser.add_argument('-folder', type=str, help="Folder to scan and work in, defaults to '.' (current directory).")
    parser.add_argument('-jpg', type=str, help="Ending of JPG files, defaults to '.JPG'.")
    parser.add_argument('-raw', type=str, help="Ending of RAW files, defaults to '.ARW'.")

    args = parser.parse_args()

    folderPath = args.folder if args.folder is not None else '.'
    jpgEndig = args.jpg if args.jpg is not None else '.JPG'
    rawEnding = args.raw if args.raw is not None else '.ARW'

    if rawEnding == '.py':
        print("How dare you...")
        return

    jpgList = getDirFileList(folderPath, jpgEndig)
    rawList = getDirFileList(folderPath, rawEnding)

    filesToDelte = [f for f in rawList if os.path.splitext(f)[0]+jpgEndig not in jpgList]

    if len(filesToDelte) == 0:
        print("Found {} '{}' and {} '{}' files but 0 '{}' files to delete.".format(len(jpgList), jpgEndig, len(rawList),  rawEnding, rawEnding))
    else:
        print("Found {} '{}', {} '{}' files and {} '{}' files to delete.".format(len(jpgList), jpgEndig, len(rawList),  rawEnding, len(filesToDelte), rawEnding))
        while True:
            inp = input("Type 'delete' to delete, 'print' to print the names or 'exit' to exit: ")
            if inp == 'delete':
                for f in progressbar(filesToDelte, prefix='Deleting files '):
                    send2trash(f)
                break
            elif inp == 'print':
                for f in filesToDelte:
                    print(f)
            elif inp == 'exit':
                break
    print('Exiting.')


if __name__ == '__main__':
    main()
