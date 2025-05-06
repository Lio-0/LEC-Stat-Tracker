#
import tkinter as tk
from tkinter import messagebox
from setup import create_connection

cnx = create_connection(True)

# Function to execute a query and show results in the text area
def run_query(query):
    try:
        cursor = cnx.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        # Clear the output box and display column headers
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "\t".join(columns) + "\n" + "-"*50 + "\n")
        for row in results:
            result_text.insert(tk.END, "\t".join(str(cell) for cell in row) + "\n")

    except Exception as e:
        messagebox.showerror("Query Error", str(e))


if __name__ == "__main__":
        
    # GUI setup
    root = tk.Tk()
    root.title("MySQL Viewer")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Add buttons with custom queries
    tk.Button(frame, text="Show All Matches", command=lambda: run_query("SELECT * FROM Matches")).pack(fill='x', pady=2)

    # Text box to display query results
    result_text = tk.Text(root, wrap='none', height=20, width=80)
    result_text.pack(padx=10, pady=10)

    root.mainloop()

    cnx = create_connection(True)