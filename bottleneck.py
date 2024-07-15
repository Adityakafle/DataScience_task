import pandas as pd
import matplotlib.pyplot as plt
import bottleneck

def identify_bottlenecks(workflow_execution_data):
    # Calculate average duration per step
    avg_duration_per_step = workflow_execution_data.groupby('Step')['Duration (seconds)'].mean().reset_index()

    # Plot average duration per step
    plt.figure(figsize=(12, 6))
    plt.bar(avg_duration_per_step['Step'], avg_duration_per_step['Duration (seconds)'])
    plt.xlabel('Step')
    plt.ylabel('Average Duration (seconds)')
    plt.title('Average Duration per Step')
    plt.xticks(rotation=45)
    plt.show()

    # Identify steps with manual interventions
    manual_interventions = workflow_execution_data[workflow_execution_data['Notes'].str.contains('manual', case=False, na=False)]
    print("Steps with Manual Interventions:")
    print(manual_interventions)

    return manual_interventions

if __name__ == "__main__":
    from dataset import load_datasets
    _, workflow_execution_data = load_datasets('performance.csv', 'workflow_execution.csv')
    manual_interventions = identify_bottlenecks(workflow_execution_data)
