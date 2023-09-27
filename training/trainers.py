from clearml import TaskTypes
from clearml.automation.controller import PipelineDecorator

# @PipelineDecorator.component(return_values=["model"], cache=True, task_type=TaskTypes.training)
def train_linear_regression(X_train, y_train):
    # make sure we have pandas for this step, we need it to use the data_frame
    import pandas as pd  # noqa
    from sklearn.linear_model import LinearRegression
    from clearml import Logger
    import training

    model = LinearRegression()
    model.fit(X_train, y_train)

    PipelineDecorator.get_logger().report_table(
        title='Regression Report',
        series='Coefficient and Interception',
        table_plot = training.extract_coef_intercept(model)
    )
    return model


def extract_coef_intercept(model):
    # Extract coefficients and interception from the SciKit Linear Reg model
    # input
    #   @param model: Scikit Model
    # output:
    #   Pandas table
    
    import pandas as pd

    output = {
        "const": model.intercept_
    }
    for idx, coef in enumerate(model.coef_) :
        output[f'x{idx + 1}'] = round(coef, 4)
    
    return pd.DataFrame(output, index=[0])