from urllib.parse import urlparse
from html.parser import HTMLParser
import os
import re
import requests
from bs4 import BeautifulSoup

                
import requests
from bs4 import BeautifulSoup
import langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter



link='https://www.americares.org/emergency-program/war-in-ukraine/#:~:text=On%20the%20morning%20of%20February,The%20deadly%20conflict%20continues%20unabated.'


#scrape for p tags


response=requests.get(link)
html=response.text

soup = BeautifulSoup(html)
text=soup.get_text()

text_split=RecursiveCharacterTextSplitter(
    chunk_size=700,chunk_overlap=0,length_function=len
)

chunks=text_split.split_text(text)

        
        
    