
from bs4 import BeautifulSoup
import requests
import subprocess

page = requests.get('http://www.tagesschau.de')
soup = BeautifulSoup(page.content, 'html.parser')


content2 = soup.select('a')
news_list = []
    

for i in content2:
    soup2 = BeautifulSoup(str(i), 'html.parser')

    dachzeile = ''
    for j in soup2.find_all('p', class_='dachzeile'):
        dachzeile = j.get_text() + ". "
    if (dachzeile == ''):
        for j in soup2.find_all('span', class_='dachzeile'):
            dachzeile = j.get_text() + ". "
            
    title = ''
    for j in soup2.select('h4'):
        title = j.get_text() + ". "
        
    teaser = ''
    for j in soup2.find_all('p', class_='teasertext'):
        teaser = j.get_text() + ". "
        teaser = teaser[0:teaser.find('\n')]
        teaser = teaser[0:teaser.find('|')]
    if (teaser == ''):
        for j in soup2.find_all('span', class_='teasertext'):
            teaser = j.get_text() + ". "
            teaser = teaser[0:teaser.find('\n')]
            teaser = teaser[0:teaser.find('|')]
    
    if (title != ''):
        news_list.append(dachzeile + '\n' + title + '\n' + teaser + '\n')

for i in range(10):
    subprocess.call('espeak -v \\mb\\mb-de2 -s 150 "' + news_list[i] +'"', shell=True)
