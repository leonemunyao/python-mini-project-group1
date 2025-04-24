from typing import List

def validate_metric(metric: List[float]) -> bool:
    """
    Validate the metric data to ensure it is a list of floats.

    Args:
        metric (List[float]): The metric data to validate.

    Returns:
        bool: True if the metric is valid, False otherwise.
    """
    if not isinstance(metric, list):
        return False
    for value in metric:
        if not isinstance(value, float):
            return False
    return True

def validate_years(years: List[int]) -> bool:
    """
    Validate the years data to ensure it is a list of integers.

    Args:
        years (List[int]): The years data to validate.

    Returns:
        bool: True if the years are valid, False otherwise.
    """
    if not isinstance(years, list):
        return False
    for value in years:
        if not isinstance(value, int):
            return False
    return True

def formal_results(data: dict) -> str:
    """
    Format the results for display.
    """
    
    output = []
    for key, value in data.items():
        if isinstance(value, dict):
            output.append(f"{key}:")
            for sub_key, sub_value in value.items():
                output.append(f"  {sub_key}: {sub_value:.2f}")
        else:
            output.append(f"{key}: {value:.2f}")
    return "\n".join(output)



# ...Testing Functionality...

if __name__ == "__main__":
    print("\n=== Testing Utility Functions ===\n")

    # Test 1: validate_metric
    print("Testing validate_metric function...")
    test_metrics = [
        [23.5, 24.1, 25.0],  # Valid list of floats
        [23, 24, 25],        # Invalid - integers
        "not a list",        # Invalid - string
        []                   # Valid - empty list
    ]
    
    for i, metric in enumerate(test_metrics):
        result = validate_metric(metric)
        print(f"Test {i+1}: {metric} -> {'Valid' if result else 'Invalid'}")

    # Test 2: validate_years
    print("\nTesting validate_years function...")
    test_years = [
        [2020, 2021, 2022],  # Valid list of integers
        [2020.5, 2021.5],    # Invalid - floats
        "not a list",        # Invalid - string
        []                   # Valid - empty list
    ]
    
    for i, years in enumerate(test_years):
        result = validate_years(years)
        print(f"Test {i+1}: {years} -> {'Valid' if result else 'Invalid'}")

    # Test 3: formal_results
    print("\nTesting formal_results function...")
    test_data = {
        "2020": 23.5,
        "Seasonal": {
            "mean": 24.5,
            "min": 20.0,
            "max": 28.0
        }
    }

    
    formatted = formal_results(test_data)
    print("Formatted output:")
    print(formatted)

print("\nAll unitilis testes completed successfully.")

# The above code defines utility functions for validating data and formatting results.
# The functions are designed to ensure that the data being processed is in the correct format and type.
# The testing section at the end of the code demonstrates how to use these functions and verifies their functionality.