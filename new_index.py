# This code will be designed to FTP into the sec.gov/edgar database 
# and get the daily updated  index file
 
# Information on SEC.gov ftp is available at:
# http://www.sec.gov/edgar/searchedgar/ftpusers.htm



# importing

import os

import datetime

import sys

from ftplib import FTP



# setting up the program to check for the date in the format that SEC.gov/edgar formats them

filedate = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')




# The documents are in the format of form.YYYYMMDD.IDX 

# so now time = YYYYMMDD



# I now define a variable newfile to be the title of the document of the day

newfile = 'form.' + filedate + '.idx'


# Testing newfile

print(newfile + ' should be yesterday right?')


# Getting connected

# Establish a connection to the server at: (fpt.http://www.sec.gov/edgar/daily-index) 
# and/or ftp.http://www.sec.gov/edgar/full-index via FTP

# log in as user "anonymous," using your electronic mail address as the password

# defining and connecting to edgar with credentials

ftp = FTP('ftp.sec.gov')
ftp.login('anonymous','michael@hdnfl.com')

print('FTP session now open with ftp.sec.gov')


# change to the correct directory
ftp.cwd('/edgar/daily-index/')

print('The current directory is now ftp.sec.gov/edgar/daily-index/')


# open local file so that we can copy data to it
local = open(newfile, 'wb')


# If our new index is in the files listed. this should download it and tell us.

#
# This if loop does not save the file.
#

            
if newfile in ftp.nlst():
        ftp.retrbinary('RETR %s' % newfile, local.write) and print (newfile + ' has been downloaded')
else:
        print ('It is either a weekend or stock holiday. No index document was released today')

# Close the local file
local.close()

# Close the connection
ftp.quit()

print ('ftp is now closed')
