import pandas as pd


def main(a):
    data='2023.'+a+'.csv'

    df = pd.read_csv(data)
    print("p")

    g_total="10"

    filtered_df = df[df["total"] >= int(g_total)]

    filtered_df.to_csv(g_total+"_"+data, index=False)

    print("g")
    
for i in range(1,13):
    if i<10:
        a="0"+str(i)
    else:
        a=str(i)
    main(a)
