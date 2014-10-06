import time
cur_year = time.localtime().tm_year

class Appliance(object):
    def __init__(self, name, year, price, vetuste=0.9):
        self.name = name
        self.year = year
        self.price = price
        self.vetuste = vetuste

    def value(self):
        return self.price * (self.vetuste**(cur_year-self.year))


salon = [
    Appliance("television", 2009, 1500.),
    Appliance("dac", 2014, 400.),
    Appliance("ampli", 2009, 2000.),
    Appliance("cd", 2009, 600.),
    Appliance("ordi", 2010, 1000.),
    Appliance("bluray", 2013, 90.),
    Appliance("canape", 2014, 3000, 1.),
    Appliance("clic_clac", 2010, 1600, 1.),
    Appliance("table_salon", 2010, 300, 1.),
    Appliance("photo_boitier", 2011, 650),
    Appliance("photo_50", 2011, 125),
    Appliance("photo_105", 2011, 800),
    Appliance("photo_tokina", 2011, 700),
    Appliance("musique_seagull", 2012, 700, 1.),
    Appliance("musique_ampli", 2012, 700, 1.),
    Appliance("musique_strat", 2012, 1500, 1.),
    Appliance("cds", 2011, 200*10, 1.),
    Appliance("bds", 2012, 300*12, 1.),
    ]


cuisine = [
    Appliance("table", 2014, 450., 1),
    Appliance("desserte", 2014, 250., 1),
    Appliance("frigo", 2014, 600.),
    Appliance("lave_vaisselle", 2014, 800.),
    Appliance("micro_ondes", 2010, 100.),
   ]

cellier = [
    Appliance("congelateur", 2013, 500.),
    Appliance("machine_laver", 2004, 400.),
    ]

cellier = [
    Appliance("scie_circulaire", 2012, 400.),
    Appliance("scie_sauteuse", 2013, 200.),
    Appliance("lamelleuse", 2014, 300.),
    Appliance("rabot", 2013, 200.),
    Appliance("tondeuse", 2014, 100.),
    Appliance("debroussailleuse", 2014, 400.),
    ]

chambre = [
    Appliance("matelas", 2005, 500.),
    Appliance("vetements_colin", 2010, 4000.),
    Appliance("vetements_maud", 2010, 2000.),
    ]

all = []
all.extend(salon)
all.extend(cuisine)
all.extend(cellier)
all.extend(chambre)

if __name__ == "__main__":
    print sum( [app.value() for app in all] )
