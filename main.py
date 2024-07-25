from winequality import logger
from winequality.pipeline.stage_01_data_ingestion import DataINgestionTrainingPipeline
from winequality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from winequality.pipeline.stage_03_data_trasnformation import DataTransformationTrainingPipeline
from winequality.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from winequality.pipeline.stage_05_data_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataINgestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data transformation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "model trainer Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion = ModelTrainerPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data evaluation start Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion = ModelEvaluationPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
