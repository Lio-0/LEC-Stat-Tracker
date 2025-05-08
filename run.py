"""Main script for data viewer"""

import tkinter as tk
from tkinter import ttk, messagebox
from setup import create_connection


def run_query(query):
    """Runs string as SQL query"""

    global current_columns
    try:
        cursor = cnx.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        current_columns = columns  # Save current columns for sorting

        # Clear and configure the Treeview
        tree.delete(*tree.get_children())
        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: sort_by_column(c))
            tree.column(col, anchor='w', width=100)

        for row in results:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Query Error", str(e))

def sort_by_column(column):
    global current_table

    if not current_table:
        return

    # Toggle sort order
    order = current_sort_order.get(column, 'ASC')
    new_order = 'DESC' if order == 'ASC' else 'ASC'
    current_sort_order[column] = new_order

    query = f"SELECT * FROM {current_table} ORDER BY `{column}` {new_order}"
    run_query(query)

def show_table(table_name):
    global current_table
    current_table = table_name
    run_query(f"SELECT * FROM {table_name}")

if __name__ == "__main__":
    cnx = create_connection(True)
    current_sort_order = {}  # Keeps track of sort direction per column
    current_table = ""       # Keeps track of the currently displayed table

    root = tk.Tk()
    root.title("MySQL Viewer")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Buttons for loading tables
    tk.Button(frame, text="Show All Matches", command=lambda: show_table("Matches")).pack(fill='x', pady=2)
    tk.Button(frame, text="Show All Teams", command=lambda: show_table("Teams")).pack(fill='x', pady=2)
    tk.Button(frame, text="Show All Players", command=lambda: show_table("Players")).pack(fill='x', pady=2)
    tk.Button(frame, text="Show All Champions", command=lambda: show_table("Champions")).pack(fill='x', pady=2)
    tk.Button(frame, text="Show Team Statistics", command=lambda: show_table("TeamStatistics")).pack(fill='x', pady=2)

    # Treeview for displaying results
    tree = ttk.Treeview(root)
    tree.pack(padx=10, pady=10, fill='both', expand=True)

    root.mainloop()
