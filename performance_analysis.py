import pandas as pd
import matplotlib.pyplot as plt

import importlib

try:
    importlib.import_module('bottleneck')
except ImportError:
    pass
def analyze_performance(performance_data):
    # Convert string representation of list to actual list
    performance_data['Avg. Processing Time/Step (min)'] = performance_data['Avg. Processing Time/Step (min)'].apply(lambda x: [float(i) for i in x.split(',')])

    # Calculate total average processing time for each workflow
    performance_data['Total Avg. Processing Time (min)'] = performance_data['Avg. Processing Time/Step (min)'].apply(sum)

    # Plot total average processing time for each workflow
    plt.figure(figsize=(10, 6))
    plt.bar(performance_data['Workflow Name'], performance_data['Total Avg. Processing Time (min)'])
    plt.xlabel('Workflow Name')
    plt.ylabel('Total Avg. Processing Time (min)')
    plt.title('Total Average Processing Time per Workflow')
    plt.xticks(rotation=45)
    plt.show()

    # Print key metrics
    print(performance_data[['Workflow Name', 'Total Avg. Processing Time (min)', 'Error Rate (%)', 'Re-Work Rate (%)', 'Throughput (per hour)']])

if __name__ == "__main__":
    from dataset import load_datasets
    performance_data, _ = load_datasets('performance.csv', 'workflow_execution.csv')
    analyze_performance(performance_data)
