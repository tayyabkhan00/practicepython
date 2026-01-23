import pandas as pd

dict1={
    "location":["whitefield","pune","lko","pwn","spn","delhi"],
    "size":["2 bhk","2 bhk","1 bhk","4 bedroom","5 bedroom","2 bhk"],
    "price":[50,60,78,84,69,66]
}
df=pd.DataFrame(dict1)
df["bhk"]=df['size'].apply(lambda x:int(x.split()[0]))
df.drop('size',axis=1,inplace=True)
print(df.head())