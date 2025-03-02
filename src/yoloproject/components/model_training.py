import yaml
import os
from pathlib import Path
from src.yoloproject import logger
from src.yoloproject.constants import *
from src.yoloproject.utils.common import read_yaml_dict
from src.yoloproject.entity.config_entity import ModelTrainingConfig




class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    def model_training(self):
        '''
        Train the YOLOv5 model using the provided data and parameters
        '''
        # Perform the necessary training steps
        try:
            logger.info("Unzipping data")
            os.system("unzip data.zip")
            os.system("rm data.zip")
            with open(self.config.feature_store_root_dir / self.config.data_yaml_file, "r") as stream:
                num_class = str(yaml.safe_load(stream)["nc"])
                
            #model_config_file_name = self.config.pretrained_model_name.split(".")[0]
            model_config_file_name = self.config.pretrained_model_name.split("/")[-1].split(".")[0]
            print(model_config_file_name)
            
            config = read_yaml_dict(Path(f'yolov5/models/{model_config_file_name}.yaml'))
            config['nc'] = int(num_class)
            
            with open(f'yolov5/models/custome_{model_config_file_name}.yaml', "w") as file:
                yaml.dump(config, file)
            
            # Train the model using the provided parameters
            data_yaml = Path(self.config.feature_store_root_dir) / self.config.data_yaml_file
            data_yaml = data_yaml.resolve()  # Get absolute path

            os.system(f"cd yolov5/ && python train.py --img 640 --batch {self.config.params_batch_size} --epochs {self.config.params_epochs} --data {data_yaml} --cfg ./models/custome_yolov5s.yaml --weights {self.config.pretrained_model_name} --name yolov5_results --cache")
            os.system(f"cp yolov5/runs/train/yolov5_results/weights/best.pt {self.config.root_dir}")
            
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf data")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf data.yaml")
        except Exception as e:
            print(f"Error while building the model: {e}")