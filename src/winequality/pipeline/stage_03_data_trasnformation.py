from winequality.config.configuration import ConfigurationManager
from winequality.components.data_transformation import DataTransformation
from winequality import logger
from pathlib import Path

STAGE_NAME = "Data transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # file_path = r"red-wine-ml\artifacts\data_validation\status.txt"
        try:
            # with open(Path(file_path), "r") as f:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(
                        config=data_transformation_config)
                    data_transformation.train_test_split()
                else:
                    raise Exception("your schema is not valid")

        except Exception as e:
            raise e

            # config = ConfigurationManager()
            # data_transformation_config = config.get_data_transformation_config()
            # data_transformation = DataTransformation(
            #     config=data_transformation_config)
            # data_transformation.train_test_split()
