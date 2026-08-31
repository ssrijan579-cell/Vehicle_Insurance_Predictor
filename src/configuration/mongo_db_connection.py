import os
import sys
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

from src.constants import MONGODB_URL_KEY
from src.exception import MyException
from src.logger import logging


# ============================================================
# Load .env file
# ============================================================

# Get project root directory
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

# Path to .env
ENV_PATH = os.path.join(PROJECT_ROOT, ".env")

# Load environment variables
load_dotenv(ENV_PATH)


# Get MongoDB URL
MONGODB_URL = os.getenv(MONGODB_URL_KEY)


# ============================================================
# MongoDB Client
# ============================================================

class MongoDBClient:

    client = None

    def __init__(self, database_name: str) -> None:

        try:

            logging.info("Initializing MongoDB connection")

            # Check MongoDB URL
            if not MONGODB_URL:

                raise Exception(
                    f"Environment variable '{MONGODB_URL_KEY}' is not set."
                )

            # ------------------------------------------------
            # Create MongoDB client
            # ------------------------------------------------

            self.mongo_client = MongoClient(
                MONGODB_URL,
                tlsCAFile=certifi.where()
            )

            # ------------------------------------------------
            # Test MongoDB connection
            # ------------------------------------------------

            self.mongo_client.admin.command("ping")

            logging.info("MongoDB connection successful.")

            # ------------------------------------------------
            # Select database
            # ------------------------------------------------

            self.database = self.mongo_client[database_name]

            logging.info(
                f"Connected to database: {database_name}"
            )

        except Exception as e:

            logging.error(
                f"Error connecting to MongoDB: {str(e)}"
            )

            raise MyException(e, sys) from e