from winequality.config.configuration import ConfigurationManager
from winequality.components.model_evaluation import ModelEvaluation
from winequality import logger
from pathlib import Path

STAGE_NAME = "Data evaluation start Stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(
            config=model_evaluation_config)
        model_evaluation_config.save_results()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
