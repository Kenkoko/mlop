
import numpy as np
import pandas as pd
from clearml import TaskTypes
from clearml.automation.controller import PipelineDecorator


@PipelineDecorator.component(return_values=["data_frame"], cache=True, task_type=TaskTypes.data_processing)
def remove_na(data: pd.DataFrame):
    return data.dropna()

@PipelineDecorator.component(return_values=["data_frame"], cache=True, task_type=TaskTypes.data_processing)
def remove_duplicate(data: pd.DataFrame):
    return data.drop_duplicates()