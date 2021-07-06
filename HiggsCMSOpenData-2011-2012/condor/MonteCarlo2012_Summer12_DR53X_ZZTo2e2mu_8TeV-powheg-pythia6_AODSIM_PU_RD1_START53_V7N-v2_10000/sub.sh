#!/bin/sh

file=$1

xrdcp root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/ZZTo2e2mu_8TeV-powheg-pythia6/AODSIM/PU_RD1_START53_V7N-v2/10000/$file file.root

cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/analyzer/analyzer_cfg_mc.py .

cmsRun analyzer_cfg_mc.py root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/ZZTo2e2mu_8TeV-powheg-pythia6/AODSIM/PU_RD1_START53_V7N-v2/10000/$file

cp result.root /eos/user/g/gamoreir/Project_Higgs/raw/MonteCarlo2012_Summer12_DR53X_ZZTo2e2mu_8TeV-powheg-pythia6_AODSIM_PU_RD1_START53_V7N-v2_10000/$file

rm *.root *.py *.txt 
