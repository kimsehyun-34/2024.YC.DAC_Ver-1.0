import pandas as pd


def main(a):
    data='100_'+'2023.'+a+'.csv'

    df = pd.read_csv(data)

    all=(df["m20"])+(df["m25"])+(df["f20"])+(df["f25"])

    g="20"

    filtered_df = df[all >= int(g)]

    filtered_df.to_csv('20y'+"_"+data, index=False)

    print("g")
    
# for i in range(1,13):
#     if i<10:
#         a="0"+str(i)
#     else:
#         a=str(i)
#     main(a)
