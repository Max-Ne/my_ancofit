#! /usr/bin/env python

import sys
import os
from array import array
from math import sqrt,exp
from optparse import OptionParser
from ConfigParser import SafeConfigParser
#root and roofit classes
import ROOT
from ROOT import RooWorkspace, TFile, TH1, TChain, RooDataHist, \
    RooHistFunc, RooFit, RooSimultaneous, RooDataSet, TH1F, \
    RooRealVar, RooBinning, RooThresholdCategory, RooCategory, \
    RooArgSet, RooArgList, TH2F, TH2D, TTree, TF2, TH1F, TH1D, TF1, TH3F, TH3D, TF3, RooFormulaVar, TCanvas, TProfile2D

parser = OptionParser(description="%prog : A RooStats Implementation of Anomalous Triple Gauge Coupling Analysis.",
                      usage="buildWZworkspace --config=example_config.cfg")
cfgparse = SafeConfigParser()
parser.add_option("--config",dest="config",help="The name of the input configuration file.")
(options,args) = parser.parse_args()
cfgparse.read(options.config)
options.config = cfgparse # put the parsed config file into our options

cfg = options.config

fit_sections = cfg.sections()
fit_sections.remove('Global') #don't need to iterate over the global configuration

pwd = ROOT.gDirectory.GetPath()

print 'starting ...'

canv = TCanvas("my_c","my_c",1600,800)
canv.Divide(3,3)
canv2 = TCanvas("my_c2","my_c2",1600,800)
canv2.Divide(3,3)

histos = []
histos_norm= []
funcs = []
funcs_norm = []
efficiencies = [0.38,0.51,0.62,0.66,0.66]

TH1.SetDefaultSumw2();

for section in fit_sections:
    print 'section: ', section
    sigFile = cfg.get(section,'signal_model').split(':')[0]
    sigObj  = cfg.get(section,'signal_model').split(':')[1]

    print sigFile, sigObj
        
#    workspaceName = cfg.get('Global','workspace')        
    
#    ws = RooWorkspace(workspaceName)    
    
    pwd = ROOT.gDirectory.GetPath()

    sigFile = cfg.get(section,'signal_model').split(':')[0]
    sigObj  = cfg.get(section,'signal_model').split(':')[1]
    
    print ' sigFile: ', sigFile, ' obj: ', sigObj
    
    sigFile = TFile.Open(sigFile)
    ROOT.gDirectory.cd(pwd)    
    sigObj = sigFile.Get(sigObj)
    if isinstance(sigObj,ROOT.TTree):
        sigObj = sigObj.CloneTree()
    else:
        print 'Signal model must be a TTree (for now)'
        exit(1)    
    sigFile.Close()
    ROOT.gDirectory.cd(pwd)

    bins = [float(i) for i in cfg.get(section,'obsBins').split(',')]

    nObsBins = len(bins)-1
    weightvar = cfg.get('Global','signal_weight_var')

    nGridPointsForNewF=0
    model=cfg.get('Global','model') 
    func_string='[0] + [1]*x + [2]*y'
    cfg_items=cfg.items('Global')
    for cfg_item in cfg_items:
        if 'function' in cfg_item:
            func_string=cfg.get('Global','function')   
        if 'outputgridpoints' in cfg_item:
            nGridPointsForNewF=int(cfg.get('Global','outputgridpoints'))
    
    print '=====================> ngrid= ',nGridPointsForNewF
    print '   fitting: ', func_string, '  model: ', model


    if (model=="par1_TH1" or model=="par1_TF1"):
        par1Name = cfg.get('Global','par1Name')
        nGridPar1Bins = cfg.getint('Global','nGridPar1Bins')
        par1GridMax = cfg.getfloat('Global','par1GridMax')
        par1GridMin = cfg.getfloat('Global','par1GridMin')
        par1PadSize = (par1GridMax-par1GridMin)/(2*nGridPar1Bins-2)
        par1GridMax = par1GridMax + par1PadSize #add padding to put values at bin centers, assuming evently spaced points
        par1GridMin = par1GridMin - par1PadSize #add padding to put values at bin centers, assuming evently spaced points
    elif (model=="par1par2_TH2" or model=="par1par2_TF2"):
        par1Name = cfg.get('Global','par1Name')
        par2Name = cfg.get('Global','par2Name')
        nGridPar1Bins = cfg.getint('Global','nGridPar1Bins')
        nGridPar2Bins = cfg.getint('Global','nGridPar2Bins')
        par1GridMax = cfg.getfloat('Global','par1GridMax')
        par1GridMin = cfg.getfloat('Global','par1GridMin')
        par2GridMax = cfg.getfloat('Global','par2GridMax')
        par2GridMin = cfg.getfloat('Global','par2GridMin')
        par1PadSize = (par1GridMax-par1GridMin)/(2*nGridPar1Bins-2)
        par2PadSize = (par2GridMax-par2GridMin)/(2*nGridPar2Bins-2)
        par1GridMax = par1GridMax + par1PadSize #add padding to put values at bin centers, assuming evently spaced points
        par1GridMin = par1GridMin - par1PadSize #add padding to put values at bin centers, assuming evently spaced points
        par2GridMax = par2GridMax + par2PadSize #add padding to put values at bin centers, assuming evently spaced points
        par2GridMin = par2GridMin - par2PadSize #add padding to put values at bin centers, assuming evently spaced points
    elif (model=="par1par2par3_TH3" or model=="par1par2par3_TF3"):
        par1Name = cfg.get('Global','par1Name')
        par2Name = cfg.get('Global','par2Name')
        par3Name = cfg.get('Global','par3Name')
        nGridPar1Bins = cfg.getint('Global','nGridPar1Bins')
        nGridPar2Bins = cfg.getint('Global','nGridPar2Bins')
        nGridPar3Bins = cfg.getint('Global','nGridPar3Bins')
        par1GridMax = cfg.getfloat('Global','par1GridMax')
        par1GridMin = cfg.getfloat('Global','par1GridMin')
        par2GridMax = cfg.getfloat('Global','par2GridMax')
        par2GridMin = cfg.getfloat('Global','par2GridMin')
        par3GridMax = cfg.getfloat('Global','par3GridMax')
        par3GridMin = cfg.getfloat('Global','par3GridMin')
        par1PadSize = (par1GridMax-par1GridMin)/(2*nGridPar1Bins-2)
        par2PadSize = (par2GridMax-par2GridMin)/(2*nGridPar2Bins-2)
        par3PadSize = (par3GridMax-par3GridMin)/(2*nGridPar3Bins-2)
        par1GridMax = par1GridMax + par1PadSize #add padding to put values at bin centers, assuming evently spaced points
        par1GridMin = par1GridMin - par1PadSize #add padding to put values at bin centers, assuming evently spaced points
        par2GridMax = par2GridMax + par2PadSize #add padding to put values at bin centers, assuming evently spaced points
        par2GridMin = par2GridMin - par2PadSize #add padding to put values at bin centers, assuming evently spaced points
        par3GridMax = par3GridMax + par3PadSize #add padding to put values at bin centers, assuming evently spaced points
        par3GridMin = par3GridMin - par3PadSize #add padding to put values at bin centers, assuming evently spaced points

        print model
        

    
    #create the variables for the nxn grid, doesn't go in the workspace
