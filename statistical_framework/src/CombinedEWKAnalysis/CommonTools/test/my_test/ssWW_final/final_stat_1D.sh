#fit for signal scaling
cd /storage/9/mneukum/CMSSW_7_1_9/src
cmsenv
cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test/my_test/ssWW_final

# run statistical analysis
cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_fs0.root ../data/anomalousCoupling/ssWW_fs0_to_fs0.root
cp ./my_test/ssWW_final/signal_proc_ssWW_fs0_to_fs0.root ../data/anomalousCoupling/signal_proc_ssWW_fs0_to_fs0.root

python buildWorkspace_AC.py --config=ssWW_fs0_to_fs0_config > ./ssWW_final/fs0_to_fs0/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_fs0_to_fs0.txt -o aC_ssWW_fs0_to_fs0_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_fs0_to_fs0 --PO poi=fs0 --PO range_fs0=-8.5,8.5 > ./ssWW_final/fs0_to_fs0/output_text2workspace
combine aC_ssWW_fs0_to_fs0_stat.root -M MultiDimFit -P fs0 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/fs0_to_fs0/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root fs0 > ./ssWW_final/fs0_to_fs0/output_build1DInterval
cat ./ssWW_final/fs0_to_fs0/output_build1DInterval


cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_fs1.root ../data/anomalousCoupling/ssWW_fs1_to_fs1.root
cp ./my_test/ssWW_final/signal_proc_ssWW_fs1_to_fs1.root ../data/anomalousCoupling/signal_proc_ssWW_fs1_to_fs1.root

python buildWorkspace_AC.py --config=ssWW_fs1_to_fs1_config > ./ssWW_final/fs1_to_fs1/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_fs1_to_fs1.txt -o aC_ssWW_fs1_to_fs1_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_fs1_to_fs1 --PO poi=fs1 --PO range_fs1=-22.8,23.5 > ./ssWW_final/fs1_to_fs1/output_text2workspace
combine aC_ssWW_fs1_to_fs1_stat.root -M MultiDimFit -P fs1 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/fs1_to_fs1/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root fs1 > ./ssWW_final/fs1_to_fs1/output_build1DInterval
cat ./ssWW_final/fs1_to_fs1/output_build1DInterval


cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_fm0.root ../data/anomalousCoupling/ssWW_fm0_to_fm0.root
cp ./my_test/ssWW_final/signal_proc_ssWW_fm0_to_fm0.root ../data/anomalousCoupling/signal_proc_ssWW_fm0_to_fm0.root

python buildWorkspace_AC.py --config=ssWW_fm0_to_fm0_config > ./ssWW_final/fm0_to_fm0/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_fm0_to_fm0.txt -o aC_ssWW_fm0_to_fm0_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_fm0_to_fm0 --PO poi=fm0 --PO range_fm0=-8.5,8.5 > ./ssWW_final/fm0_to_fm0/output_text2workspace
combine aC_ssWW_fm0_to_fm0_stat.root -M MultiDimFit -P fm0 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/fm0_to_fm0/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root fm0 > ./ssWW_final/fm0_to_fm0/output_build1DInterval
cat ./ssWW_final/fm0_to_fm0/output_build1DInterval


cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_fm1.root ../data/anomalousCoupling/ssWW_fm1_to_fm1.root
cp ./my_test/ssWW_final/signal_proc_ssWW_fm1_to_fm1.root ../data/anomalousCoupling/signal_proc_ssWW_fm1_to_fm1.root

python buildWorkspace_AC.py --config=ssWW_fm1_to_fm1_config > ./ssWW_final/fm1_to_fm1/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_fm1_to_fm1.txt -o aC_ssWW_fm1_to_fm1_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_fm1_to_fm1 --PO poi=fm1 --PO range_fm1=-8.5,8.5 > ./ssWW_final/fm1_to_fm1/output_text2workspace
combine aC_ssWW_fm1_to_fm1_stat.root -M MultiDimFit -P fm1 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/fm1_to_fm1/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root fm1 > ./ssWW_final/fm1_to_fm1/output_build1DInterval
cat ./ssWW_final/fm1_to_fm1/output_build1DInterval


cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_fm7.root ../data/anomalousCoupling/ssWW_fm7_to_fm7.root
cp ./my_test/ssWW_final/signal_proc_ssWW_fm7_to_fm7.root ../data/anomalousCoupling/signal_proc_ssWW_fm7_to_fm7.root

