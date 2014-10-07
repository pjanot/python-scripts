from ROOT import kBlack, TPaveText, TText

def officialStyle(style):
    style.SetCanvasColor (0)
    style.SetCanvasBorderSize(10)
    style.SetCanvasBorderMode(0)
    style.SetCanvasDefH (700)
    style.SetCanvasDefW (700)
    style.SetCanvasDefX (100)
    style.SetCanvasDefY (100)
    # color palette for 2D temperature plots
    # style.SetPalette(1,0)
    # Pads
    style.SetPadColor (0)
    style.SetPadBorderSize (10)
    style.SetPadBorderMode (0)
    style.SetPadBottomMargin(0.13)
    style.SetPadTopMargin (0.08)
    style.SetPadLeftMargin (0.17)
    style.SetPadRightMargin (0.05)
    style.SetPadGridX (0)
    style.SetPadGridY (0)
    style.SetPadTickX (1)
    style.SetPadTickY (1)
    # Frames
    style.SetLineWidth(3)
    style.SetFrameFillStyle ( 0)
    style.SetFrameFillColor ( 0)
    style.SetFrameLineColor ( 1)
    style.SetFrameLineStyle ( 0)
    style.SetFrameLineWidth ( 2)
    style.SetFrameBorderSize(10)
    style.SetFrameBorderMode( 0)
    # Histograms
    style.SetHistFillColor(2)
    style.SetHistFillStyle(0)
    style.SetHistLineColor(1)
    style.SetHistLineStyle(0)
    style.SetHistLineWidth(3)
    style.SetNdivisions(505)
    # Functions
    style.SetFuncColor(1)
    style.SetFuncStyle(0)
    style.SetFuncWidth(2)
    # Various
    style.SetMarkerStyle(20)
    style.SetMarkerColor(kBlack)
    style.SetMarkerSize (1.4)
    style.SetTitleBorderSize(0)
    style.SetTitleFillColor (0)
    style.SetTitleX (0.2)
    style.SetTitleSize (0.055,"X")
    style.SetTitleOffset(1.100,"X")
    style.SetLabelOffset(0.005,"X")
    style.SetLabelSize (0.050,"X")
    style.SetLabelFont (42 ,"X")
    style.SetStripDecimals(False)
    style.SetLineStyleString(11,"20 10")
    style.SetTitleSize (0.055,"Y")
    style.SetTitleOffset(1.60,"Y")
    style.SetLabelOffset(0.010,"Y")
    style.SetLabelSize (0.050,"Y")
    style.SetLabelFont (42 ,"Y")
    style.SetTextSize (0.055)
    style.SetTextFont (42)
    style.SetStatFont (42)
    style.SetTitleFont (42)
    style.SetTitleFont (42,"X")
    style.SetTitleFont (42,"Y")
    style.SetOptStat (0)

def CMSPrelim(lowX=0.17, lowY=0.94):
    cmsprel = TText(lowX, lowY, "CMS")
    cmsprel.SetNDC(True)
    cmsprel.SetTextFont ( 62 )
    return cmsprel

class HistStyle:
    def __init__(self,
                 markerStyle = 8,
                 markerColor = 1,
                 markerSize = 1,
                 lineStyle = 1,
                 lineColor = None,
                 lineWidth = 2,
                 fillColor = None,
                 fillStyle = 0 ):
        self.markerStyle = markerStyle
        self.markerColor = markerColor
        self.markerSize = markerSize
        self.lineStyle = lineStyle
        if lineColor is None:
            self.lineColor = markerColor
        else:
            self.lineColor = lineColor
        self.lineWidth = lineWidth
        self.fillColor = fillColor
#        if fillColor is None:
#            self.fillColor = lineColor
#        else:
#            self.fillColor = fillColor
        self.fillStyle = fillStyle

    def format( self, hist):
        hist.SetMarkerStyle( self.markerStyle )
        hist.SetMarkerColor( self.markerColor )
        hist.SetMarkerSize( self.markerSize )
        hist.SetLineStyle( self.lineStyle )
        hist.SetLineColor( self.lineColor )
        hist.SetLineWidth( self.lineWidth )
        if self.fillColor is not None:
            hist.SetFillColor( self.fillColor )
        hist.SetFillStyle( self.fillStyle )

traditional = HistStyle(markerColor=4, markerStyle=21)
pf = HistStyle(markerColor=2)

if __name__ == "__main__":

    from ROOT import gStyle, TH1F, gPad, TLegend

    officialStyle(gStyle)
    h = TH1F("h", "; p_{T} (GeV); a.u.", 10, -5, 5)
    h.Sumw2()
    h.FillRandom("gaus", 1000)
    h.Draw()
    pf.format(h)

    h2 = TH1F("h2", "; p_{T} (GeV); a.u.", 10, -5, 5)
    h2.Sumw2()
    h2.FillRandom("gaus", 500)
    h2.Draw("same")
    traditional.format(h2)

    legend = TLegend(0.67, 0.71, 0.92, 0.89)
    legend.AddEntry(h, "PF")
    legend.AddEntry(h2, "Traditional")
    legend.Draw()
     
    cmsprel = CMSPrelim()
    cmsprel.Draw()

    gPad.Update()
