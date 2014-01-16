from math import log

def y_fun(x, y0, m):
    y = y0 * pow(m, x)
    if y < 0.5: y = 0.5
    return y

def x_fun(y, y0, m):
    return (log(y) - log(y0))/log(m)

def history(scen, xmax):
    coeff = scen['coeff_start']
    total = 0. 
    for y in range(0,xmax):
        mod = scen['coeff']
        if coeff<0.5: 
            coeff = 0.5
        total += coeff
        print y, mod, coeff, total
        coeff *= mod
    

if __name__ == '__main__':
    from optparse import OptionParser
    import sys
    import pprint 

    if len(sys.argv) != 3:
        print 'donner le cout du sinistre'
        sys.exit(1)
    
    sinistre, scen_id = sys.argv[1:]

    data = dict(
        malusf = 1.25,
        bonusf = 0.95,
        coeff_limits = (0.5, 3.5), 
        franchise = 115.,
        cotisation = 679.,
        sinistre = sinistre )

    pprint.pprint( sorted(data.iteritems()) )

    scenarios = [
        dict(coeff_start=0.6, 
             coeff = data['bonusf']),
        dict(coeff_start=0.6 * data['malusf'], 
                  coeff = data['bonusf'])
                  ]
    
    scen = scenarios[ int(scen_id) ]
    
    coeff = scen['coeff_start']
    total = 0. 
    
