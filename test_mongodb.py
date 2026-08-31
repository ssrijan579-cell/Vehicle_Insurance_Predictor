import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi


# Load .env
load_dotenv()


# Get MongoDB URL
MONGODB_URL = os.getenv("MONGODB_URL")


print("===================================")
print("MongoDB Connection Test")
print("===================================")

print("MONGODB_URL found:", bool(MONGODB_URL))

if MONGODB_URL:

    print(
        "URL starts with:",
        MONGODB_URL[:15]
    )

else:

    print("MONGODB_URL is missing")

    raise Exception(
        "MONGODB_URL is not found in .env"
    )


# Create MongoDB client
client = MongoClient(
    MONGODB_URL,
    tlsCAFile=certifi.where()
)


# Test connection
print("\nTesting MongoDB connection...")

print(
    client.admin.command("ping")
)


print("\nMongoDB connection successful!")


# Database
database = client[
    "Vehicle_Insurance_Predictor"
]


# Collection
collection = database[
    "Vehicle-Data"
]


print(
    "Database:",
    database.name
)

print(
    "Collection:",
    collection.name
)


# Count documents
count = collection.count_documents({})


print(
    "Documents:",
    count
)