#!/usr/bin/env python3

from os import listdir, makedirs
from os.path import isfile, join, exists
from shutil import copy

# Declaring paths
base_path = "/afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs"
condor_path = base_path + "/condor"
path_2011 = base_path + "/datasets/2011_indexfiles"
path_2012 = base_path + "/datasets/2012_indexfiles"
path_mc = base_path + "/datasets/mc_indexfiles"
cernbox_path = "/eos/user/g/gamoreir/Project_Higgs/raw"

# Count total number of jobs
n_jobs_2011 = 0
n_jobs_2012 = 0
n_jobs_mc = 0

# Create condor dir
try:
	makedirs(condor_path)
except FileExistsError:
	print("Condor path already exists.")
	pass

# Create cernbox result path
try:
	makedirs(cernbox_path)
except FileExistsError:
	print("Condor path already exists.")
	pass

try:
	makedirs("/eos/user/g/gamoreir/Project_Higgs/semi-raw")
except FileExistsError:
	print("Condor path already exists.")
	pass

try:
	makedirs("/eos/user/g/gamoreir/Project_Higgs/treated")
except FileExistsError:
	print("Condor path already exists.")
	pass

# run2011
files2011 = [f for f in listdir(path_2011) if isfile(join(path_2011, f))]
rel_dirs_2011 = ["_".join(file.split("_")[1:len(file.split("_"))-2]) for file in files2011]
abs_dirs_2011 = ["/".join([condor_path, "_".join(file.split("_")[1:len(file.split("_"))-2])]) for file in files2011]
abs_dirs_2011_cernbox = ["/".join([cernbox_path, "_".join(file.split("_")[1:len(file.split("_"))-2])]) for file in files2011]

for file, abs_dir, rel_dir, cernbox_dir in zip(files2011, abs_dirs_2011, rel_dirs_2011, abs_dirs_2011_cernbox):

	try:
		makedirs(abs_dir)
	except:
		print(abs_dir + " already exists.")
		pass

	try:
		makedirs(cernbox_dir)
	except:
		print(cernbox_dir + " already exists.")

	print("Processing file " + file)

	filePath = "/".join([path_2011, file])

	with open(filePath) as f:
		lines = f.readlines()

	lines = [line.strip("\n") for line in lines]
	indexFile = [line.split("/")[len(line.split("/"))-1] for line in lines]
	rootFile = set(["/".join(line.split("/")[0:len(line.split("/"))-1]) + "/$file" for line in lines])
	xrdcp = set(["xrdcp " + "/".join(line.split("/")[0:len(line.split("/"))-1]) + "/$file file.root" for line in lines])

	copy(base_path + "/analyzer/analyzer_cfg_run2011.py", abs_dir)
	copy(base_path + "/datasets/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt", abs_dir)
	n_jobs_2011 += len(indexFile)

	with open(abs_dir + "/ListOfFiles.txt", "w") as out:

		for line in indexFile:
			out.write(line + "\n")

	with open(abs_dir + "/sub.sh", "w") as out:

		out.write("#!/bin/sh\n")
		out.write("\n")
		out.write("file=$1\n")
		out.write("\n")

		for line in xrdcp:
			out.write(line + "\n")

		out.write("\n")
		out.write("cp " + base_path + "/analyzer/analyzer_cfg_run2011.py .\n")
		out.write("cp " + base_path + "/datasets/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt .\n")
		out.write("\n")

		for line in rootFile:
			out.write("cmsRun analyzer_cfg_run2011.py " + line + "\n")

		out.write("\n")
		#out.write("cp result.root " + condor_path + "/" + rel_dir + "/root/$file\n")
		out.write("cp result.root " + cernbox_path + "/" + rel_dir + "/$file\n")
		out.write("\n")
		out.write("rm *.root *.py *.txt \n")

	with open(abs_dir + "/condor", "w") as out:

		out.write("executable = sub.sh\n")
		out.write("\n")
		#out.write("output     = test/output_$(ProcId).out\n")
		#out.write("error      = test/output_$(ProcId).err\n")
		#out.write("log        = test/output_$(ProcId).log\n")
		out.write("\n")
		out.write("getenv     = True\n")
		out.write("\n")
		out.write('environment = "X509_USER_PROXY=$ENV(HOME)/x509up_u61469"\n')
		out.write("\n")
		out.write('requirements = (OpSysAndVer =?= "SLCern6")\n')
		out.write("\n")
		out.write('+JobFlavour = "longlunch"\n')
		out.write("\n")
		out.write("should_transfer_files = IF_NEEDED\n")
		out.write("when_to_transfer_output = ON_EXIT\n")
		out.write("\n")
		out.write("queue arguments from ListOfFiles.txt\n")

