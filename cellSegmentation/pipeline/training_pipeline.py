import os
import sys

from cellSegmentation.components.data_ingestion import DataIngestion
from cellSegmentation.components.data_validation import DataValidation
from cellSegmentation.entity.artifacts_entity import (
    DataIngestionArtifacts,
    DataValidationArtifacts,
)
from cellSegmentation.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
)
from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    def start_data_ingestion(self):
        data_ingestion = DataIngestion()
        data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
        return data_ingestion_artifacts

    def start_data_validation(self, data_ingestion_artifacts: DataIngestionArtifacts):
        data_validation = DataValidation(
            data_ingestion_artifacts, self.data_validation_config
        )
        data_validation_artifacts = data_validation.initiate_data_validation()
        return data_validation_artifacts

    def run_pipeline(self):
        data_ingestion_artifacts = self.start_data_ingestion()
        data_validation_artifacts = self.start_data_validation(data_ingestion_artifacts)
