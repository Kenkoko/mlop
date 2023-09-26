
import cleanner
import ingestors
import transformer
from clearml import TaskTypes
from clearml.automation.controller import PipelineDecorator


# @PipelineDecorator.pipeline(name="data preparation", project="examples", version="0.0.5")
# @PipelineDecorator.component(return_values=["data_frame"], cache=True, task_type=TaskTypes.data_processing)
def prepare_data(columns: list):
    data = ingestors.dummy_data()
    data = cleanner.remove_na(data)
    data = transformer.multiple_columns(
        data=data, 
        columns=columns, 
        new_name='x4')
    # return data

if __name__ == "__main__":
    PipelineDecorator.run_locally()
    prepare_data(columns=['x1', 'x2'])
