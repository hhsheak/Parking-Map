import requests
import json
from datetime import datetime
import zoneinfo
import pandas as pd
import psycopg2
from qgis.PyQt.QtCore import QTimer
from qgis.core import Qgis

#Obtain real-time data from API
def api_call():
    sg_tz = zoneinfo.ZoneInfo("Asia/Singapore")
    now = datetime.now(sg_tz).isoformat(timespec="seconds").replace("+00:00", "Z")

    response = requests.get(
        "https://api.data.gov.sg/v1/transport/carpark-availability",
        headers={
          "x-api-key": ""
        },
        params={
          "date_time": now
        }
    )

    response_json = response.json()

    df = pd.json_normalize(
            response_json,
            record_path=["items", "carpark_data", "carpark_info"],
            meta = [["items", "carpark_data", "carpark_number"], ["items", "carpark_data", "update_datetime"]]
        )

    df = df[df["lot_type"] == "C"] #For simplicity, I will only use "C" lots (Lots for cars)

    df = df.rename(columns = {"items.carpark_data.carpark_number": "carpark_number", "items.carpark_data.update_datetime": "last_update"})
    return df

#Update table in pgAdmin4
def update_table(df):
    conn = psycopg2.connect(database = "parking",
            user = "postgres",
            password = "powerful2",
            host = "localhost",
            port = 5432)
        
    with conn: #Upserts data from the API
        with conn.cursor() as cursor:
            for _, row in df.iterrows():
                cursor.execute("""
                            INSERT INTO carpark_status(lot_type,
                                lots_available,
                                total_lots,
                                carpark_number,
                                last_update)
                            VALUES(%s, %s, %s, %s, %s)
                            ON CONFLICT(carpark_number)
                            DO UPDATE SET lot_type = EXCLUDED.lot_type,
                                          lots_available = EXCLUDED.lots_available,
                                          total_lots = EXCLUDED.total_lots,
                                          last_update = EXCLUDED.last_update;
                            """, (row['lot_type'],
                                 row['lots_available'],
                                 row['total_lots'],
                                 row['carpark_number'],
                                 row['last_update'])
                            )
        
    conn.close()

def refresh_data():
    try:
        df = api_call()
        update_table(df)
        iface.messageBar().pushSuccess("Success!","Refresh successful!")
    except Exception as e:
        iface.messageBar().pushCritical("Update failed!", str(e))

#Refreshes every minute 
refresh_data()
timer = QTimer()
timer.setInterval(60000)
timer.timeout.connect(refresh_data)
timer.start()