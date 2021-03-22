from configparser import ConfigParser
from pathlib import Path
import psycopg2
import requests, psycopg2, json

here = Path(__file__).parent.resolve()
CONFIG_PATH = here / 'database.ini'

def config(filename= CONFIG_PATH, section='postgresql'):
    
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db



def get_data_from_service():

    response = requests.get("https://api.ibb.gov.tr/ispark/Park")
    response.raise_for_status()
    data = response.json()

    return data


def insert_park(park):
    sql = """INSERT INTO public.parkapp_park
            (park_name, lat, lng, capacity, empty_capacity, work_hours, park_type, is_open, park_id,district,free_time,location,user_id)
            VALUES (%(parkName)s, %(lat)s, %(lng)s, %(capacity)s, %(emptyCapacity)s, %(workHours)s,%(parkType)s, %(isOpen)s, %(parkID)s, %(district)s, %(freeTime)s,ST_SetSRID(ST_MakePoint(%(lng)s,%(lat)s),4326),1);
            """ 
    
    conn = None 

    try:    
        params = config()        
        conn = psycopg2.connect(**params)            
        cur = conn.cursor()        
        cur.execute(sql,park)
        conn.commit()            
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

park_list = get_data_from_service()

for park in  park_list:
    insert_park(park)