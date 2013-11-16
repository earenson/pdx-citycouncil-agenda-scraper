"""
 scraper.py
 This script scrapes and stores the Portland City Council agenda as a JSON file.
 The code assumes the HTML tabular format currently in place on the following page:
 
 http://www.portlandonline.com/auditor/index.cfm?c=26997
 
 If this structure changes, this script may break.
 
 """
import requests, json
from bs4 import BeautifulSoup

def getHTML():
    
    # Pull current agenda from site
    html = requests.get('http://www.portlandonline.com/auditor/index.cfm?c=26997')
    if html.status_code is 200:
        agendaData = parseData(html.text)
        return agendaData

def parseData(html):
    soup = BeautifulSoup(html)
    agendaTable = soup.findAll('div','wysiwyg')
    
    # TODO: City Council sessions sometimes span multiple days. Need to detect dates in the table and split sessions for storage
    
    # Get Council Session date(s)
    agenda_date_html = agendaTable[1].find('td').findAll('p')[1:]
    agenda_date = ''.join(agenda_date_html[0].find(text=True))
    agenda = {'agenda_date':agenda_date, 'items':{}}
    
    #Collect all the important rows
    items = []
    for row in agendaTable[1].findAll('td'):
        item = {}
        item['timestamp'] = ''
        itemNumber = row.find('a')
        if itemNumber is not None:
            item['item_number'] = itemNumber.text.replace("&nbsp;","")
            itemNumber.extract()
            text = row.text.replace('\t',"")
            text = text.replace('&nbsp;'," ")
            text = text.replace('\n'," ")
            item['description'] = text.lstrip()
            items.append(item)
        else:
            print row
            
    agenda['items'] = items
    
    return agenda


# Get this party started
agenda = getHTML()

# TODO: Store in DB or write to file
print json.dumps(agenda)