#    obs_mc = ws.var('%s_%s'%(cfg.get('Global','obsVar'),section))    
    weight = RooRealVar(weightvar,'the weight of the data',0,1000)

    bins = [float(i) for i in cfg.get(section,'obsBins').split(',')]

#    print bins
#    break;


    outfile_newF = TFile.Open('signal_proc_'+section+'.root','RECREATE')

#    print ('outfile_newF = signal_proc'+section+'.root');


    for i in range(1,len(bins)):
        
        if (model=="par1_TH1" or model=="par1_TF1"):
            theBaseData = TH1F('theBaseData_'+section+'_'+str(i),'Base Histogram for RooDataHist',
                               nGridPar1Bins,par1GridMin,par1GridMax)
            newFormatInput = TH1D('bin_content_par1_'+str(i),'bincontent',
                                  nGridPointsForNewF,par1GridMin,par1GridMax)
        elif (model=="par1par2_TH2" or model=="par1par2_TF2"):
            theBaseData = TH2F('theBaseData_'+section+'_'+str(i),'Base Histogram for RooDataHist',
                               nGridPar1Bins,par1GridMin,par1GridMax,
                               nGridPar2Bins,par2GridMin,par2GridMax)
            newFormatInput = TH2D('bin_content_par1_par2_'+str(i),'bincontent',
                                  nGridPointsForNewF,par1GridMin,par1GridMax,
                                  nGridPointsForNewF,par2GridMin,par2GridMax)
        elif (model=="par1par2par3_TH3" or model=="par1par2par3_TF3"):
            theBaseData = TH3F('theBaseData_'+section+'_'+str(i),'Base Histogram for RooDataHist',
                               nGridPar1Bins,par1GridMin,par1GridMax,
                               nGridPar2Bins,par2GridMin,par2GridMax,
                               nGridPar3Bins,par3GridMin,par3GridMax)
            newFormatInput = TH3D('bin_content_par1_par2_par3_'+str(i),'bincontent',
                                  nGridPointsForNewF,par1GridMin,par1GridMax,
                                  nGridPointsForNewF,par2GridMin,par2GridMax,
                                  nGridPointsForNewF,par3GridMin,par3GridMax)
        
        if i != len(bins) - 1:
            binMin = bins[i-1]
            binMax = bins[i]
            
            if (model=="par1_TH1" or model=="par1_TF1"):
                sigObj.Draw(par1Name+' >> theBaseData_'+section+'_'+str(i),
#                            '('+weight.GetName()+'*'+str(efficiencies[i-1])+')'+'*('+cfg.get(section,'obsVar') + #
                            weight.GetName()+'*('+cfg.get(section,'obsVar') + #
                            ' > ' + str(binMin) +
                            ' && ' + cfg.get(section,'obsVar') +
                            ' < ' + str(binMax)+')','goff')
            elif (model=="par1par2_TH2" or model=="par1par2_TF2"):
                sigObj.Draw(par2Name+':'+par1Name+' >> theBaseData_'+section+'_'+str(i),
                            weight.GetName()+'*('+cfg.get(section,'obsVar') + #
#                            '('+weight.GetName()+'/64.4217490480265127)'+'*('+cfg.get(section,'obsVar') + #
#                            '('+weight.GetName()+'*'+efficiencies[i-1]+')'+'*('+cfg.get(section,'obsVar') + #
                            ' > ' + str(binMin) +
                            ' && ' + cfg.get(section,'obsVar') +
                            ' < ' + str(binMax)+')','goff')
            elif (model=="par1par2_TH3" or model=="par1par2_TF3"):
                sigObj.Draw(par3Name+':'+par2Name+':'+par1Name+' >> theBaseData_'+section+'_'+str(i),
                            weight.GetName()+'*('+cfg.get(section,'obsVar') + #
                            ' > ' + str(binMin) +
                            ' && ' + cfg.get(section,'obsVar') +
                            ' < ' + str(binMax)+')','goff')
        else:
            if (model=="par1_TH1" or model=="par1_TF1"):
                sigObj.Draw(par1Name+' >> theBaseData_'+section+'_'+str(i),
#                            '('+weight.GetName()+'*'+str(efficiencies[i-1])+')'+'*('+cfg.get(section,'obsVar') + #
                            weight.GetName()+'*('+cfg.get(section,'obsVar')+#
                            ' > ' + str(bins[len(bins)-2])+')','goff')
            elif (model=="par1par2_TH2" or model=="par1par2_TF2"):
                sigObj.Draw(par2Name+':'+par1Name+' >> theBaseData_'+section+'_'+str(i),
#                            '('+weight.GetName()+'/64.4217490480265127)'+'*('+cfg.get(section,'obsVar')+#
#                            '('+weight.GetName()+'*'+efficiencies[i-1]+')'+'*('+cfg.get(section,'obsVar')+#
                            weight.GetName()+'*('+cfg.get(section,'obsVar')+#
                            ' > ' + str(bins[len(bins)-2])+')','goff')
            elif (model=="par1par2par3_TH3" or model=="par1par2par3_TF3"):
                sigObj.Draw(par3Name+':'+par2Name+':'+par1Name+' >> theBaseData_'+section+'_'+str(i),
                            weight.GetName()+'*('+cfg.get(section,'obsVar')+#
                            ' > ' + str(bins[len(bins)-2])+')','goff')
                

        if (model=="par1_TH1" or model=="par1_TF1"):
            func = TF1('bin_content_par1_'+str(i),func_string,
                       2*par1GridMin,2*par1GridMax)
        elif (model=="par1par2_TH2" or model=="par1par2_TF2"):
            func = TF2('bin_content_par1_par2_'+str(i),func_string,
                       par1GridMin,par1GridMax,
                       par2GridMin,par2GridMax)
        elif (model=="par1par2par3_TH3" or model=="par1par2par3_TF3"):
            func = TF3('bin_content_par1_par2_par3_'+str(i),func_string,
                       par1GridMin,par1GridMax,
                       par2GridMin,par2GridMax,
                       par3GridMin,par3GridMax)
       
        print range(nGridPar1Bins)
        for k in range(nGridPar1Bins+1):
