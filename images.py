from bs4 import BeautifulSoup
import random
import urllib
import re
import urllib3
import shutil
#Randomise file names
import os
import urllib3
import urllib2

import os








name = random.randrange(1,100000)
HT = urllib3.PoolManager()



#Get search term
inp=input("Enter")

# Make directory according to search term

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

filePath =  r"./" + inp + "/"
createFolder(filePath)






#Generate Search URL for Yahoo image search

BaseURL = "https://images.search.yahoo.com/search/images?p="
Full_URL = BaseURL + inp

#Search_URL= "https://images.search.yahoo.com/search/images?p=" + inp

#Parsing HTML from download link

html_page = urllib2.urlopen(Full_URL)
soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images)


#Dumping URLs in a text file
f1 = open("A","w")

for item in images:
    f1.write("%s\n" % item)

#Removing Null enrties from text file
f1=open("A","r")
f2=open("B","w")
i=0
while(f1):
    str = f1.readline()
    i=i+1
    if i%2==0:
        f2.write(str)


