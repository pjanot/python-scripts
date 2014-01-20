import glob
import os 
import markup
import operator
from markup import oneliner as e

def allowedType(fname, types):
    n, ext = os.path.splitext(fname)
    return ext in types

def split(sequence, size):
    for i in xrange(0, len(sequence), size):
        yield sequence[i:i+size] 


class File(str):
    def __new__(cls,*args,**kw):
        return str.__new__(cls,*args,**kw)

    def __init__(self, fname):
        if not allowedType(fname, self.__class__.TYPES):
            raise ValueError('Type not allowed for file'+fname)

class Image(File):
    TYPES = ['.png', '.jpg']

class TextFile(File):
    TYPES = ['.txt', '.tex']


        
class Directory(object):
    '''Can contain other directories, images, and an index.html'''

    def __init__(self, path, title=None):
        print 'creating directory', path

        # page parameters
        self.title = path
        self.header = ''
        self.footer = ''
        self.css = ['default.css']
        self.nimagesperrow = 3

        self.path = path
        self.images = []
        self.textFiles = []
        self.subdirs = []
        self.HTML = None
        self._addImages()
        self._addTextFiles()
        self._addDirs()
        self._addHTML()

        # print self

    def _addImages(self):
        '''Add all images in this directory'''
        for imgnam in os.listdir(self.path):
            img = None
            try:
                img = Image(imgnam)
            except ValueError:
                continue
            self.images.append(img)

    def _addTextFiles(self):
        '''Add all text files in this directory'''
        for filenam in os.listdir(self.path):
            txt = None
            try:
                txt = TextFile(filenam)
            except ValueError:
                continue
            self.textFiles.append(txt)
        
    def _addDirs(self):
        '''Add all directories in this directory'''
        self.subdirs = []
        for sub in os.listdir(self.path):
            subfullname = '/'.join([self.path, sub])
            if os.path.isdir(subfullname):
                self.subdirs.append( Directory(subfullname) ) 
    
    def _addHTML(self):
        '''Add index.html'''
        index = open('/'.join([self.path,'index.html']), 'w')
        index.write( str(self) + '\n')
        index.close()
        

    def __str__(self):
        page = markup.page( )
        page.init(
            title=self.title, 
            css=self.css, 
            header=self.header, 
            footer=self.footer
            )
        
        page.h1(self.title)

        # subdirectory section
        if len(self.subdirs):
            links = []
            for s in sorted(self.subdirs, key=operator.attrgetter('path')):
                print s.path
                base = os.path.basename(s.path)
                link = e.a(base,
                           href='/'.join([base, 'index.html']))
                links.append(link)
            page.h2('Subdirectories:')
            page.ul( class_='mylist' )
            page.li( links, class_='myitem' )
            page.ul.close()

        #text files
        for txt in self.textFiles:
            page.h2(txt)
            textfile = open('/'.join([self.path, txt]))
            page.p( '\n'.join(textfile.readlines() ) )
            textfile.close()

        #plots
        size = 100/self.nimagesperrow - 1
        if len(self.images):
            page.h2('Plots')
            for rimgs in split(sorted(self.images), self.nimagesperrow):
                page.img( src=rimgs, width='{size}%'.format(size=size),
                          alt=rimgs)
                page.br()
        return str(page)



    
if __name__ == '__main__':

    import sys

    from optparse import OptionParser
    
    parser = OptionParser()
    parser.usage = '''
    %prog <input directory>

    Adds web pages to the input directory, and its subdirectories.
    all pdb images will be added to the pages.

    Example: just run

    python DirectoryTree.py templates
    '''
    opt, args = parser.parse_args()
    if len(args)!=1:
        parser.print_usage()
        print 'provide the input directory'

    idir = args[0]

    dir = Directory(idir)
