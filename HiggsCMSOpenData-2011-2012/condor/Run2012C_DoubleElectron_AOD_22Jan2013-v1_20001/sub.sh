#!/bin/sh

file=$1

xrdcp root://eospublic.cern.ch//eos/opendata/cms/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20001/$file file.root

cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/analyzer/analyzer_cfg_run2012.py .
cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/datasets/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt .

cmsRun analyzer_cfg_run2012.py root://eospublic.cern.ch//eos/opendata/cms/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20001/$file

cp result.root /eos/user/g/gamoreir/Project_Higgs/raw/Run2012C_DoubleElectron_AOD_22Jan2013-v1_20001/$file

rm *.root *.py *.txt 
