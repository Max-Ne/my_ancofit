import sys

import ROOT
from ROOT import *

inputFileName = sys.argv[3]
minmax = [float(sys.argv[1]),float(sys.argv[2])]
parm = sys.argv[4]
file = TFile.Open(inputFileName,'READ')
limit = file.Get('limit')

nEntries = limit.GetEntries()-1

histo = TH1F('LLHscan','',nEntries,minmax[0],minmax[1])
#limit.Draw("fs0 >> LLHscan","deltaNLL",'goff')
limit.Draw(parm+" >> LLHscan","deltaNLL",'goff')

minBin = histo.GetMinimumBin()
minBinCenter = histo.GetBinCenter(minBin)
minVal = histo.GetBinContent(minBin)

#print 'Found profile-likelihood minimum value %.3f at %.3f'%(minVal,minBinCenter)
#skip best fit value which is entry 0
bounds68 = []
bounds95 = []
bounds99 = []
lastBelowErr68 = False
lastAboveErr68 = True
lastBelowErr95 = False
lastAboveErr95 = True
lastBelowErr99 = False
lastAboveErr99 = True

for i in xrange(nEntries):
    limit.GetEntry(i+1)
    NLL = limit.GetLeaf("deltaNLL").GetValue()
    if NLL - minVal <= 0.5:
        if lastAboveErr68:
            bounds68.append([])
            bounds68[-1].append(limit.GetLeaf(parm).GetValue())
        lastBelowErr68 = True
        lastAboveErr68 = False
    else:
        if lastBelowErr68:
            bounds68[-1].append(limit.GetLeaf(parm).GetValue())
        lastBelowErr68 = False
        lastAboveErr68 = True
    if NLL - minVal <= 1.92:
        if lastAboveErr95:
            bounds95.append([])
            bounds95[-1].append(limit.GetLeaf(parm).GetValue())
        lastBelowErr95 = True
        lastAboveErr95 = False
    else:
        if lastBelowErr95:
            bounds95[-1].append(limit.GetLeaf(parm).GetValue())
        lastBelowErr95 = False
        lastAboveErr95 = True
    if NLL - minVal <= 3.32:
        if lastAboveErr99:
            bounds99.append([])
            bounds99[-1].append(limit.GetLeaf(parm).GetValue())
        lastBelowErr99 = True
        lastAboveErr99 = False
    else:
        if lastBelowErr99:
            bounds99[-1].append(limit.GetLeaf(parm).GetValue())
        lastBelowErr99 = False
        lastAboveErr99 = True

file.Close()

print bounds68, bounds95, bounds99

#boundstext68 = ['[%.3g,%.3g]'%(b[0],b[1]) for b in bounds68]
#boundstext95 = ['[%.3g,%.3g]'%(b[0],b[1]) for b in bounds95]
#boundstext99 = ['[%.3g,%.3g]'%(b[0],b[1]) for b in bounds99]
#print '68% CL Limit:','U'.join(boundstext68)
#print '95% CL Limit:','U'.join(boundstext95)
#print '99% CL Limit:','U'.join(boundstext99)

#print 'U'.join(boundstext68)
#print 'U'.join(boundstext95)
#print 'U'.join(boundstext99)

