from src.datascience.components.data_validation import DataValidation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger


STAGE_NAME = "DATA VALIDATION STAGE"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_ingestion_config)
        data_ingestion.validate_all_columns()


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} ended <<<<<<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e