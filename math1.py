import streamlit as st

def show_complexity_page():
    st.title(":blue[Mathematical Derivations of Time and Space Complexity]")

    st.write("""
    This page provides detailed explanations and mathematical derivations for various types of time and space complexities commonly encountered in algorithms.
    """)

    # Constant Time Complexity: O(1)
    st.header("Constant Time Complexity: :violet[O(1)]")
    st.write("""
    **Explanation:**
    An algorithm is said to have constant time complexity if it performs a fixed number of operations regardless of the input size. No loops or recursions are involved.
    """)

    st.code("""
    def return_first_element(arr):
        return arr[0]
    """, language='python')

    st.write("**Mathematical Derivation:**")
    st.latex(r"T(n) = O(1)")

    # Linear Time Complexity: O(n)
    st.header("Linear Time Complexity: :violet[O(n)]")
    st.write("""
    **Explanation:**
    An algorithm has linear complexity when the number of operations scales directly in proportion to the size of the input. This is usually seen in algorithms that involve a single loop over the input elements.
    """)

    st.code("""
    def print_all_elements(arr):
        for i in arr:
            print(i)
    """, language='python')

    st.write("**Mathematical Derivation:**")
    st.latex(r"T(n) = c \cdot n")
    st.latex(r"T(n) = O(n)")

    # Quadratic Time Complexity: O(n²)
    st.header("Quadratic Time Complexity: :violet[O(n²)]")
    st.write("""
    **Explanation:**
    When an algorithm contains nested loops, where each loop runs `n` times, the overall time complexity becomes quadratic.
    """)

    st.code("""
    def print_all_pairs(arr):
        for i in arr:
            for j in arr:
                print(i, j)
    """, language='python')

    st.write("**Mathematical Derivation:**")
    st.latex(r"T(n) = c \cdot n \cdot n = c \cdot n^2")
    st.latex(r"T(n) = O(n^2)")

    # Logarithmic Time Complexity: O(log n)
    st.header("Logarithmic Time Complexity: :violet[O(log n)]")
    st.write("""
    **Explanation:**
    Algorithms with logarithmic time complexity reduce the size of the input at every step, typically by dividing it in half. This is common in search algorithms like binary search.
    """)

    st.code("""
    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    """, language='python')

    st.write("**Mathematical Derivation:**")
    st.latex(r"T(n) = \log_2 n")
    st.latex(r"T(n) = O(\log n)")

    # Linearithmic Time Complexity: O(n log n)
    st.header("Linearithmic Time Complexity: :violet[O(n log n)]")
    st.write("""
    **Explanation:**
    This complexity occurs in algorithms that split the input into two parts and recursively solve each part. These algorithms have `O(\log n)` recursive steps, and each step requires `O(n)` work.
    """)

    st.code("""
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            merge_sort(left)
            merge_sort(right)
            merge(left, right)
    """, language='python')

    st.write("**Mathematical Derivation:**")
    st.latex(r"T(n) = 2T\left(\frac{n}{2}\right) + O(n)")
    st.latex(r"T(n) = O(n \log n)")

    # Exponential Time Complexity: O(2^n)
    st.header("Exponential Time Complexity: :violet[O(2^n)]")
    st.write("""
    **Explanation:**
    Algorithms with exponential time complexity solve problems by exploring all possible solutions, which grows exponentially with the input size. This is common in problems like generating all subsets or permutations.
    """)

    st.code("""
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    """, language='python')

    st.write("**Mathematical Derivation:**")
    st.latex(r"T(n) \approx 2^n")
    st.latex(r"T(n) = O(2^n)")

    # Factorial Time Complexity: O(n!)
    st.header("Factorial Time Complexity: :violet[O(n!)]")
    st.write("""
    **Explanation:**
    Factorial time complexity is common in algorithms that generate all permutations or solve problems like the traveling salesman problem (TSP), where every possible arrangement needs to be explored.
    """)

    st.code("""
    from math import factorial

    def factorial_example(n):
        return factorial(n)
    """, language='python')

    st.write("**Mathematical Derivation:**")
    st.latex(r"T(n) = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 1 = O(n!)")

    # Space Complexity Section
    st.header("Space Complexity")
    st.write("""
    **Explanation:**
    Space complexity measures the amount of memory an algorithm uses as a function of the input size. This includes both:
    - **Auxiliary space**: Memory used by variables, arrays, or data structures.
    - **Recursive space**: Memory used by recursive function calls.
    """)

    st.code("""
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)
    """, language='python')

    st.write("**Space Complexity:**")
    st.latex(r"O(n)")

    st.code("""
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            merge_sort(left)
            merge_sort(right)
            merge(left, right)
    """, language='python')

    st.write("**Space Complexity:**")
    st.latex(r"O(n)")

    st.write("Feel free to reach out if you have any questions or need further clarifications!")

