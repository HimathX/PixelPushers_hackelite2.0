import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB connection details from environment variables
uri = os.getenv("MONGODB_URI")
db_name = os.getenv("MONGODB_DB_NAME", "infact_db")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client[db_name]  

# Collections
article_collection = db[os.getenv("MONGODB_ARTICLE_COLLECTION", "articles")]
clusters_collection = db[os.getenv("MONGODB_CLUSTERS_COLLECTION", "clusters")]
fact_checks_collection = db[os.getenv("MONGODB_FACT_CHECKS_COLLECTION", "fact_checks")]

# Check if connection is successful
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"MongoDB Connection Error: {e}")
