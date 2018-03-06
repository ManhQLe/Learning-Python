import os

def rename_file():
    wfolder = "F:\DeepLearningProjects\Python\Files"
    file_list = os.listdir(wfolder)
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(wfolder)
    for f in file_list:
        os.rename(f,f.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_file();