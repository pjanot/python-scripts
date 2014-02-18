from twitter_stream import *

keywords = [
    '@F_Desouche',
    'Fdesouche',
    '@FrDesouche',
    '#FN', 
    '#marinelepen',
    'ElyseeMarine', 
    'Philippot',
    '#LePen',
    '#Gollnisch',
    '#BrunoSubtil',
    'BleuMarine',
    ] 

tweets, df = init_stream( ','.join(keywords), language='fr')  
