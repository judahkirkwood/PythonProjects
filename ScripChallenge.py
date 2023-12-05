import os


folderPath = 'C:\\Users\\Judah Kirkwood\\OneDrive\\Desktop\\A\\'
files = os.listdir(folderPath)


for file in files:
    if file.endswith(".txt"):
        filePath = os.path.join(folderPath,file)
        modifiedTime = os.path.getmtime(filePath)
        formattedTime = f"{file} - Last Modified: {modifiedTime}"
        print(formattedTime)



