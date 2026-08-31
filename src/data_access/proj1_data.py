import sys
import pandas as pd

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException
from src.logger import logging


class Proj1Data:

    def __init__(self) -> None:

        try:

            logging.info(
                "Initializing Proj1Data"
            )

            self.mongo_client = MongoDBClient(
                database_name=DATABASE_NAME
            )

        except Exception as e:

            raise MyException(e, sys) from e


    def export_collection_as_dataframe(
        self,
        collection_name: str
    ) -> pd.DataFrame:

        try:

            logging.info(
                f"Exporting collection '{collection_name}' as dataframe"
            )

            # Get collection
            collection = self.mongo_client.database[
                collection_name
            ]

            # Get all documents
            data = list(
                collection.find()
            )

            # Convert MongoDB documents to DataFrame
            dataframe = pd.DataFrame(data)

            # Remove MongoDB generated _id column
            if "_id" in dataframe.columns:

                dataframe.drop(
                    columns=["_id"],
                    inplace=True
                )

            logging.info(
                f"Data successfully loaded. Shape: {dataframe.shape}"
            )

            return dataframe

        except Exception as e:

            logging.error(
                f"Error while exporting collection: {str(e)}"
            )

            raise MyException(e, sys) from e