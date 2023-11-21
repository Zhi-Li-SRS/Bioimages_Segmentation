import os
import sys
import zipfile

import gdown

from cellSegmentation.entity.artifacts_entity import DataIngestionArtifacts
from cellSegmentation.entity.config_entity import DataIngestionConfig
from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def download_data(self):
        dataset_url = self.data_ingestion_config.data_download_url
        zip_download_dir = self.data_ingestion_config.data_ingestion_dir
        os.makedirs(zip_download_dir, exist_ok=True)
        data_file_name = "data.zip"
        zip_file_path = os.path.join(zip_download_dir, data_file_name)
        logging.info(f"Downloading data from {dataset_url} to {zip_file_path}")

        file_id = dataset_url.split("/")[-2]
        prefix = "https://drive.google.com/uc?/export=download&id="
        gdown.download(prefix + file_id, zip_file_path)

        logging.info(f"Downloaded data to {zip_file_path}")
        return zip_file_path

    def extract_zip_file(self, zip_file_path):
        feature_store_path = self.data_ingestion_config.data_ingestion_feature_store_dir
        os.makedirs(feature_store_path, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(feature_store_path)

        return feature_store_path

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)
            data_ingestion_artifacts = DataIngestionArtifacts(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path,
            )
            logging.info("Data ingestion completed")

            return data_ingestion_artifacts
        except Exception as e:
            raise AppException(e, sys)
