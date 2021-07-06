#!/bin/sh

file=$1

xrdcp root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/ZZTo4e_mll4_7TeV-powheg-pythia6/AODSIM/PU_S13_START53_LV6-v1/30000/$file file.root

cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/analyzer/analyzer_cfg_mc.py .

cmsRun analyzer_cfg_mc.py root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/ZZTo4e_mll4_7TeV-powheg-pythia6/AODSIM/PU_S13_START53_LV6-v1/30000/$file

cp result.root /eos/user/g/gamoreir/Project_Higgs/raw/MonteCarlo2011_Summer11LegDR_ZZTo4e_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_30000/$file

rm *.root *.py *.txt 
