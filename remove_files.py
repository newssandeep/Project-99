import time, os, shutil
path = 'C:/WhitehatJr/Python/files'
days = 30
timeA = 30*24*60*60
if (os.path.exists(path)):
    for root, dirs, files in os.walk(path):
        for i in dirs:
            fpath = os.path.join(path, i)
            if time.time()-os.stat(fpath).st_ctime > timeA:
                shutil.rmtree(fpath)
                print(f"Folder {i} has been deleted!")
        for i in files:
            fpath = os.path.join(path, i)
            if time.time()-os.stat(fpath).st_ctime > timeA:
                os.remove(fpath)
                print(f"File {i} has been deleted!")
else:
    print("The path given doesn't exist!")