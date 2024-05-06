import requests
import json
import pyproj
import pandas as pd

xx=[]
yy=[]

def KATEC_to_wgs84(x, y):
    KATEC = "+proj=latlong +datum=WGS84 +ellps=WGS84"
    WGS84 = "+proj=tmerc +lat_0=38N +lon_0=128E +ellps=bessel +x_0=400000 +y_0=600000 +k=0.9999 +units=m +towgs84=-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43"

    KATEC_proj = pyproj.CRS(KATEC)
    WGS84_proj = pyproj.CRS(WGS84)
    trans_func = pyproj.Transformer.from_crs(KATEC_proj, WGS84_proj, always_xy=True)
    a=trans_func.transform(x, y)

    x=a[0]
    y=a[1]
    x=str(x)
    y=str(y)
    x = x.split('.')
    y = y.split('.')
    x=x[0]
    y=y[0]

    with open('유치원_정보.csv', "a", encoding='utf-8') as f: #txt추가
        data = x+', '+y+'\n'
        f.write(data)

for i in range(1,50):
    df = pd.read_csv('aa.csv', encoding = "cp949")
    aaa=df['loc'][i]

    apiurl = "https://api.vworld.kr/req/address?"
    params = {
        "service": "address",
        "request": "getcoord",
        "crs": "epsg:4326",
        "address": aaa,
        "format": "json",
        "type": "road",
        "key": "9F7D1A45-E0A0-3D8C-96F7-A649A260FBE2"
    }
    response = requests.get(apiurl, params=params)
    if response.status_code == 200:
        json_string=response.json()
        xx=json_string['response']['result']['point']['x']
        yy=json_string['response']['result']['point']['y']

        KATEC_to_wgs84(xx, yy)

    
