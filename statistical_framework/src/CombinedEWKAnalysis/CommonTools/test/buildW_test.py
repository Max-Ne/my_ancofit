#!/usr/bin/env python2

import pyroot_logon
import limits
import os
import sys

from array import *

from ROOT import *
from optparse import OptionParser
from ConfigParser import SafeConfigParser

parser = OptionParser(description="%prog : A blablabla", usage="blub --config=blubblub")
cfgparse = SafeConfigParser()

parser.add_option("--config",dest="config",help="The name of the input configuration file.")
(options,args) = parser.parse_args()

miss_options = False

if options.config is None:
  print 'Need to specify --config'
  miss_options=True

if miss_options:
  exit(1)

cfgparse.read(options.config)
options.config = cfgparse

cfg = options.config # cfg is now our configfile

fit_sections = cfg.sections()

signalModel='-1'
signalModel=cfg.get('Global','model')
print 'modelName= ',signalModel

fit_sections.remove('Global') #don't need to iterate over the global configuration


Ndim=0
if ( signalModel == 'par1_TF1'):
  Ndim=1
  print 'yay'
elif (signalModel == 'TF123'):
  Ndim=1
  print 'ok'
else:
  raise RuntimeError('InvalidCouplingChoice %s'%signalModel, 'We can only use ...!')

par1name = ''
par2name = ''
par3name = ''

cfg_items=cfg.items('Global')
for cfg_item in cfg_items:
    if 'par1name' in cfg_item:
        par1name = cfg.get('Global','par1name')
    if 'par2name' in cfg_item:
        par2name = cfg.get('Global','par2name')
    if 'par3name' in cfg_item:
        par3name = cfg.get('Global','par3name')
    if 'nlnn' in cfg_item:
        NlnN = int(cfg.get('Global','nlnn'))

#print par1name, par2name, par3name

lnN_name = []
for i in range(1,NlnN+1):
    lnN_name.append(cfg.get('Global','lnN%i_name'%i))
lnN_value = []
for i in range(0,NlnN):
    lnN_value.append([])
    for value in cfg.get('Global','lnN%i_value'%(i+1)).split(','):
        lnN_value[i].append(value)


lnN_for = []
for i in range(0,NlnN):
    lnN_for.append([])
    for name in cfg.get('Global','lnN%i_for'%(i+1)).split(','):
        lnN_for[i].append(name)

#print '\n\t\t=============================================> lnN: ',lnN_name
#print 'lnN value: ',lnN_value
#print 'lnN for: ',lnN_for

if Ndim == 1:
    par1low  = float(cfg.get('Global', 'par1Low'))
    par1high = float(cfg.get('Global', 'par1High'))
elif Ndim == 2:
    par1low  = float(cfg.get('Global', 'par1Low'))
    par1high = float(cfg.get('Global', 'par1High'))
    par2low  = float(cfg.get('Global', 'par2Low'))
    par2high = float(cfg.get('Global', 'par2High'))

else:
    print 'Only dimensions 1, 2 and 3 implemented... this thing will crash.'

#print par1low, par1high

NSigBkg_corr_unc_int=0

basepath = '%s/src/CombinedEWKAnalysis/CommonTools/data/anomalousCoupling'%os.environ['CMSSW_BASE']

for section in fit_sections:
  codename = section
  lType = codename
  print codename
  
#  f = TFile('%s/%s.root'%(basepath,codename))

  print '%s/%s.root'%(basepath,codename)

  
  Nbkg = cfg.get(codename,'Nbkg')
  print "Nbkg= ",Nbkg
  Nbkg_int=int(Nbkg)

  bkg_name = []
  for i in range(1,Nbkg_int+1):
    bkg_name.append(cfg.get(codename,'bkg%i_name'%i))

  background_shapeSyst = []
  for i in range(0,Nbkg_int):
    background_shapeSyst.append([])
    cfg_items=cfg.items(codename)
    for cfg_item in cfg_items:
      if ('bkg%i_shape_syst'%(i+1) in cfg_item):
        for name in cfg.get(codename,'bkg%i_shape_syst'%(i+1)).split(','):
          background_shapeSyst[i].append(name)

  print bkg_name
  print background_shapeSyst

  # get bkg from file
#  background = []
#  for i in range(0,Nbkg_int):
#    background.append(f.Get(bkg_name[i]))

  # get bkg shapes from file
#  background_backshapeUp = []
#  background_backshapeDown = []
#  for j in range(0,Nbkg_int):
#    background_backshapeUp.append([])
#    background_backshapeDown.append([])
#    for i in range(0,len(background_shapeSyst[j])):
#      background_backshapeUp[j].append(f.Get('%sUp'%background_shapeSyst[j][i]))
#      background_backshapeDown[j].append(f.Get('%sDown'%background_shapeSyst[j][i]))
 





