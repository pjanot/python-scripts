#!/usr/bin/python
# FileName: Subsampling.py 
# Version 1.0 by Tao Ban, 2010.5.26
# This function extract all the contents, ie subject and first part from the .eml file 
# and store it in a new file with the same name in the dst dir. 

import email 
import os, sys, stat
import shutil

def extract(filename):
	''' Extract the subject and payload from the .eml file.
	
	'''
	if not os.path.exists(filename): # dest path doesnot exist
		print "ERROR: input file does not exist:", filename
		os.exit(1)
	fp = open(filename)
	msg = email.message_from_file(fp)
	payload = msg.get_payload()
	if type(payload) == type(list()) :
		payload = payload[0] # only use the first part of payload
	sub = msg.get('subject')
	sub = str(sub)
	if type(payload) != type('') :
		payload = str(payload)
	output = dict(
		body = payload,
		sub = sub,
		filename = filename
		)
	return output

def process_dir( srcdir ):
	'''Extract the body information from all .eml files in the srcdir and 
	
	save the file to the dstdir with the same name.'''
	files = os.listdir(srcdir)
	contents_all_mails = []
	print 'extracting from', srcdir
	for ifile, file in enumerate(files):
		nf = ifile+1
		if nf%100==0:
			print nf
		srcpath = os.path.join(srcdir, file)
		src_info = os.stat(srcpath)
		if stat.S_ISDIR(src_info.st_mode): # for subfolders, recurse
			extract(srcpath, dstpath)
		else:  # copy the file
			contents_mail = extract(srcpath)
			contents_all_mails.append(contents_mail)
	return contents_all_mails

def load_labels( labelfilename ):
	fp = open(labelfilename)
	labels = dict()
	for line in fp:
		label, emlfnam = line.split()
		labels[ emlfnam ] = int( label )
	return labels

def label( all_mails, labels ):
	for mail in all_mails:
		fnam = os.path.basename( mail['filename'] ) 
		label = labels[ fnam ]
		mail['label'] = label


if __name__ == '__main__':

	import shelve
	
	args = sys.argv[1:]
	if len(args)!=2:
		print 'usage ExtractContent.py <email source dir> <labels file>'
	srcdir = args[0]
	labelfilename = args[1] 
	if not os.path.exists(srcdir):
		print 'The source directory %s does not exist, exit...' % (srcdir)
		sys.exit()

	labels = load_labels( labelfilename )
	all_mails = process_dir( srcdir ) 
	label( all_mails, labels ) 

	shlf = shelve.open('output.dat')
	shlf['mails'] = all_mails
	shlf.close()

	# might want to parse html to get plain text
	# and to keep the info about html formatting! 
