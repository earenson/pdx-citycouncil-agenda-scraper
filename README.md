pdx-citycouncil-agenda-scraper
==============================

A basic Python-based scraper to collect City Council session agenda information from Portlandonline.com

### Background
Every Friday, the Auditor's Office at the City of Portland posts the City Council's agenda for the following week's
session (typically held on Wednesday). This script scrapes and parses the HTML table found at:

http://www.portlandonline.com/auditor/index.cfm?c=26997

Theoretically, this script could run as a CRON job and be tweaked to dump the results into a database or other storage
to build a dataset of City Council agenda information over time.


### Caveats
There are two main caveats to know when using this script:

1. If the structure of the page found at the above URL changes, or the URL itself changes, this script will break until updated.
2. The agenda posted to the above URL will not contain votes on resolutions or other information generated as a result of the City Council session. Agendas updated with this information are stored under Council Records (http://www.portlandonline.com/auditor/index.cfm?c=56674) in PDF format.


### TODO
1. City Council sessions can span multiple days, but there's no hook in the HTML table to easily separate the dates in a single posted agenda.
2. This script doesn't currently dump to a database, but is set to print out JSON of the current agenda as sample output.
