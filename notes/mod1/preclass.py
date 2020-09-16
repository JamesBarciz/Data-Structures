### Runtime Complexity
'''
- Constant time

For any input size (n), a constant time algorithm performs the same
number of operations every time.
Graphically: f(x) always the same output
Examples:
    - Fetching an element in an array using an index
    - Using a key to fetch a value in a hash table
Code:
```
def print_100th_element(array):
    print(array[99])

def loop_50_times(array):
    for i in range(50):
        print(array[i])
```
---------------------------------------------------------------------------

- Logarithmic time

^ number of operations it performs as a logarithmic function
of input (n) - Next best after constant time
Examples:
    - Looking up a word in a dictionary
        - Don't know exact page but have an idea where
    - Binary search - look for some entry in an already sorted list
Code:
```
def binary_search(sorted_arr, target):
    low = 0
    high = len(sorted_arr) - 1
    midpoint = (high - low) // 2
    if target == sorted_arr[midpoint]:
        return midpoint
    elif targer < sorted_arr[midpoint]:
        return binary_search(sorted_arr[:midpoint])
    else:
        return binary_search(sorted_arr[midpoint:])
```
--------------------------------------------------------------------------

- Linear time

# operations directly proportional to the size of (n)
Examples:
    - Counting
Code:
```
def search(array, target):  ### Not sorted
    for i in array:         ### Inspect array one element at a time
        if target == i:
            return True
    return False

def print_all_elements_twice(array):  ### O(2n) - two actions
    for i in array:
        print(i)
    for i in array:
        print(i)

def print_up_to_n(n):  ### O(n) = n
    for i in range(n):
        print(i)    
```
--------------------------------------------------------------------------

- Log-linear time

Looking over all elements we have and doing work on each one
Examples:
    - Sorting
        - look at every item in the array - n
        - rearrange elements in the array - log(n)
Code:
        - Algorithms
            - Quicksort
            - Mergesort
            - Heapsort
            - Timsort
--------------------------------------------------------------------------

- Quadratic time

n**c
elements = 10 --> operations = 100
elements = 100 --> operations = 1000000
Examples:
    - Enumerate all possible permutations of strings
    - Bubble sorting - elements moving through the entire array
Code:
```
def print_all_pairs(array):
    for first_item in array:
        for second_item in array:
            print(first_item, second_item)

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
```
--------------------------------------------------------------------------

- Exponential time
number of nested loops increases as n increases
Examples:
    - Cracking an unknown password
    - Decision problem form of the knapsack problem
    - Minesweeper consistency problem
    - Prime factorization or large integers
    - Longest common subsequence of strings problem
'''