#!/usr/bin/env python3

from os import listdir, makedirs
from os.path import isfile, join, exists
import concurrent.futures

# Declaring paths
base_path = "/afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs"
path_2011 = base_path + "/datasets/2011_indexfiles"
path_2012 = base_path + "/datasets/2012_indexfiles"
path_mc = base_path + "/datasets/mc_indexfiles"
cernbox_path = "/eos/user/g/gamoreir/Project_Higgs/raw"

def counter(indexFiles):

	n_jobs = 0
	for file in indexFiles:			
		with open(file) as f:
			lines = f.readlines()
		
		n_jobs += len(lines)

	return n_jobs

def countResult(_dir):
	files = listdir(join(cernbox_path, _dir))
	n_jobs = len(files)

	return n_jobs

# Listing all indexFiles
files = [[join(path_2011,f) for f in listdir(path_2011) if isfile(join(path_2011, f))], 
			[join(path_2012,f) for f in listdir(path_2012) if isfile(join(path_2012, f))],
			[join(path_mc,f) for f in listdir(path_mc) if isfile(join(path_mc, f))]]

with concurrent.futures.ProcessPoolExecutor() as executor:
	results = executor.map(counter, files)
	result = [result for result in results]
	n_jobs_to_submit = sum(result)

# Result paths
paths = listdir(cernbox_path)

with concurrent.futures.ProcessPoolExecutor() as executor:
	results = executor.map(countResult, paths)
	result = [result for result in results]
	n_jobs_result = sum(result)

print(n_jobs_to_submit, n_jobs_result)
