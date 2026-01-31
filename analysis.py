import pandas as pd

# Load customer data
customers = pd.read_csv("Customer.csv")

# Display first 5 rows
print("Customer Data:")
print(customers.head())

# Load shipment data
shipments = pd.read_csv("Shipment_Details.csv")

# Display shipment info
print("\nShipment Data:")
print(shipments.head())

# Check missing values
print("\nMissing Values:")
print(customers.isnull().sum())
