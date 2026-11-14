# Parking-Map
*The web map is a static version and does not update in real time. To use the real-time map, you'll need to install QGIS and pgAdmin4 and download the files in "Live Map Files".*

*AI was consulted to provide the general direction of how and what to do. AI was not used to generate any code—all code here (at least the ones in "Live Map Files") was written by me.*

This was an attempt to develop my skills in PostGIS and PyGIS.

##Process
###Step 1: SQL
I downloaded the "HDB Carpark Information" dataset from data.gov.sg (https://data.gov.sg/datasets/d_23f946fa557947f93a8043bbef41dd09/view) and imported it into pgAdmin4. I then used information from it to create carpark_status.

Next, I created carpark_information as a dummy table for data to be inserted, referencing the data provided by the API (https://data.gov.sg/datasets/d_ca933a644e55d34fe21f28b8052fac63/view).
