ARTIFACTS_DIR: str = "artifacts"

DATA_INGESTION_DIR_NAME = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"

DATA_DOWNLOAD_URL = (
    url
) = "https://drive.google.com/file/d/1ECfl3dtYyfivY8kYPq7RHUBTjC-2vf61/view?usp=sharing"

"""
Data Validation constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_STATUS = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "data.yaml"]

"""
Model Trainer related Constant folder name
"""
MODEL_TRAINER_DIR_NAME = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME = "yolov8s-seg.pt"
MODEL_TRAINER_NO_EPOCHS = 1
MODEL_TRAINER_BATCH_SIZE = 16
