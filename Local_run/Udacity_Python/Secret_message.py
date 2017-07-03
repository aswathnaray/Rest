import os


def rename_files():

    #get filenames from folder
    file_list = os.listdir(r"C:\Users\BADRINAR\Downloads\prank\prank")
    print file_list

    act_path = os.getcwd()
    os.chdir(r"C:\Users\BADRINAR\Downloads\prank\prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(act_path)

rename_files()