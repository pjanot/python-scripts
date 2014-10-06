import os, sys

from ROOT import gROOT, TFile, TCanvas, gPad, TBrowser, TH2F, TH1F, TH1D , TProfile, TLegend

gROOT.Macro( os.path.expanduser( '~/rootlogon.C' ) )

# adding current directory in PYTHONPATH
sys.path.append('.')

filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    exec(open(filename).read())
