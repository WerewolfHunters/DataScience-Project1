import os
import zipfile
import urllib.request as request
from src.datascience import logger
from src.datascience.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    # Downloading the zipfile
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with the following info: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists")

    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Functions returns none
        """
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)