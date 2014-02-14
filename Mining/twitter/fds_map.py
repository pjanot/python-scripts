from twitter_stream import *

keywords = [
    '@F_Desouche',
    'Fdesouche',
    '@FrDesouche',
    '#FN', 
    '#marinelepen',
    'ElyseeMarine', 
    'Philippot',
    ] 

tweets, df = init_stream( ','.join(keywords) )  
