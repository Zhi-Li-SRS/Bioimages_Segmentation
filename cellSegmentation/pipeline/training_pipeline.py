import os
import sys

from cellSegmentation.components.data_ingestion import DataIngestion
from cellSegmentation.entity.artifacts_entity import DataIngestionArtifacts
from cellSegmentation.entity.config_entity import DataIngestionConfig
from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self):
        data_ingestion = DataIngestion()
        data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
        return data_ingestion_artifacts

    def run_pipeline(self):
        data_ingestion_artifacts = self.start_data_ingestion()