# run2012
files2012 = [f for f in listdir(path_2012) if isfile(join(path_2012, f))]
rel_dirs_2012 = ["_".join(file.split("_")[1:len(file.split("_"))-2]) for file in files2012]
abs_dirs_2012 = ["/".join([condor_path, "_".join(file.split("_")[1:len(file.split("_"))-2])]) for file in files2012]
abs_dirs_2012_cernbox = ["/".join([cernbox_path, "_".join(file.split("_")[1:len(file.split("_"))-2])]) for file in files2012]

for file, abs_dir, rel_dir, cernbox_dir in zip(files2012, abs_dirs_2012, rel_dirs_2012, abs_dirs_2012_cernbox):

	try:
		makedirs(abs_dir)
	except:
		print(abs_dir + " already exists.")
		pass

	try:
		makedirs(cernbox_dir)
	except:
		print(cernbox_dir + " already exists.")

	print("Processing file " + file)

	filePath = "/".join([path_2012, file])

	with open(filePath) as f:
		lines = f.readlines()

	lines = [line.strip("\n") for line in lines]
	indexFile = [line.split("/")[len(line.split("/"))-1] for line in lines]
	rootFile = set(["/".join(line.split("/")[0:len(line.split("/"))-1]) + "/$file" for line in lines])
	xrdcp = set(["xrdcp " + "/".join(line.split("/")[0:len(line.split("/"))-1]) + "/$file file.root" for line in lines])

	copy(base_path + "/analyzer/analyzer_cfg_run2012.py", abs_dir)
	copy(base_path + "/datasets/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt", abs_dir)
	n_jobs_2012 += len(indexFile)

	with open(abs_dir + "/ListOfFiles.txt", "w") as out:

		for line in indexFile:
			out.write(line + "\n")

	with open(abs_dir + "/sub.sh", "w") as out:

		out.write("#!/bin/sh\n")
		out.write("\n")
		out.write("file=$1\n")
		out.write("\n")

		for line in xrdcp:
			out.write(line + "\n")

		out.write("\n")
		out.write("cp " + base_path + "/analyzer/analyzer_cfg_run2012.py .\n")
		out.write("cp " + base_path + "/datasets/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt .\n")
		out.write("\n")

		for line in rootFile:
			out.write("cmsRun analyzer_cfg_run2012.py " + line + "\n")

		out.write("\n")
		#out.write("cp result.root " + condor_path + "/" + rel_dir + "/root/$file\n")
		out.write("cp result.root " + cernbox_path + "/" + rel_dir + "/$file\n")
		out.write("\n")
		out.write("rm *.root *.py *.txt \n")

	with open(abs_dir + "/condor", "w") as out:

		out.write("executable = sub.sh\n")
		out.write("\n")
		# out.write("output     = test/output_$(ProcId).out\n")
		# out.write("error      = test/output_$(ProcId).err\n")
		# out.write("log        = test/output_$(ProcId).log\n")
		out.write("\n")
		out.write("getenv     = True\n")
		out.write("\n")
		out.write('environment = "X509_USER_PROXY=$ENV(HOME)/x509up_u61469"\n')
		out.write("\n")
		out.write('requirements = (OpSysAndVer =?= "SLCern6")\n')
		out.write("\n")
		out.write('+JobFlavour = "longlunch"\n')
		out.write("\n")
		out.write("should_transfer_files = IF_NEEDED\n")
		out.write("when_to_transfer_output = ON_EXIT\n")
		out.write("\n")
		out.write("queue arguments from ListOfFiles.txt\n")

