from clearml import PipelineController
import training
import data_stage

def prepare_data(columns: list):
    print("Preparing data now ....")
    import data_stage
    data = data_stage.dummy_data() # getting data
    print("Get data: Okay")
    data = data_stage.remove_na(data) # cleaning data
    print("Clean data: Okay")
    data = data_stage.multiple_columns( 
        data=data, 
        columns=columns, 
        new_name='x4') # transform data
    print("Transform data: Okay")
    return data


if __name__ == "__main__":
    pipe = PipelineController(
            project='examples',
            name='linear_regression pipeline',
            version='1.1',
            repo='https://github.com/Kenkoko/mlop.git',
            add_pipeline_tags=False,
        )
    pipe.add_parameter(
        name='columns',
        description='transform columns',
        default=['x1', 'x2']
    )
    
    pipe.add_function_step(
        name='data_preparation',
        function=prepare_data,
        function_kwargs=dict(columns='${pipeline.columns}'),
        function_return=['data_frame'],
        # cache_executed_step=True,
    )

    pipe.add_function_step(
        name='processing_data',
        function=data_stage.split_dataset,
        function_kwargs=dict(data_frame='${data_preparation.data_frame}'),
        function_return=['X_train', 'X_test', 'y_train', 'y_test'],
        # cache_executed_step=True,
    )

    pipe.add_function_step(
        name='training',
        function=training.train_linear_regression,
        function_kwargs=dict(
            X_train='${processing_data.X_train}',
            y_train='${processing_data.y_train}'),
        function_return=['model'],
        # cache_executed_step=True,
    )

    pipe.add_function_step(
        name='validation',
        function=training.regression_results,
        function_kwargs=dict(
            model='${training.model}',
            X_test='${processing_data.X_test}',
            y_test='${processing_data.y_test}'),
        function_return=['report_df'],
        # cache_executed_step=True,
    )
    
    pipe.set_default_execution_queue('default')

    pipe.start_locally(run_pipeline_steps_locally=True)

    print('pipeline completed')
    