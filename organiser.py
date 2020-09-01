#!/usr/bin/python
'''
Files Organiser
Author: Shanmukha Vishnu
gitub: @iam-shanmukha
twitter: @iam_shanmukha

'''
import os
import subprocess
import shutil
#list present working directory files and folders
#ls = files+folders
doc_extensions=[".txt",".docx",".doc",".xls",".xls"]
compress_ext =[".zip",".rar",".zst",".gz",".xz"]
vids_ext=[".mp4",".avi",".mkv"]
pic_ext=[".png",".jpg",".jpeg"]
ls=os.listdir()
def create_dirs():
	directories = ["Pdfs", "Pictures", "Videos", "compressed_Files", "Documents", "Py_files"]
	for directory in directories:	
		if directory in ls:
			print(f"{directory} directory exists...skipping ")
		else:
			print(f"Creating {directory} Directory")
			os.mkdir(directory)
create_dirs()
for file in ls:
	if file.endswith(".pdf"):
		shutil.move(file, "Pdfs")
		print(f"{file} files moved successfully")
	elif file.endswith(tuple(pic_ext)):
		shutil.move(file, "Pictures")
		print(f"{file} files moved successfully")
	elif file.endswith(tuple(vids_ext)):
		shutil.move(file, "Videos")
		print(f"{file} files moved successfully")
	elif file.endswith(tuple(compress_ext)):
		shutil.move(file, "compressed_Files")
		print(f"{file} files moved successfully")
	elif file.endswith(tuple(doc_extensions)):
		shutil.move(file, "compressed_Files")
		print(f"{file} files moved successfully")
	elif file.endswith(".py"):
		if file == "organiser.py":
			continue
		shutil.move(file, "Py_files")
		print(f"{file} files moved successfully")