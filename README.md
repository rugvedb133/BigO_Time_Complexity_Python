# Big O Notation for Time Complexity in Python

This is designed to understand the types of Big O notations using Python code.

### Initial Test

A plot function is created using the matplotlib pylot package. This is done to prevent repetitive statements


```python
import matplotlib.pyplot as plt
%matplotlib inline

def plot (xarr,yarr):
    plt.plot(xarr,yarr)
    plt.xlabel('n - array size')
    plt.ylabel('iterations - repeat counts')
    plt.title("Plot of size vs. Iterations")
    plt.show()
```

## Task 1

This task is just used to show the relation between array size and number of iterations. It is used to demonstrate the plot function.


```python
import random
# Test array 
arr = [ 2, 3, 4, 10, 40, 60, 80, 100]
x = 100

# The approach: create arrays to show the performance curve.
# task1: create the plot function.
# for each size N, save the number of iterations in an array.
size = [1, 2, 3, 4]
iters = [1, 4, 9, 16]

# and graph it
plot (size, iters)
```


![png](assets\output_7_0.png)


## Task 2

This function is used to return a single element from an array, and increments the count every time.


```python
def return_element (arr, i, count = 0):
    count+=1
    return arr[i], count
```


```python
import random
from plot import plot
arr = [10, 8, 6, 4, 2, 1]
x = 100
size = []
iters = []
for i in range(10):
    # task 2: create the return_element function
    # gen a random index into the array
    index = random.randint(0,len(arr)-1)
    result, count = return_element(arr, index)
    iters.append (count)
    size.append (len(arr))
    
    arr+=arr
    
plot (size, iters)
```


![png](assets\output_11_0.png)


In this function, the array is accessed only once, hence it is a constant time fucntion.
It is denoted by ***O(1)***

## Task 3

This is a bubble sort function. The array is accessed **n** times. Every access takes **n** iterations, and hence the whole operation takes **n<sup>2</sup>** iterations


```python
def bubble_sort(arr, count=0):
    for i in range(len(arr)):
        count+=1
        for j in range(len(arr)-1):
            count+=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr, count
```


```python
from plot import plot
arr = [10, 8, 6, 4, 2, 1]
x = 100
size = []
iters = []
for i in range(10):
    # task 3: Create the Bubblesort function
    # populate the array in reverse order (worst case)
    for j in range(len(arr)):
        arr[j] = len(arr) - j
    result, count = bubble_sort(arr)
    iters.append (count)
    size.append (len(arr))
    print("The array of size ", len(arr), "took ", count, "iterations")
    arr+=arr
    
plot (size, iters)
```

    The array of size  6 took  36 iterations
    The array of size  12 took  144 iterations
    The array of size  24 took  576 iterations
    The array of size  48 took  2304 iterations
    The array of size  96 took  9216 iterations
    The array of size  192 took  36864 iterations
    The array of size  384 took  147456 iterations
    The array of size  768 took  589824 iterations
    The array of size  1536 took  2359296 iterations
    The array of size  3072 took  9437184 iterations
    


![png](assets\output_16_1.png)


This is denoted as ***O(n<sup>2</sup>)***

## Task 4

This is the linear search function. The element being searched for is kept at the last position, to consider worst case scenario. Hence it takes **n** iterations. 


```python
def linear_search(arr, x, count=0):
    for i in range(len(arr)):
        count+=1
        if arr[i]==x:
            return i, count
    return -1, count
    
```


```python
import random
# Task 4: Create and analyze the linear search function
arr = [ 2, 3, 4, 10, 40, 60, 80, 100]
x = 100

# Function call 
size = []
iters = []
for i in range(10):
    result,count = linear_search(arr, x)
    
    iters.append (count)
    size.append (len(arr))
    if result != -1: 
       print("Element is present at index", str(result)) 
    else: 
       print("Element is not present in array") 
    print("The array of size ", len(arr), "took ", count, "iterations")
    arr+=arr
    arr[len(arr) -1 ] = 1000 + i
    x = 1000 + i

plot (size, iters)
```

    Element is present at index 7
    The array of size  8 took  8 iterations
    Element is present at index 15
    The array of size  16 took  16 iterations
    Element is present at index 31
    The array of size  32 took  32 iterations
    Element is present at index 63
    The array of size  64 took  64 iterations
    Element is present at index 127
    The array of size  128 took  128 iterations
    Element is present at index 255
    The array of size  256 took  256 iterations
    Element is present at index 511
    The array of size  512 took  512 iterations
    Element is present at index 1023
    The array of size  1024 took  1024 iterations
    Element is present at index 2047
    The array of size  2048 took  2048 iterations
    Element is present at index 4095
    The array of size  4096 took  4096 iterations
    


![png](assets\output_21_1.png)


This is denoted at ***O(n)***

## Task 5

This is the binary search funtion. It basically divides the sorted array into two halves, and after comparing the middle element, looks in the lower or higher half. It keeps repeating this process until the desired element is found. As array is divided into two halves, it takes **log<sub>2</sub>n** iterations


```python
def binary_search(arr, first, last, x, count=0):
    if last >= first:
        mid = (last + first)//2
        if arr[mid]==x:
            return mid, count
        elif x < arr[mid]:
            count+=1
            return binary_search(arr, first, mid-1, x, count)
        else:
            count+=1
            return binary_search(arr, mid+1, last, x, count)
    else:
        return -1, count
```


```python
import random

# task 5: Create and analyze the binary_search function
arr = [0, 10, 20, 30, 40, 50, 60]
x = 60
result, count = binary_search(arr, 0, len(arr)-1, x)
#initial test
# Test array 
arr = [ 2, 3, 4, 10, 40, 60, 80, 100]
x = 100
# Function call 
size = []
iters = []
for i in range(10):
    
    #task 4 -- using tuple
    result, count = binary_search(arr, 0, len(arr)-1, x)
    
    iters.append (count)
    size.append (len(arr))
    if result != -1: 
       print("Element is present at index", str(result)) 
    else: 
       print("Element is not present in array") 
    print("The array of size ", len(arr), "took ", count, "iterations")
    arr+=arr
    arr[len(arr) -1 ] = 1000 + i
    x = 1000 + i

plot (size, iters)
```

    Element is present at index 7
    The array of size  8 took  3 iterations
    Element is present at index 15
    The array of size  16 took  4 iterations
    Element is present at index 31
    The array of size  32 took  5 iterations
    Element is present at index 63
    The array of size  64 took  6 iterations
    Element is present at index 127
    The array of size  128 took  7 iterations
    Element is present at index 255
    The array of size  256 took  8 iterations
    Element is present at index 511
    The array of size  512 took  9 iterations
    Element is present at index 1023
    The array of size  1024 took  10 iterations
    Element is present at index 2047
    The array of size  2048 took  11 iterations
    Element is present at index 4095
    The array of size  4096 took  12 iterations
    


![png](assets\output_26_1.png)


This is represented as ***O(log <small>n</small>)***
