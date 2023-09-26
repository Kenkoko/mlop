import numpy as np
import pandas as pd
from clearml import TaskTypes
from clearml.automation.controller import PipelineDecorator


@PipelineDecorator.component(return_values=["data_frame"], cache=True, task_type=TaskTypes.data_processing)
def multiple_columns(data: pd.DataFrame, columns: list, new_name: str):
    import json
    columns = json.loads(columns) if type(columns) is str else columns
    print(f'Transforming those columns: {columns}')
    print(f'Len: {len(columns)}')
    print(f'Data type: {type(columns)}')
    output = data[columns[0]]
    for idx in range(1, len(columns)):
        output *= data[columns[idx]]
    data[new_name] = output
    return data

# @PipelineDecorator.component(return_values=["X_train", "X_test", "y_train", "y_test"], cache=True, task_type=TaskTypes.data_processing)
def split_dataset(data_frame, test_size=0.2, random_state=1202):
    import pandas as pd  # noqa
    from sklearn.model_selection import train_test_split

    y = data_frame["y"]
    X = data_frame[(c for c in data_frame.columns if c != "y")]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test
