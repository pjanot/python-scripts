

class Marker(dict):
    pass


class GoogleMap(object):

    def __init__(self):
        self.markers = []
        pass

    def addMarker(self, lat, lon, color): 
        self.markers.append( Marker( lat = lat, 
                                     lon = lon, 
                                     color = color )
                                     )
               
    def __str__(self):
        url = 'http://maps.googleapis.com/maps/api/staticmap?{parstr}'
        parameters = [ 
            'sensor=false',
            'size=512x512',
        # 'center=Sergy,France'
            ]
        if len(self.markers):
            marker_strings = [ 'markers=color:blue',
                               'label:C']
            for marker in self.markers:
                loc = '{lat:2.8},{lon:2.8}'.format( 
                    lat=marker['lat'],
                    lon=marker['lon'])
                marker_strings.append(loc)
            markstr = '|'.join(marker_strings)
            parameters.append(markstr) 
        else:
            parameters.append('center=Sergy,France')
        parstr = '&'.join(parameters)
        return url.format(parstr=parstr)


if __name__ == '__main__':

    import webbrowser

    map = GoogleMap()
    map.addMarker(40.7147282342, -73.9986722325, 'blue')
    print map
    browser = webbrowser.open( str(map) )
