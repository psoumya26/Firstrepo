import numpy as np

def main():
    print("--- Numpy Example ---")
    # Create a 1D array
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Created Array: {arr}")
    
    # Perform some basic mathematical operations
    print(f"Mean of array: {np.mean(arr)}")
    print(f"Sum of array: {np.sum(arr)}")
    print(f"Standard Deviation: {np.std(arr):.2f}")

if __name__ == "__main__":
    main()
