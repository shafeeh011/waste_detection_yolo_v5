from src.yoloproject.constants import *
from src.yoloproject.utils.common import read_yaml, create_directories
from src.yoloproject.entity.config_entity import DataIngestionConfig, DataValidationConfig, ModelTrainingConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_dir=config.local_dir,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([Path(config.root_dir)])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            data_validation_status_file=Path(config.data_validation_status_file),
            data_validation_required_files_dir=Path(config.data_validation_required_files_dir),  
            data_validation_all_required_files=list(config.data_validation_all_required_files), # Expected files
            data_location=Path(config.data_location),
            data_copy_location=Path(config.data_copy_location),
            data_file= config.data_file,  # Expected file name
            
        )

        return data_validation_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        
        create_directories([config.root_dir, config.feature_store_root_dir])
        
        model_training_config = ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            feature_store_root_dir=Path(config.feature_store_root_dir),
            data_yaml_file=config.data_yaml_file,  
            pretrained_model_path=Path(config.pretrained_model_path),
            pretrained_model_name=config.pretrained_model_name,
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE, 
        )
        
        return model_training_config