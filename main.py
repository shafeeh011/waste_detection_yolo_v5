from src.yoloproject import logger
from src.yoloproject.pipeline.stage_01_data_ingetion import DataIngestionTrainingPipeline
from src.yoloproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.yoloproject.pipeline.stage_03_model_training import ModelTrainingTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

SAGE_NAME = "Model Training stage"

try:
    logger.info(f">>>>>> stage {SAGE_NAME} started <<<<<<")
    pipeline = ModelTrainingTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {SAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e