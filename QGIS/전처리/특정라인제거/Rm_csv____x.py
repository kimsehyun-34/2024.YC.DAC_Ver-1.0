import pandas as pd

# data = pd.read_csv('2023.12.csv')
# data11 = pd.read_csv('2023.11.csv')
# print("a")
# data10 = pd.read_csv('2023.10.csv')
# data9 = pd.read_csv('2023.09.csv')
# print("b")
# data8 = pd.read_csv('2023.08.csv')
# data7 = pd.read_csv('2023.07.csv')
# print("c")
# data6 = pd.read_csv('2023.06.csv')
# data5 = pd.read_csv('2023.05.csv')
# print("d")
# data4 = pd.read_csv('2023.04.csv')
# data3 = pd.read_csv('2023.03.csv')
# print("e")
# data2 = pd.read_csv('2023.02.csv')
data1 = pd.read_csv('2023.01.csv')
print("f")

# data=[data1,data2]

while True:
    for j in range(1,13):
        # data= data[j]
        # data=str(data) 
        data=data1
        for i in range(1,11):
            total_a=i

            fr = data1[(data['total'] == total_a)]
            # fr1 = fr.iloc[:,32:33]

            print(fr)
            print(i)
            data.drop(fr.index, inplace=True)
            data.to_csv("10"+"_data"+"t"+".csv", index=False)
        
        print('1')

        for i in range(1,51):
            total_a=i

            fr = data[(data['total'] == total_a)]
            # fr1 = fr.iloc[:,32:33]

            print(fr)
            print(i)
            data.drop(fr.index, inplace=True)
            data.to_csv("50"+"_data"+"t"+".csv", index=False)

        print('2')

        for i in range(1,101):
            total_a=i

            fr = data[(data['total'] == total_a)]
            # fr1 = fr.iloc[:,32:33]

            print(fr)
            print(i)
            data.drop(fr.index, inplace=True)
            data.to_csv("100"+"_data"+"t"+".csv", index=False)
            
    break
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\naaaaaaaaaaaaaaaaaaaaaaaaaa")