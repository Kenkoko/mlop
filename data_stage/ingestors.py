from clearml import TaskTypes
from clearml.automation.controller import PipelineDecorator


@PipelineDecorator.component(return_values=["data_frame"], cache=True, task_type=TaskTypes.data_processing)
def dummy_data(seed = None, number_example: int = 100):
    import numpy as np
    import pandas as pd
    np.random.seed(seed)

    x1 = np.random.uniform(1, 10, size=(number_example,))
    x2 = np.random.uniform(1, 10, size=(number_example,))
    x3 = np.random.uniform(1, 10, size=(number_example,))
    y = 3*x1 + 2*x2 + 10*x3 + 2*x1*x2 + np.random.normal(-1,1, size=(number_example,))

    data = pd.DataFrame({
        'x1': x1,
        'x2': x2,
        'x3': x3,
        'y': y
    })
    return  data

