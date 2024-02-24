# Recursive Floyd Warshall algorithm

In this project we created a new version of the Floyd Warshall algorithm that uses recursion. We also created a function that create random graph to use in the unit and performance tests.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Testing](#testing)
- [License](#license)

## Installation

To use the Floyd-Warshall algorithm implementations, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/stefanopalu/midmodule_assignment.git
    ```

2. Install the required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

## Usage

You can use the provided implementations of the Floyd-Warshall algorithm by importing them into your Python code. Here's an example of how to use the recursive implementation:

```python
from floydwarshall.recursive_floydwarshall import floydwarshall_recursive

# Example usage with a graph represented as an adjacency matrix
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

distances = floyd_warshall(graph)
print(distances)
```

## Directory Structure

The directory structure of this project is organized as follows:

```
midmodule_assignment/
├─── LICENSE
├─── README.md
├─── requirements.txt
├─── performance_tests.py
├─── unit_test.py
├─── floydwarshall/
    ├─── __init__.py
    ├─── imperative_floydwarshall.py
    ├─── recursive_floydwarshall.py
    ├─── randomgraph_generator.py
```

## Testing 

This project includes a suite of unit tests to verify the correctness of the recursive version of the Floyd-Warshall algorithm. The unit tests cover various scenarios and edge cases to ensure the algorithms produce accurate results under different conditions. These tests compare the outputs of the implementations with the expected results, using the imperative version of the algorithm as a benchmark for correctness.
You can run the tests using the following command:

```
python -m unittest unit_test.py
```

In addition to unit tests, performance tests are available to evaluate the efficiency of the implementations.

You can run the performance tests using the following command:

```
python performance_test.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)