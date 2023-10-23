import dataretrieval.nwis as nwis
from datetime import datetime
from dateutil import tz
from tabulate import tabulate
import pandas as pd
import configparser
import string

def retrieval():
    #Setting up config parser to get data from settings.ini

    config = configparser.ConfigParser()
    config.read('settings.ini')

    #Create a dictionary passed off settings.ini

    df = pd.DataFrame(columns=['Name', 'Code', 'Flow', 'Temp'])
    rivers = config.options('Gauges')
    for river in rivers:
        temp = None
        code = config.get('Gauges', river)
        record = nwis.get_record(sites=code, service='iv')
        flow = record.iloc[-1]['00060']
        temp = pd.to_datetime(record.index[-1])

        
        try:
            temp = round((record.iloc[-1]['00010']*1.8+32), 1)
        except:
            temp = None
        try:
            if(int(float(flow)) and flow > 0):
                df.loc[len(df.index)] = [string.capwords(river), code, int(float(flow)), temp]
        except:
            continue
    return df

if __name__ == "__main__":
    print (retrieval())