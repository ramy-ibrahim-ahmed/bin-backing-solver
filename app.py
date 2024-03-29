import tkinter as tk
from tkinter import messagebox
import backtracking as bt

def run_backtracking():
    try:
        try:
            items = [int(item) for item in item_entry.get().split()]
            capacity = int(capacity_entry.get())
        except:
            raise ValueError("Invalid entry provided!")
        bins, solution, time = bt.solve(items, capacity)
        backtracking_result_label.config(
            text=f"Best solution: {solution}\nNumber of bins: {bins}\nTime: {time:.6f} seconds"
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)} :(")

root = tk.Tk()
root.title("Bin Packing Solver")

input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

item_label = tk.Label(input_frame, text="Enter items (separated by space):")
item_label.grid(row=0, column=0, padx=5, pady=5)
item_entry = tk.Entry(input_frame)
item_entry.grid(row=0, column=1, padx=5, pady=5)

capacity_label = tk.Label(input_frame, text="Enter capacity:")
capacity_label.grid(row=1, column=0, padx=5, pady=5)
capacity_entry = tk.Entry(input_frame)
capacity_entry.grid(row=1, column=1, padx=5, pady=5)

result_frame = tk.Frame(root, padx=10, pady=10)
result_frame.pack()

backtracking_button = tk.Button(result_frame, text="Run Backtracking", command=run_backtracking)
backtracking_button.grid(row=0, column=0, padx=5, pady=5)
backtracking_result_label = tk.Label(result_frame, text="")
backtracking_result_label.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()