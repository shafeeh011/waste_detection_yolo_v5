from src.yoloproject.config.configuration import ConfigurationManager
from src.yoloproject.components.model_training import ModelTraining
from src.yoloproject import logger

SAGE_NAME = "Model Training stage"

class ModelTrainingTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        
        # Get Model Training Configuration
        model_training_config = config_manager.get_model_training_config()

        # Initialize Model Training Class
        trainer = ModelTraining(config=model_training_config)
        
                # Run the Training
        print("Starting YOLOv5 Training...")
        trainer.model_training()
        print("Training Completed Successfully!")
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {SAGE_NAME} started <<<<<<")
        pipeline = ModelTrainingTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {SAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e