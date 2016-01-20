import urllib2
from bs4 import BeautifulSoup
import csv

url = ('http://nflcombineresults.com/nflcombinedata.php?year=2000&pos=&college')

page = urllib2.urlopen(url).read()

soup = BeautifulSoup(page,"html.parser")
table = soup.find('table')
#print table.prettify()
#print table.find('tr')
f = csv.writer(open("2000scrape.csv", "w"))
f.writerow(["Name", "Position", "Height", "Weight", "40-yd", "Bench", "Vertical", "Broad", "Shuttle", "3-Cone"])
# variable to check length of rows
x = (len(table.find('tr')) - 1)
# set to run through x
for row in table.find('tr'):
  
        col = row.find('td')
        name = col[1].getText()
        position = col[3].getText()
        height = col[4].getText()
        weight = col[5].getText()
        forty = col[7].getText()
        bench = col[8].getText()
        vertical = col[9].getText()
        broad = col[10].getText()
        shuttle = col[11].getText()
        threecone = col[12].getText()
        player = (name, position, height, weight, forty, bench, vertical, broad, shuttle, threecone, )
        f.writerow(player)
   
        
