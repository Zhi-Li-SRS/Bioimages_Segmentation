import os
import sys

from cellSegmentation.entity.artifacts_entity import ModelTrainerArtifacts
from cellSegmentation.entity.config_entity import ModelTrainerConfig
from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging
from cellSegmentation.utils.main_utils import read_yaml_file


class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self):
        logging.info("Initiating Model Trainer")
        try:
            logging.info("unzip data")
            os.system("unzip data.zip")
            os.system("rm data.zip")
            os.system(
                f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true"
            )
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(
                f"cp runs/segment/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}"
            )
            os.system("rm -rf yolov8s-seg.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")

            model_trainer_artifacts = ModelTrainerArtifacts(
                trained_model_file_path=f"{self.model_trainer_config.model_trainer_dir}/best.pt"
            )
            logging.info("Model Trainer Completed")

            return model_trainer_artifacts

        except Exception as e:
            raise AppException(e, sys)
