import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of the product
URL = "https://www.amazon.in/dp/B0CHX1D7PH/"
headers = {"User-Agent": "Mozilla/5.0"}

# Step 1: Send request
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# Step 2: Extract product title and price
title = soup.find("span", attrs={"id": "productTitle"}).get_text().strip()
price = soup.find("span", attrs={"class": "a-price-whole"}).get_text().strip()

# Step 3: Store data in dictionary
data = {
    "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Product": [title],
    "Price": [price]
}

# Step 4: Save to CSV
df = pd.DataFrame(data)
df.to_csv("amazon_price_tracker.csv", mode='a', index=False, header=False)

print("Data saved successfully:", data)
https://www.amazon.in/dp/B0CHX1D7PH/
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of the product
URL = "https://www.amazon.in/dp/B0CHX1D7PH/"
headers = {"User-Agent": "Mozilla/5.0"}

# Step 1: Send request
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# Step 2: Extract product title and price
title = soup.find("span", attrs={"id": "productTitle"}).get_text().strip()
price = soup.find("span", attrs={"class": "a-price-whole"}).get_text().strip()

# Step 3: Store data
data = {
    "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Product": [title],
    "Price": [price]
}

df = pd.DataFrame(data)
df.to_csv("amazon_price_tracker.csv", mode='a', index=False, header=False)

print("Data saved:", data)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_price_tracker.csv", names=["Date", "Product", "Price"])
df["Price"] = df["Price"].str.replace(",", "").astype(float)

plt.plot(df["Date"], df["Price"])
plt.title("Amazon Product Price Trend")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.xticks(rotation=45)
plt.show()
