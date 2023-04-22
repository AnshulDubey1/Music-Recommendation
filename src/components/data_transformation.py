import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import os


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data tranasformation
        '''
        try:
            numerical_columns = ['tempo', 'valence']
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())

                ]
            )
            logging.info("Read and transformed the relevant data")
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns)
                ]
            )
            return preprocessor
        except Exception as E:
            raise CustomException(E, sys)

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()
            numerical_columns = ['tempo', 'valence']
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            input_df_train = train_df[numerical_columns]
            input_df_test = test_df[numerical_columns]
            input_feature_train = preprocessing_obj.fit_transform(input_df_train)
            input_feature_test = preprocessing_obj.transform(input_df_test)
            emotional_stage_train = (input_feature_train[:, 1] + input_feature_train[:, 0]) / 2
            emotional_stage_test = (input_feature_test[:, 1] + input_feature_test[:, 0]) / 2
            emotions_train = np.where(emotional_stage_train > 0, 1, 0)
            emotions_test = np.where(emotional_stage_test > 0, 1, 0)
            input_feature_train = np.column_stack((input_feature_train, emotions_train))
            input_feature_test = np.column_stack((input_feature_test, emotions_test))
            logging.info("Saved preprocessing object")
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                input_feature_train,
                input_feature_test,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as E:
            raise CustomException(E, sys)
