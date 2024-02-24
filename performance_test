"""Compare performance of the two algorithms"""

import timeit
from floydwarshall.recursive_floydwarshall import floydwarshall_recursive
from floydwarshall.imperative_floydwarshall import floydwarshall_imperative
from floydwarshall.randomgraph_generator import generate_graph

graph = generate_graph(5,60)

# Define the number of times to repeat the timing measurements
repetitions = 30
execution_times_recursive = []
execution_times_imperative = []

# Repeat the timing measurements for the specified number of times
for _ in range(repetitions):
    # Measure the start time for the recursive function
    rec_start = timeit.default_timer()
    floydwarshall_recursive(graph)
    # Measure the time difference and append to the list of execution times
    execution_times_recursive.append(timeit.default_timer() - rec_start)

    # Measure the start time for the imperative function
    imp_start = timeit.default_timer()
    floydwarshall_imperative(graph)
    # Measure the time difference and append to the list of execution times
    execution_times_imperative.append(timeit.default_timer() - imp_start)

# Calculate the average execution time for the recursive function
avg_time_recursive = sum(execution_times_recursive) / repetitions

# Calculate the average execution time for the imperative function
avg_time_imperative = sum(execution_times_imperative) / repetitions

print(f"The recursive function took {avg_time_recursive:.10f} seconds on average",)
print(f"The imperative function took {avg_time_imperative:.10f} seconds on average",)
