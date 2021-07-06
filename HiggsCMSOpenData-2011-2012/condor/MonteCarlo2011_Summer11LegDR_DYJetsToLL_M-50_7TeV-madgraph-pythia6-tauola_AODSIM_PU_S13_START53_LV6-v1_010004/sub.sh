#!/bin/sh

file=$1

xrdcp root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola/AODSIM/PU_S13_START53_LV6-v1/010004/$file file.root

cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/analyzer/analyzer_cfg_mc.py .

cmsRun analyzer_cfg_mc.py root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola/AODSIM/PU_S13_START53_LV6-v1/010004/$file

cp result.root /eos/user/g/gamoreir/Project_Higgs/raw/MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_010004/$file

rm *.root *.py *.txt 
