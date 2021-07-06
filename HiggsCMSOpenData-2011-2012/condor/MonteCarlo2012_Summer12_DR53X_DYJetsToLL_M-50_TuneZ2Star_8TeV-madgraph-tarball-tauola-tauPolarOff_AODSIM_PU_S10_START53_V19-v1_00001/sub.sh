#!/bin/sh

file=$1

xrdcp root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-tauola-tauPolarOff/AODSIM/PU_S10_START53_V19-v1/00001/$file file.root

cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/analyzer/analyzer_cfg_mc.py .

cmsRun analyzer_cfg_mc.py root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-tauola-tauPolarOff/AODSIM/PU_S10_START53_V19-v1/00001/$file

cp result.root /eos/user/g/gamoreir/Project_Higgs/raw/MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-tauola-tauPolarOff_AODSIM_PU_S10_START53_V19-v1_00001/$file

rm *.root *.py *.txt 
