 import os
 import sys 
 import yaml 
 import base64
 
 from cellSegmentation.logger import logging 
 from cellSegmentation.exception import AppException
 
 def read_yaml_file(file_path: str) -> dict:
     try:
         with open(file_path, "rb") as f:
             logging.info(f"Read yaml file successfully ")
             return yaml.safe_load(f)
    except Exception as e:
        raise AppException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool=False) -> None:
    try:
        if replace:
            is os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as f:
            yaml.dump(content, f)
            logging.info(f"Successfully write yaml file")
    except Exception as e:
        raise AppException(e, sys)
    
def decodeImage(imgstring, file_name):
    imgdata = base64.b64decode(imgstring)
    with open("./data" + file_name, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())