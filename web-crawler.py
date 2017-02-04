#making of a web crawler by abhishektiwari981996
#github id abhishek981996
#Lets do it 
#Step 1 :searching in a given website


import urllib
import re
from bs4 import BeautifulSoup

class Find:
    def open(self,url):
        page = urllib.urlopen(url).read()
        return page

    def find(self,word,page):
        list = re.findall(word, page)
        return list

    def Find_link(self,html):
        soup = BeautifulSoup(html,"html.parser")
        links = []
        
        for link in soup.find_all('a',attrs={'href': re.compile("^http://")}):
            links.append(link.get('href'))

        return links


def Main(url,word):
    Http_page_object = Find()
    found = False
    while found==False:
        print(">>////>>  visiting %s") %url
        Http_page = Http_page_object.open(url)
        link = Http_page_object.Find_link(Http_page)

        word_found = Http_page_object.find(word,Http_page)
        if word_found:
            place = Http_page.find(word)
            print ("%s found at place %s")% (word,place)
            print("\nword found in the page %s")%url
            found = True
        else:
            for i in link:
                print(">>////>>  visiting %s") %i
                page = Http_page_object.open(i)
                word_found_link = Http_page_object.find(word,page)
                if word_found_link:
                    place = page.find(word)
                    print ("%s found at place %s in page %s")% (word,place,i)
                    found = True
                    break
                print("Success")
            if found== False:
                print("%s word not found")%word
                found= True




if __name__ == '__main__':
    print("enter the word you want to search:")
    lib = raw_input()
    print("enter the site from which you want to search:")
    site = raw_input()
    Main(str(site),str(lib))