#            theBaseData.SetBinError(k,0.0000021);
            print "bin"+str(k)+": ", theBaseData.GetBinContent(k), " +- ", theBaseData.GetBinError(k)
    
        func.SetLineColor(2)
        r = theBaseData.Fit(func,'R0S','')

        print "chi2: ", r.Chi2()
        print "par0: ", r.Parameter(0), "+-", r.ParError(0), " rel: ", r.ParError(0)/r.Parameter(0)
        print "par1: ", r.Parameter(1), "+-", r.ParError(1), " rel: ", r.ParError(1)/r.Parameter(1)
        print "par2: ", r.Parameter(2), "+-", r.ParError(2), " rel: ", r.ParError(2)/r.Parameter(2)
        covM = ROOT.TMatrixD(r.GetCorrelationMatrix())
        covM.Print()

        canv.cd(i)
        histos.append(TH1F(theBaseData))
        funcs.append(TF1(func))
#        histos[i-1].Draw("PIE")
        histos[i-1].Draw("E0 SAME")
        funcs[i-1].Draw("SAME")
        canv.Update()
        canv.SaveAs(section+"_hist_func.pdf")
    
#        getattr(ws,'import')(theBaseData)
        theBaseData.Write()

# use fitted yield in SM or generated as SM_yield to scale all inputs!
        if (model=="par1_TH1" or model=="par1_TF1"):
