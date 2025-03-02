from src.yoloproject.exception import AppException
import sys
import os
from src.yoloproject.entity.config_entity import DataValidationConfig
import shutil


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        try:
            feature_store_path = self.config.data_validation_all_required_files  # Expected files
            actual_files = set(os.listdir(self.config.data_validation_required_files_dir))  # Files present in the directory

            # Check if all required files are present
            missing_files = [file for file in feature_store_path if file not in actual_files]
            validation_status = len(missing_files) == 0

            # Ensure the directory for status file exists
            self.config.root_dir.mkdir(parents=True, exist_ok=True)

            # Write validation status to file
            with open(self.config.root_dir.joinpath(self.config.data_validation_status_file), "w") as file:
                file.write(f"Validation status: {validation_status}\n")
                if not validation_status:
                    file.write(f"Missing files: {', '.join(missing_files)}\n")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)
        
    def copy_data(self):
        source_file = self.config.data_location / self.config.data_file
        destination_file = self.config.data_copy_location / self.config.data_file

        # Ensure destination directory exists
        self.config.data_copy_location.mkdir(parents=True, exist_ok=True)

        # Copy the file
        shutil.copy(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")