python buildWorkspace_AC.py --config=ssWW_fm7_to_fm7_config > ./ssWW_final/fm7_to_fm7/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_fm7_to_fm7.txt -o aC_ssWW_fm7_to_fm7_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_fm7_to_fm7 --PO poi=fm7 --PO range_fm7=-13.5,13.5 > ./ssWW_final/fm7_to_fm7/output_text2workspace
combine aC_ssWW_fm7_to_fm7_stat.root -M MultiDimFit -P fm7 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/fm7_to_fm7/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root fm7 > ./ssWW_final/fm7_to_fm7/output_build1DInterval
cat ./ssWW_final/fm7_to_fm7/output_build1DInterval


cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_ft0.root ../data/anomalousCoupling/ssWW_ft0_to_ft0.root
cp ./my_test/ssWW_final/signal_proc_ssWW_ft0_to_ft0.root ../data/anomalousCoupling/signal_proc_ssWW_ft0_to_ft0.root

python buildWorkspace_AC.py --config=ssWW_ft0_to_ft0_config > ./ssWW_final/ft0_to_ft0/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_ft0_to_ft0.txt -o aC_ssWW_ft0_to_ft0_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_ft0_to_ft0 --PO poi=ft0 --PO range_ft0=-.72,.72 > ./ssWW_final/ft0_to_ft0/output_text2workspace
combine aC_ssWW_ft0_to_ft0_stat.root -M MultiDimFit -P ft0 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/ft0_to_ft0/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root ft0 > ./ssWW_final/ft0_to_ft0/output_build1DInterval
cat ./ssWW_final/ft0_to_ft0/output_build1DInterval


cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_ft1.root ../data/anomalousCoupling/ssWW_ft1_to_ft1.root
cp ./my_test/ssWW_final/signal_proc_ssWW_ft1_to_ft1.root ../data/anomalousCoupling/signal_proc_ssWW_ft1_to_ft1.root

python buildWorkspace_AC.py --config=ssWW_ft1_to_ft1_config > ./ssWW_final/ft1_to_ft1/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_ft1_to_ft1.txt -o aC_ssWW_ft1_to_ft1_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_ft1_to_ft1 --PO poi=ft1 --PO range_ft1=-0.275,0.29 > ./ssWW_final/ft1_to_ft1/output_text2workspace
combine aC_ssWW_ft1_to_ft1_stat.root -M MultiDimFit -P ft1 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/ft1_to_ft1/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root ft1 > ./ssWW_final/ft1_to_ft1/output_build1DInterval
cat ./ssWW_final/ft1_to_ft1/output_build1DInterval


cd /storage/9/mneukum/CMSSW_7_1_9/src/CombinedEWKAnalysis/CommonTools/test
cp ../data/anomalousCoupling/ssWW_smallGrid_ft2.root ../data/anomalousCoupling/ssWW_ft2_to_ft2.root
cp ./my_test/ssWW_final/signal_proc_ssWW_ft2_to_ft2.root ../data/anomalousCoupling/signal_proc_ssWW_ft2_to_ft2.root

python buildWorkspace_AC.py --config=ssWW_ft2_to_ft2_config > ./ssWW_final/ft2_to_ft2/output_buildWorkspace_AC
text2workspace.py -m 125 aC_ssWW_ft2_to_ft2.txt -o aC_ssWW_ft2_to_ft2_stat.root -P CombinedEWKAnalysis.CommonTools.ACModel:par1_TF1_Model --PO channels=ssWW_ft2_to_ft2 --PO poi=ft2 --PO range_ft2=-13.5,13.5 > ./ssWW_final/ft2_to_ft2/output_text2workspace
combine aC_ssWW_ft2_to_ft2_stat.root -M MultiDimFit -P ft2 --floatOtherPOIs=0 --algo=grid --points=1000 --minimizerStrategy=2 --saveSpecifiedNuis all --saveSpecifiedFunc model_s,model_b > ./ssWW_final/ft2_to_ft2/output_combine
python build1DInterval.py -25.0 25.0 higgsCombineTest.MultiDimFit.mH120.root ft2 > ./ssWW_final/ft2_to_ft2/output_build1DInterval
cat ./ssWW_final/ft2_to_ft2/output_build1DInterval

cd -

#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fs0.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fs0.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fs1.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fs1.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fm0.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fm0.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fm1.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fm1.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_fm7.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_fm7.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_ft0.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_ft0.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_ft1.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_ft1.root
#cp ./my_test/ssWW_smallGrid/signal_proc_ssWW_smallGrid_ft2.root ../data/anomalousCoupling/signal_proc_ssWW_smallGrid_ft2.root


