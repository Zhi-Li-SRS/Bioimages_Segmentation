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
