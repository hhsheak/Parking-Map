# Parking-Map
*The web map is a static version and does not update in real time. To use the real-time map, you'll need to install QGIS and pgAdmin4 and download the files in "Live Map Files".*

*AI was consulted to provide the general direction of how and what to do. AI was not used to generate any code—all code here (at least the ones in "Live Map Files") was written by me.*

This was an attempt to develop my skills in PostGIS and PyGIS.

## Process
### Step 1: SQL
I downloaded the "HDB Carpark Information" dataset from data.gov.sg (https://data.gov.sg/datasets/d_23f946fa557947f93a8043bbef41dd09/view) and imported it into pgAdmin4. I then used information from it to create carpark_information.

Next, I created carpark_status as a dummy table for data to be inserted, referencing the data structure provided by the API (https://data.gov.sg/datasets/d_ca933a644e55d34fe21f28b8052fac63/view).

Finally, I created a view (so as to allow for updating) that joined the two tables together, using a left join on carpark_status such that only carparks with live information with displayed. This is because while testing, I noticed that carparks with no live information had a null "lot_type" value, which would imply that there was no information about them at all and hence, they would always call a NULL value. Thus, there was no point in keeping them and therefore, I decided to use a left join instead of an inner join.

### Step 2: Python
I then used the Python console in QGIS to write out a programme to call the Carpark Availability API provided by HDB ((https://data.gov.sg/datasets/d_ca933a644e55d34fe21f28b8052fac63/view) and write the data to pgAdmin4. I defined two functions, one to call the API and another to upsert data into pgAdmin4. I then automated the programme using QTimer, ensuring that the programme would continually run as long as QGIS was open. 

### Step 3: QGIS
I added in the carpark_map layer from the connected base and added some symbology to reflect the live availability status of each carpark. This was done using QGIS' automatic layer refresh functionality and hence, I did not need to use any code to automate this. 

I then used qgis2web to upload a static version of the map online for viewing in this repository.

## Areas for Improvement
Currently, the web map is a static version that does not update live. I originally wanted to share the live map online but it would entail dealing with servers and live-hosting, which would have been beyond my abilities.

Another function that would have been useful would be to take the user's live location and show the nearest available carpark. However, I could not figure out how to get the user's live location for free and hence, I decided to drop this function.


