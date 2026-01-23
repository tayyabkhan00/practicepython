import pandas as pd

data = {
    'location': [
        'Whitefield', 'Whitefield', 'Whitefield',
        'Electronic City', 'Electronic City',
        'Rajaji Nagar',
        'Small Area 1',
        'Small Area 2',
        'Small Area 3'
    ],
    'total_sqft': [1200, 1300, 1250, 1000, 1050, 1500, 900, 850, 870],
    'price': [60, 65, 63, 40, 42, 95, 30, 28, 29]
}

df = pd.DataFrame(data)

location_stats=df['location'].value_counts()
df['location']=df['location'].apply(lambda x:"other" if location_stats[x]<2 else x )

dummies = pd.get_dummies(df['location'], drop_first=True)
df = pd.concat([df.drop('location', axis=1), dummies], axis=1)
print(df)
