from clearml import TaskTypes
from clearml.automation.controller import PipelineDecorator

# @PipelineDecorator.component(return_values=["model"], cache=True, task_type=TaskTypes.training)
def train_linear_regression(X_train, y_train):
    # make sure we have pandas for this step, we need it to use the data_frame
    import pandas as pd  # noqa
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model