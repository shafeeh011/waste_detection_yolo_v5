from src.yoloproject.config.configuration import ConfigurationManager
from src.yoloproject.components.data_validation import DataValidation
from src.yoloproject import logger


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()

        data_validator = DataValidation(config=data_validation_config)
        validation_status = data_validator.validate_data()
        print(f"Data Validation Completed. Status: {validation_status}")
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataValidationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e