# mc
filesmc = [f for f in listdir(path_mc) if isfile(join(path_mc, f))]
rel_dirs_mc = ["_".join(file.split("_")[1:len(file.split("_"))-2]) for file in filesmc]
abs_dirs_mc = ["/".join([condor_path, "_".join(file.split("_")[1:len(file.split("_"))-2])]) for file in filesmc]
abs_dirs_mc_cernbox = ["/".join([cernbox_path, "_".join(file.split("_")[1:len(file.split("_"))-2])]) for file in filesmc]

for file, abs_dir, rel_dir, cernbox_dir in zip(filesmc, abs_dirs_mc, rel_dirs_mc, abs_dirs_mc_cernbox):

	try:
		makedirs(abs_dir)
	except:
		print(abs_dir + " already exists.")
		pass

	try:
		makedirs(cernbox_dir)
	except:
		print(cernbox_dir + " already exists.")

	print("Processing file " + file)

	filePath = "/".join([path_mc, file])

	with open(filePath) as f:
		lines = f.readlines()

	lines = [line.strip("\n") for line in lines]
	indexFile = [line.split("/")[len(line.split("/"))-1] for line in lines]
	rootFile = set(["/".join(line.split("/")[0:len(line.split("/"))-1]) + "/$file" for line in lines])
	xrdcp = set(["xrdcp " + "/".join(line.split("/")[0:len(line.split("/"))-1]) + "/$file file.root" for line in lines])

	copy(base_path + "/analyzer/analyzer_cfg_mc.py", abs_dir)
	n_jobs_mc += len(indexFile)

	with open(abs_dir + "/ListOfFiles.txt", "w") as out:

		for line in indexFile:
			out.write(line + "\n")

	with open(abs_dir + "/sub.sh", "w") as out:

		out.write("#!/bin/sh\n")
		out.write("\n")
		out.write("file=$1\n")
		out.write("\n")

		for line in xrdcp:
			out.write(line + "\n")

		out.write("\n")
		out.write("cp " + base_path + "/analyzer/analyzer_cfg_mc.py .\n")
		out.write("\n")

		for line in rootFile:
			out.write("cmsRun analyzer_cfg_mc.py " + line + "\n")

		out.write("\n")
		#out.write("cp result.root " + condor_path + "/" + rel_dir + "/root/$file\n")
		out.write("cp result.root " + cernbox_path + "/" + rel_dir + "/$file\n")
		out.write("\n")
		out.write("rm *.root *.py *.txt \n")

	with open(abs_dir + "/condor", "w") as out:

		out.write("executable = sub.sh\n")
		out.write("\n")
		# out.write("output     = test/output_$(ProcId).out\n")
		# out.write("error      = test/output_$(ProcId).err\n")
		# out.write("log        = test/output_$(ProcId).log\n")
		out.write("\n")
		out.write("getenv     = True\n")
		out.write("\n")
		out.write('environment = "X509_USER_PROXY=$ENV(HOME)/x509up_u61469"\n')
		out.write("\n")
		out.write('requirements = (OpSysAndVer =?= "SLCern6")\n')
		out.write("\n")
		out.write('+JobFlavour = "longlunch"\n')
		out.write("\n")
		out.write("should_transfer_files = IF_NEEDED\n")
		out.write("when_to_transfer_output = ON_EXIT\n")
		out.write("\n")
		out.write("queue arguments from ListOfFiles.txt\n")

print("\nn_jobs_2011 = " + str(n_jobs_2011))
print("n_jobs_2012 = " + str(n_jobs_2012))
print("n_jobs_mc =" + str(n_jobs_mc))
print("n_jobs = " + str(n_jobs_2011+n_jobs_2012+n_jobs_mc))
