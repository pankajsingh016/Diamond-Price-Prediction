import os
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split


# Data Ingestion Configuration 
@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')


# Create a Data Ingestion class
class DataIngestion:
    def __init__(self)->None:
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        # logging.info('Data Ingestion method starts')

        try:
            df = pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            # logging.info('Data Read as pandas DataFrame')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            # logging.info("Train test split")
            train_set,test_set = train_test_split(df,test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False, header=True)

            # logging.info('Ingestion of Data is Completed.')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            # logging.info('Error occured in Data Ingestion Config')
            raise CustomException(e,sys)
        


