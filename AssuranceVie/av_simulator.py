
if __name__ == '__main__':
    from optparse import OptionParser
    import sys

    banque = sys.argv[1]

    maif = dict(
        ini_fr = 0.024,
        reg_fr = 0.022,
        ges_fr = 0.0,
        taux = 0.04,
        )

    banque_postale = dict(
        ini_fr = 0.01,
        reg_fr = 0.025,
        ges_fr = 0.0095,
        taux = 0.03,
        )


    ini_dep = 100000.
    reg_dep = 100.
    annees = 8
    abattement = 9200.

    verbose = False
    # data = banque_postale
    # data = maif

    if ini_dep>=50000.:
        # remise sur les frais au dela de 50000 euros a la banque postale
        banque_postale['ini_fr'] = 0.005

    data = locals()[banque]

    capital = ini_dep * (1- data['ini_fr'])
    interets = 0
    versements = ini_dep
    print 'initial, capital=', capital, 'frais=', -ini_dep*data['ini_fr']
    for ia in range(annees):
        ia +=1
        print '-'*20
        for im in range(12):
            capital += reg_dep * (1-data['reg_fr'])
            versements += reg_dep
            if verbose: print 'mois', im, 'capital=', capital
        #calcul des frais
        fr_y = capital * data['ges_fr']
        capital -= fr_y
        # print 'annee', ia, 'capital=', capital, 'gestion=',fr_y, 'interets=',interets
        #calcul des interets
        interets_y = capital * data['taux']
        interets += interets_y
        capital += interets_y
        print 'annee', ia, 'capital=', capital, 'versements=', versements, 'frais=',-fr_y, 'int_y=',interets_y, 'interets=', interets
