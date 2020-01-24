import easygui
import os

program = "DriveSearch"


def search(path, keyword):
    list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if keyword.lower() in name.lower():
                list.append(os.path.join(root, name) + "\n\n")
    return list

def main():
    try:
        while True:
            # Directory input
            directory = easygui.diropenbox("Select a folder to recursively search", program)
            if directory is None:
                if easygui.ccbox("No folder selected. Try again?", program):
                    continue
                else:
                    exit()

            # Keyword input
            keyword = easygui.enterbox("Enter the keyword to search for, case insensitive", program)
            if keyword is None:
                if easygui.ccbox("No keyword entered. Try again?", program):
                    continue
                else:
                    exit(0)

            results = search(directory, keyword)

            if results is None:
                if easygui.ccbox("No Results found. Try again?", program):
                    continue
                else:
                    exit(0)
            header = "To save press OK\nResults: \n Directory: " + directory + "\n Keyword: " + keyword + "\n Number of Results: " + str(len(results))
            if easygui.textbox(header, program, results):
                easygui.filesavebox("Save Results", program, program + "_" + keyword, results)
            else:
                exit(0)




    except SystemExit:
        exit(0)
    except:
        easygui.exceptionbox("Error occurred. Please contact the maintainer of this program", program)


main()
