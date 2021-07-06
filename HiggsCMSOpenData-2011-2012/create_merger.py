#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join, exists
import concurrent.futures

# LXPLUS Path
cernbox_raw = "/eos/user/g/gamoreir/Project_Higgs/raw"
cernbox_semiraw = "/eos/user/g/gamoreir/Project_Higgs/semi-raw"
cernbox_treated = "/eos/user/g/gamoreir/Project_Higgs/treated"

#  # Home Path
# cernbox_raw = "/mnt/Seagate/cernbox/Project_Higgs/raw"
# cernbox_semiraw = "/mnt/Seagate/cernbox/Project_Higgs/semi-raw"
# cernbox_treated = "/mnt/Seagate/cernbox/Project_Higgs/treated"

def check_singlefiles(path):
	files = [f for f in listdir(join(cernbox_raw+"/"+path)) if isfile(join(cernbox_raw+"/"+path, f))]
	return True if len(files) == 1 else False

def unique(mylist):
	used = set()
	return [x for x in mylist if x not in used and (used.add(x) or True)]

def merge_raw():

	folders = listdir(cernbox_raw)

	with concurrent.futures.ProcessPoolExecutor() as executor:
		results = executor.map(check_singlefiles, folders)
		results = [x for x in results]
		cp_list = [x for x, y in zip(folders, results) if y is True]
		hadd_list = [x for x, y in zip(folders, results) if y is False]

	with open("raw.sh", "w") as f:

		f.write("#!/bin/usr/env bash\n\n")

		for path in hadd_list:
			print(f"Processing file {path}")
			files = [cernbox_raw+"/"+path+"/"+f for f in listdir(cernbox_raw+"/"+path) if isfile(join(cernbox_raw+"/"+path, f))]
			string = " ".join(files)
			f.write(f"hadd {cernbox_raw+'/'+path+'.root'} {string} &\n")

		for path in cp_list:
			print(f"Processing file {path}")
			files = [cernbox_raw+"/"+path+"/"+f for f in listdir(cernbox_raw+"/"+path) if isfile(join(cernbox_raw+"/"+path, f))]
			string = "".join(files)
			f.write(f"cp {string} {cernbox_raw+'/'+path+'.root'} &\n")

def merge_semiraw():

	onlyfiles = [f for f in listdir(cernbox_semiraw) if not f.startswith(".") and isfile(join(cernbox_semiraw, f))]
	version = [file.split("_")[len(file.split("_"))-1] for file in onlyfiles]
	files = ["_".join(file.split("_")[0:len(file.split("_"))-1]) for file in onlyfiles]
	res = [([i for i,v in enumerate(files) if v == file], file) for file in unique(files)]
	res = {join(cernbox_treated, t[1]+".root"): [join(cernbox_semiraw, "_".join([files[idx], version[idx]])) for idx in t[0]] for t in res}

	with open("semiraw.sh", "w") as f:

		f.write("#!/bin/usr/env bash\n\n")

		for newfile, files in zip(res.keys(), res.values()):
			print(f"Processing file {newfile}")
			string = " ".join(files)

			if len(files) == 1:
				f.write(f"cp {string} {newfile} &\n")
			else:
				f.write(f"hadd {newfile} {string} &\n")