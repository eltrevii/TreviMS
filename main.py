__import__("os").system("pip install requests")

import os, requests as re, zipfile as zf, hashlib as hl
from io import BytesIO
from tkinter import Tk
from tkinter.filedialog import askopenfilename as aof

def main():
	clear()
	
	print("downloading hashes...")
	hashes_req   = re.get("https://bazaar.abuse.ch/export/txt/md5/full/").content

	print("extracting hashes (zip)...")
	hashes_zf    = zf.ZipFile(BytesIO(hashes_req), "r")
	hashes_file  = hashes_zf.read("full_md5.txt")
	hashes_raw   = str(hashes_file).replace("\\r", "").split("\\n")
	hashes       = [x for x in hashes_raw if not '#' in x][:-1]

	clear()

	print("waiting for file selection...")
	Tk().withdraw()
	filename     = aof(title="Select program to scan")

	try: file    = open(filename, "rb").read()
	except: os._exit(0)

	file_md5     = hl.md5(file).hexdigest()

	clear()

	print(f"scanning in hashes... this shouldn't take much time")
	if file_md5 in hashes:
		print(f"virus detected for hash: {file_md5}")

def clear(): os.system("cls") if os.name == "nt" else os.system("clear")

if __name__ == '__main__':
	main()