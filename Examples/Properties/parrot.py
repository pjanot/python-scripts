class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        print 'setting voltage to', value
        self._voltage = value
        
p = Parrot()


class Parrot2(object):
    def __init__(self):
        self._voltage = 100000

    voltage = property()
