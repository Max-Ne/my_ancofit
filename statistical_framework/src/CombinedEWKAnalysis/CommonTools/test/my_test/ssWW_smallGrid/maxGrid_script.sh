#fit for signal scaling
cd /storage/9/mneukum/CMSSW_7_1_9/src
cmsenv
cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test/my_test/ssWW_smallGrid
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_fs0.root ./ssWW_smallGrid_fs0.root
python ./doFit.py --config=ssWW_smallGrid_fs0_config
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_fs1.root ./ssWW_smallGrid_fs1.root
python ./doFit.py --config=ssWW_smallGrid_fs1_config
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_fm0.root ./ssWW_smallGrid_fm0.root
python ./doFit.py --config=ssWW_smallGrid_fm0_config
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_fm1.root ./ssWW_smallGrid_fm1.root
python ./doFit.py --config=ssWW_smallGrid_fm1_config
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_fm7.root ./ssWW_smallGrid_fm7.root
python ./doFit.py --config=ssWW_smallGrid_fm7_config
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_ft0.root ./ssWW_smallGrid_ft0.root
python ./doFit.py --config=ssWW_smallGrid_ft0_config
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_ft1.root ./ssWW_smallGrid_ft1.root
python ./doFit.py --config=ssWW_smallGrid_ft1_config
cp /storage/9/mneukum/test/pythia_output_to_ATGCRooStats/ready_to_fit_ssWW_KC_maxGrid_ft2.root ./ssWW_smallGrid_ft2.root
python ./doFit.py --config=ssWW_smallGrid_ft2_config

# run statistical analysis
#cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fs0.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fs0.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fs1.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fs1.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fm0.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fm0.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fm1.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fm1.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fm7.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fm7.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_ft0.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_ft0.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_ft1.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_ft1.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_ft2.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_ft2.root


