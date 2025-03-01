import os
import sys
import zipfile
import gdown
from src.yoloproject import logger
from src.yoloproject.utils.common import get_size
from src.yoloproject.entity.config_entity import DataIngestionConfig
from src.yoloproject.exception import AppException

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self)-> str:
        '''
        Fetch the data from the source URL
        '''
        
        try:
            dataset_url = self.config.source_URL
            zip_download_path = self.config.local_dir
            os.makedirs(os.path.dirname(zip_download_path), exist_ok=True)
            logger.info(f"Downloading file from {dataset_url} to {zip_download_path}")
            
            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_path)
            logger.info(f"Downloading file from {dataset_url} to {zip_download_path}")
            
        except Exception as e:
            raise AppException(e , sys)
        
    def extract_zip_file(self):
        '''
        Extract the data from the zip file
        '''
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_dir, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted zip file to {unzip_path}")
                
        except Exception as e:
            raise AppException(e, sys)