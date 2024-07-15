import time
from optimization import optimize_workflow

def measure_performance(steps):
    start_time = time.time()
    results = optimize_workflow(steps)
    end_time = time.time()
    processing_time = end_time - start_time
    return processing_time

if __name__ == "__main__":
    from bottleneck import identify_bottlenecks
    from dataset import load_datasets
    _, workflow_execution_data = load_datasets('performance.csv', 'workflow_execution.csv')
    manual_interventions = identify_bottlenecks(workflow_execution_data)
    steps_to_optimize = manual_interventions['Step'].unique()

    # Measure performance before optimization
    before_optimization_time = measure_performance(steps_to_optimize)
    print(f"Processing Time Before Optimization: {before_optimization_time:.2f} seconds")

    # Implement optimization (already done in previous step)
    optimized_results = optimize_workflow(steps_to_optimize)

    # Measure performance after optimization
    after_optimization_time = measure_performance(steps_to_optimize)
    print(f"Processing Time After Optimization: {after_optimization_time:.2f} seconds")

    # Calculate efficiency gains
    efficiency_gain = before_optimization_time - after_optimization_time
    print(f"Efficiency Gain: {efficiency_gain:.2f} seconds")