#            SM_yield=func.Eval(0.) # use fitted yield
            SM_yield=theBaseData.GetBinContent(theBaseData.FindBin(0.)) # use generated yield
        elif (model=="par1par2_TH2" or model=="par1par2_TF2"):
#            SM_yield=func.Eval(0.,0.)
            SM_yield=theBaseData.GetBinContent(theBaseData.FindBin(0.,0.))
        elif (model=="par1par2par3_TH3" or model=="par1par2par3_TF3"):
#            SM_yield=func.Eval(0.,0.,0.)
            SM_yield=theBaseData.GetBinContent(theBaseData.FindBin(0.,0.,0.))

        print "SM yield: ", SM_yield


        print "----> checking newframe input:"

        if (model=="par1_TH1"):
            for bin_x in range(1,nGridPointsForNewF+1):
                par1_value=newFormatInput.GetXaxis().GetBinCenter(bin_x)
                yield_bin=func.Eval(par1_value)
                newFormatInput.SetBinContent(bin_x,yield_bin)
        elif (model=="par1par2_TH2"):
            for bin_x in range(1,nGridPointsForNewF+1):
                for bin_y in range(1,nGridPointsForNewF+1):
                    par1_value=newFormatInput.GetXaxis().GetBinCenter(bin_x)
                    par2_value=newFormatInput.GetYaxis().GetBinCenter(bin_y)
                    yield_bin=func.Eval(par1_value, par2_value)
                    newFormatInput.SetBinContent(bin_x,bin_y,yield_bin)
        elif (model=="par1par2par3_TH3"):
            for bin_x in range(1,nGridPointsForNewF+1):
                for bin_y in range(1,nGridPointsForNewF+1):
                    for bin_z in range(1,nGridPointsForNewF+1):
                        par1_value=newFormatInput.GetXaxis().GetBinCenter(bin_x)
                        par2_value=newFormatInput.GetYaxis().GetBinCenter(bin_y)
                        par3_value=newFormatInput.GetZaxis().GetBinCenter(bin_z)
                        yield_bin=func.Eval(par1_value, par2_value, par3_value)
                        newFormatInput.SetBinContent(bin_x,bin_y,bin_z,yield_bin)

        if (model=="par1_TH1" or model=="par1par2_TH2" or model=="par1par2par3_TH3"):

            print " before scaling: read SM yield: ", newFormatInput.GetBinContent(newFormatInput.FindBin(0.,0.))
            print " scaling with SM yield: ",SM_yield
            newFormatInput.Scale(1./SM_yield)
            print "--->  after scaling: read SM yield: ", newFormatInput.GetBinContent(newFormatInput.FindBin(0.,0.))

            print 'model is TH -> write out TH object'
            newFormatInput.Write()

        elif (model=="par1_TF1" or model=="par1par2_TF2" or model=="par1par2par3_TF3"):
            print "  before scaling: read SM yield: ", func.Eval(0.)
            print " scaling with SM yield: ",SM_yield
            print " number of free parameters: ", func.GetNumberFreeParameters()
            for i2 in range (0,func.GetNumberFreeParameters()):
                print "par ",i2," -> ", func.GetParameter(i2)
                func.FixParameter(i2,func.GetParameter(i2)/SM_yield)
                print " ->par ",i2," -> ", func.GetParameter(i2)
            print "--->  after scaling: read SM yield: ", func.Eval(0.)
            func.Write()
        else:
            print ' have to select the model'

        canv2.cd(i)
        funcs_norm.append(TF1(func))
        histos_norm.append(theBaseData)
	histos_norm[-1].Divide(TF1('const',"1",par1GridMin,par1GridMax),SM_yield)
        #func = TF1('bin_content_par1_'+str(i),func_string,par1GridMin,par1GridMax)
        #funcs_norm[-1].SetRange(-25.,25.)
        funcs_norm[-1].SetRange(par1GridMin-par1PadSize,par1GridMax+par1PadSize)
        funcs_norm[-1].Draw()
        histos_norm[-1].Draw("SAME")
        canv2.Update()
        canv2.SaveAs(section+"_func_norm.pdf")


    outfile_newF.Close()

#raw_input("Press enter to continue...")
