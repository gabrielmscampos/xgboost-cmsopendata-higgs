#!/bin/sh

file=$1

xrdcp root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/DYJetsToLL_M-10to50_HT-400toInf_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V19-v1/30000/$file file.root

cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/analyzer/analyzer_cfg_mc.py .

cmsRun analyzer_cfg_mc.py root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/DYJetsToLL_M-10to50_HT-400toInf_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V19-v1/30000/$file

cp result.root /eos/user/g/gamoreir/Project_Higgs/raw/MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-10to50_HT-400toInf_TuneZ2star_8TeV-madgraph-tauola_AODSIM_PU_S10_START53_V19-v1_30000/$file

rm *.root *.py *.txt 
