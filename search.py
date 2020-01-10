import easygui
import os

program = "DriveSearch"


def search(path, keyword):
    list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if keyword.lower() in name.lower():
                print("file: ", os.path.join(root, name))
                list.append(os.path.join(root, name))
    return list


def main():
    try:
        print("Please select a folder.")
        directory = easygui.diropenbox("Select a folder to recursively search", program)
        keyword = easygui.enterbox("Enter the keyword to search for, case insensitive", program)
        results = search(directory, keyword)


    except:
        easygui.exceptionbox("Error occurred. Please contact the maintainer of this program", program)


main()
