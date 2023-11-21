import os
import shutil
import sys

from cellSegmentation.entity.artifacts_entity import (
    DataIngestionArtifacts,
    DataValidationArtifacts,
)
from cellSegmentation.entity.config_entity import DataValidationConfig
from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifacts: DataIngestionArtifacts,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys)

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifacts.feature_store_path)

            for file in all_files:
                if (
                    file
                    not in self.data_validation_config.data_validation_all_required_files
                ):
                    validation_status = False
                    os.makedirs(
                        self.data_validation_config.data_validation_dir, exist_ok=True
                    )
                    with open(
                        self.data_validation_config.valid_status_file_dir, "w"
                    ) as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(
                        self.data_validation_config.data_validation_dir, exist_ok=True
                    )
                    with open(
                        self.data_validation_config.validation_status_file_dir, "w"
                    ) as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifacts:
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifacts = DataValidationArtifacts(
                validation_status=status
            )

            logging.info(
                "Exited initiate_data_validation method of DataValidation class"
            )
            logging.info(f"Data validation artifact: {data_validation_artifacts}")

            if status:
                shutil.copy(
                    self.data_ingestion_artifacts.data_zip_file_path, os.getcwd()
                )

            return data_validation_artifacts

        except Exception as e:
            raise AppException(e, sys)
