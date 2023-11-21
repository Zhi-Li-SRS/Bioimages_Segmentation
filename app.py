import os
import sys

from cellSegmentation.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
print("Training done")
