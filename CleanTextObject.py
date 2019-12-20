# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:20:16 2018

@author: graeme
"""
####
#Assuming InitialiseLibraryAndImportText.py has been run
####

#replace unnecessary punctuation, keep period and apostrophe
alphanums = re.compile('[^a-z. \'A-Z0-9]')
data = alphanums.sub('',data)

#replace uppercase with lowercase
data = data.lower()
#fast regex routine to remove double spaces
data = re.sub(r'  ',' ',data)
#and remove 's
data = re.sub(r'\'s','',data)