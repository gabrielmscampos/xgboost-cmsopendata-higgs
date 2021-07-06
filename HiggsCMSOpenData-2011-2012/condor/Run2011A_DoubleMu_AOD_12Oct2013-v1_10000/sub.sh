#!/bin/sh

file=$1

xrdcp root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/AOD/12Oct2013-v1/10000/$file file.root

cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/analyzer/analyzer_cfg_run2011.py .
cp /afs/cern.ch/user/g/gamoreir/public/CMSSW_5_3_32/src/Project_Higgs/datasets/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt .

cmsRun analyzer_cfg_run2011.py root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/AOD/12Oct2013-v1/10000/$file

cp result.root /eos/user/g/gamoreir/Project_Higgs/raw/Run2011A_DoubleMu_AOD_12Oct2013-v1_10000/$file

rm *.root *.py *.txt 
