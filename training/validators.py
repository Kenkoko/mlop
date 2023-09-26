from clearml import TaskTypes
from clearml.automation.controller import PipelineDecorator

@PipelineDecorator.component(return_values=["report"], cache=True, task_type=TaskTypes.qc)
def regression_results(model, X_test, y_test):
    # Product the performance of the regression model.
    # @param: y

    import sklearn.metrics as metrics
    import numpy as np
    import pandas as pd

    # Regression metrics
    y_pred = model.predict(X_test)
    resutls = {
        "explained_variance" : round(metrics.explained_variance_score(y_test, y_pred), 4),
        "mean_squared_log_error" : round(metrics.mean_squared_log_error(y_test, y_pred), 4),
        "R2" : round(metrics.r2_score(y_test, y_pred), 4),
        "MAE" : round(metrics.mean_absolute_error(y_test, y_pred) , 4),
        "MSE" : round(metrics.mean_squared_error(y_test, y_pred), 4),
        "RMSE" : round(np.sqrt(metrics.mean_squared_error(y_test, y_pred)), 4),
    }

    report_df = pd.DataFrame(resutls, index=[0])
    print(report_df)

    return report_df

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