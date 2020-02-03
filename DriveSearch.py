import easygui
import os
import win32api
import pathlib
program = "DriveSearch"


def search(path, keyword):
    abs_path = pathlib.Path(path).resolve()

    list = []
    for root, dirs, files in os.walk(abs_path, topdown=False):
        for name in files:
            if keyword.lower() in name.lower():
                list.append(os.path.join(root, name))
    return list


def save_file(path, text):
    f = open(path+".txt", "a")
    for line in text:
        f.write(line+"\n")
    exit(1)

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
            print("Directory: ", directory)

            # Keyword input
            keyword = easygui.enterbox("Enter the keyword to search for, case insensitive", program)
            if keyword is None:
                if easygui.ccbox("No keyword entered. Try again?", program):
                    continue
                else:
                    exit(0)

            print("Keyword: ", keyword)

            results = search(directory, keyword)

            print("Entries: ", len(results))
            print("Results: ", results)

            if results is None:
                if easygui.ccbox("No Results found. Try again?", program):
                    continue
                else:
                    exit(0)
            header = "To save press OK.\nResults: \n Directory: " + directory + "\n Keyword: " + keyword + "\n Number of Results: " + str(len(results))
            results_pretty = ""
            for line in results:
                results_pretty += line + "\n\n"
            if easygui.textbox(header, program, results_pretty):
                path = easygui.filesavebox("Save Results", program, program + "_" + keyword, results_pretty)
                if path is not None:
                    save_file(path, results)
                    exit(0)
                else:
                    exit(0)
            else:
                exit(0)

    except SystemExit:
        exit(0)
    except:
        easygui.exceptionbox("Error occurred. Please contact the maintainer of this program.", program)


main()

