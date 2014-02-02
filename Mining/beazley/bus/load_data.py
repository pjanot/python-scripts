
import glob
import gzip
import xml.etree.ElementTree as ET
import pprint
from collections import namedtuple


class BusTimeLine( dict ):
    
    def __init__(self, id):
        self.id = id
        self.buses = {}

    def addBus(self, bus):
        if bus.id != self.id: 
            raise ValueError('cannot add a different bus to a BusTimeLine')
        self[bus.time] = bus

    def positions(self):
        return [ (bus.lat, bus.lon) for bus in self.values() ]
            
Bus = namedtuple('Bus', ['time','id','direction', 'lat', 'lon'])

class TimeLine( dict ):
    '''Stores each bus in a BusTimeLine'''
    def __init__(self, snapshots): 
        for sh in snapshots:
            for bus in sh.buses.values():
                self.setdefault(bus.id, 
                                BusTimeLine(bus.id)).addBus( bus )


    
class SnapShot( object ):
    
    def __init__(self, etree ):
        self.etree = etree
        self.time = etree.find('time').text
        self.buses = {}
        # self.timelines = {}
        for bustree in etree.iter('bus'):
            bus = Bus(
                time = self.time,
                id = bustree.find('id').text, 
                direction = bustree.find('d').text, 
                lat = bustree.find('lat').text,
                lon = bustree.find('lon').text,
                )
            self.buses[bus.id] = bus 
            # self.timelines.setdefault(bus.id, BusTimeLine(bus.id)).addBus( bus )
            
    def __str__(self):
        timeline = ''.join(['time:  ', self.time])
        buslines = '\n'.join( (str(bus) for bus in self.buses.values()) )
        return '\n'.join( [timeline, buslines] ) 
           
           
def get_xml_data(filename):
    print 'processing', filename
    f = gzip.open(filename, 'rb')
    try: 
        tree = ET.parse(f)
        root = tree.getroot()
        f.close()
        return root    
    except ET.ParseError: 
        print 'Warning: cannot parse', filename
        raise
    

def process_file( filename ):
    root = get_xml_data(filename)
    snapshot = SnapShot( root ) 
    return snapshot 


if __name__ == '__main__':

    from Google.googlemap import GoogleMap 

    import sys 
    import shelve

    test = True
    ndata_files = -1
    if test:
        ndata_files = 5
    
    
    timeline = None
    if len(sys.argv)==1:
        data_dir = 'data'
        data_files = glob.glob('/'.join([data_dir, '*.xml.*']))
        snapshots = list()
        
        for f in data_files[:ndata_files]:
            try: 
                snapshots.append( process_file(f) ) 
            except ET.ParseError: 
                pass
        timeline = TimeLine(snapshots)
        bak = shelve.open('timeline.bak')
        bak['timeline'] = timeline
        bak.close() 
        
    map = GoogleMap()
    # import pdb; pdb.set_trace()
    bustimeline = timeline.values()[0]
    if not test:
        bustimeline = timeline['1380']
    for lat, lon in bustimeline.positions():
        map.addMarker(lat, lon, 'blue')

    print map 
    print len( str(map) )
    
