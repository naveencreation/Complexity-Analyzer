import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import factorial



def show_front_page():
    
    def plot_time_complexity():
        x = np.linspace(1, 20, 100)

        complexities = {
            'O(1)': np.ones_like(x),
            'O(log n)': np.log(x + 1),
            'O(n)': x,
            'O(n log n)': x * np.log(x + 1),
            'O(n^2)': x**2,
            'O(2^n)': 2**x / 20,
            'O(n!)': [factorial(int(i)) / 20 for i in x],
        }

        plt.figure(figsize=(12, 8))
        for label, y in complexities.items():
            plt.plot(x, y, label=label)

        plt.title('Time Complexity Graphs')
        plt.xlabel('Input Size (n)')
        plt.ylabel('Operations Count')
        plt.ylim(0, 50)
        plt.legend()
        plt.grid()
        st.pyplot(plt)

    
    def plot_space_complexity():
        x = np.linspace(1, 20, 100)

        space_complexities = {
            'O(1)': np.ones_like(x),
            'O(n)': x,
            'O(n^2)': x**2,
        }

        plt.figure(figsize=(12, 8))
        for label, y in space_complexities.items():
            plt.plot(x, y, label=label)

        plt.title('Space Complexity Graphs')
        plt.xlabel('Input Size (n)')
        plt.ylabel('Memory Space Used')
        plt.ylim(0, 400)
        plt.legend()
        plt.grid()
        st.pyplot(plt)

    
    def create_summary_tables():
        time_complexity_data = {
            "Complexity Type": ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(2^n)", "O(n!)"],
            "Description": [
                "Constant time, independent of input size.",
                "Time grows logarithmically with input size.",
                "Time grows linearly with input size.",
                "Time grows in proportion to n * log(n).",
                "Time grows quadratically with input size.",
                "Time doubles with each additional input.",
                "Time grows factorially with input size."
            ],
            "Example Algorithms": [
                "Array indexing",
                "Binary search",
                "Linear search",
                "Merge sort, heapsort",
                "Bubble sort, selection sort",
                "Recursive Fibonacci",
                "Brute-force Traveling Salesman"
            ]
        }

        space_complexity_data = {
            "Space Complexity Type": ["O(1)", "O(n)", "O(n^2)"],
            "Description": [
                "Uses fixed space regardless of input size.",
                "Space grows linearly with input size.",
                "Space grows quadratically with input size."
            ],
            "Example": [
                "Variable swaps",
                "Storing copies of arrays",
                "Two-dimensional arrays"
            ]
        }

        time_complexity_df = pd.DataFrame(time_complexity_data)
        space_complexity_df = pd.DataFrame(space_complexity_data)

        st.subheader(":blue[Time Complexity Summary]")
        st.table(time_complexity_df)

        st.subheader(":blue[Space Complexity Summary]")
        st.table(space_complexity_df)

    st.markdown("<h1 style='text-align: center;'>Hello, I am <span style='color:#8a4af3;'>Naveen</span> 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;color:#2196f3'>Time and Space Complexity Visualizer</h1>", unsafe_allow_html=True)

    st.write("""
    This app visualizes different types of time and space complexities through graphs and tables.
    Understanding these complexities helps in analyzing algorithm performance.
    """)

    st.header(":blue[Time Complexity Graphs]")
    plot_time_complexity()

    st.header(":blue[Space Complexity Graphs]")
    plot_space_complexity()

    st.header("Complexity Summary Tables")
    create_summary_tables()

    st.write("""
    ---
    This application helps to visually understand how different algorithms behave with varying input sizes,
    both in terms of time and space usage.
    """)
    
