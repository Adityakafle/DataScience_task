import pandas as pd

def load_datasets(performance_file, execution_file):
    performance_data = pd.read_csv(performance_file)
    workflow_execution_data = pd.read_csv(execution_file)
    return performance_data, workflow_execution_data

if __name__ == "__main__":
    performance_data, workflow_execution_data = load_datasets('performance.csv', 'workflow_execution.csv')
    print("Performance Data:")
    print(performance_data.head())
    print("\nWorkflow Execution Data:")
    print(workflow_execution_data.head())
