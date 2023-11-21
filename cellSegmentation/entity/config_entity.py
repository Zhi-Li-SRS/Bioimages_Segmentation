import os
from dataclasses import dataclass
from datetime import datetime

from cellSegmentation.constant.training_pipeline import *


@dataclass
class TrainingPipelineConfig:
    artifacts_dir = ARTIFACTS_DIR


training_pipeline_config = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )
    data_ingestion_feature_store_dir = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )
    data_download_url = DATA_DOWNLOAD_URL


@dataclass
class DataValidationConfig:
    data_validation_dir = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )
    validation_status_file_dir = os.path.join(
        data_validation_dir, DATA_VALIDATION_STATUS
    )
    data_validation_all_required_files = DATA_VALIDATION_ALL_REQUIRED_FILES


@dataclass
class ModelTrainerConfig:
    model_trainer_dir = os.path.join(
        training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME
    )
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    no_epochs = MODEL_TRAINER_NO_EPOCHS
    batch_size = MODEL_TRAINER_BATCH_SIZE
