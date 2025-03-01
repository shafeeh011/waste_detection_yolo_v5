from src.yoloproject.constants import *
from src.yoloproject.utils.common import read_yaml, create_directories
from src.yoloproject.entity.config_entity import DataIngestionConfig, DataValidationConfig


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
            data_validation_all_required_files=list(config.data_validation_all_required_files) # Expected files
        )

        return data_validation_config
    