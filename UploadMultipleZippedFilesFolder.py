import os

pathfile = input("Enter Folder path")
zip_file_list = []
for root, dirs, files in os.walk(pathfile):
    for filename in files:
        if filename.endswith('.zip'):
            filename1 = os.path.join(root,filename)
            zip_file_list.append(filename1)


for zipfile in zip_file_list:
    os.system('%s %s %s' % ('python', 'Zip_Extractor.py', zipfile))