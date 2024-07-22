import os
from winequality import logger
from winequality.entity.config_entity import (DataValidationConfig)
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_columns(self) -> bool:
        try:
            validate_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema:
                    validate_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status{validate_status}")
                else:
                    validate_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status{validate_status}")
            return validate_status
        except Exception as e:
            raise e
