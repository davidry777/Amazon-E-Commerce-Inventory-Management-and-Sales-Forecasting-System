import pandas as pd
from pymongo import MongoClient
import os

mongo_password = os.getenv('MONGO_PASSWORD')
client = MongoClient(f"mongodb+srv://dryan0319:{mongo_password}@cluster0.kq8dt.mongodb.net/")
db = client["ecommerce"]

# Importing Amazon-Sale-Report.csv to ecommerce database
db.create_collection("Amazon-Sale-Report")
df = pd.read_csv("Amazon-Sale-Report.csv")
data = df.to_dict(orient='records')
db["Amazon-Sale-Report"].insert_many(data)

# Importing International_Sale_Report.csv to ecommerce database
db.create_collection("International-Sale-Report")
df = pd.read_csv("International_Sale_Report.csv")
data = df.to_dict(orient='records')
db["International-Sale-Report"].insert_many(data)

# Importing Sale_Report.csv to ecommerce database
db.create_collection("Sales-Report")
df = pd.read_csv("Sale_Report.csv")
data = df.to_dict(orient='records')
db["Sales-Report"].insert_many(data)

# Importing March-2021.csv to ecommerce database
db.create_collection("Sales-March-2021")
df = pd.read_csv("March-2021.csv")
data = df.to_dict(orient='records')
db["Sales-March-2021"].insert_many(data)

# Importing May-2022.csv to ecommerce database
db.create_collection("Sales-May-2022")
df = pd.read_csv("May-2022.csv")
data = df.to_dict(orient='records')
db["Sales-May-2022"].insert_many(data)