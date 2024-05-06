import pyproj
import pandas as pd

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

    with open('버스정류장_현황_katec.csv', "a", encoding='utf-8') as f: #txt추가
        data = x+', '+y+'\n'
        f.write(data)

for i in range(1,876):
    df = pd.read_csv('영주시_버스정류장 현황.csv', encoding = "cp949")
    aax=df['경도'][i]
    aay=df['위도'][i]

    KATEC_to_wgs84(aax, aay)