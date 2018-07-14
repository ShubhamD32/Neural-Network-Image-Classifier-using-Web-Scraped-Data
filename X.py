from bs4 import BeautifulSoup
import urllib
import os
from urllib import urlretrieve,urlopen
import random
name = 5
# Make directory to save images according to search term
def MakeFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error creating directory : ' + directory)


def GetImages(searchTerm):

    # Generate Search URL for Yahoo image search
    baseURL = "https://images.search.yahoo.com/search/images?p="
    fullURL = "https://in.images.search.yahoo.com/search/images?p=%s&ei=UTF-8&save=0" % searchTerm

    # Search_URL= "https://images.search.yahoo.com/search/images?p=" + inp

    # Parsing HTML from download link
    html_page = urlopen(fullURL)
    soup = BeautifulSoup(html_page, "html.parser")
    imagesURL = []

    i = 0       # alternate results show 'None', skipping them
    for img in soup.findAll('img'):
        i = i + 1
        if (i%2 == 0):
            imagesURL.append(img.get('src'))


    print('Following Images (URLs) were retrieved\n')
    print(imagesURL)


    savedImgsPath = './' + searchTerm + '/'     # directory structure to save images of searched term
    MakeFolder(savedImgsPath)                   # make   directory mentioned above

    for image in imagesURL:
           name = random.randrange(1,1000)
           name = str(name)
           name = name + ".jpeg"
           urlretrieve(image, os.path.join(savedImgsPath, os.path.basename(name)))



# Program Starts Here
searchTerm = input("Enter the search term : ")
GetImages(searchTerm)


