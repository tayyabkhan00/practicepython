import pandas as pd

data = {
    "total_sqft": [
        "1056",
        "2100-2850",
        "3000",
        "34.46Sq. Meter",
        "4125Perch",
        "1200",
        "1500-1800",
        "600Sq. Yards",
        "not available",
        "2000"
    ]
}

df = pd.DataFrame(data)

def convert_sqft(x):
    tokens=x.split('-')
    if len(tokens)==2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None

df['total_sqft']=df["total_sqft"].apply(convert_sqft)
df.dropna
print(df)