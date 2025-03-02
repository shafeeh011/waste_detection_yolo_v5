from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_dir: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_validation_status_file: Path
    data_validation_required_files_dir: Path
    data_validation_all_required_files: list
    data_location: Path
    data_copy_location: Path
    data_file : str
    
    
@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    feature_store_root_dir: Path
    data_yaml_file: str
    pretrained_model_path: Path
    pretrained_model_name: str
    params_epochs: int
    params_batch_size: int
    