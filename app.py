
import tkinter as tk
from tkinter import ttk, messagebox

from disk_algorithms import calculate_disk_scheduling


def calculate():
    try:
        cylinders = int(cylinder_entry.get())
        head = int(head_entry.get())

        requests = [
            int(x)
            for x in request_entry.get().replace(",", " ").split()
        ]

        if cylinders < 1:
            raise ValueError("Enter at least 1 cylinder.")

        if not 0 <= head < cylinders:
            raise ValueError(
                f"Head position must be between 0 and {cylinders - 1}."
            )

        if any(x < 0 or x >= cylinders for x in requests):
            raise ValueError(
                f"Requests must be between 0 and {cylinders - 1}."
            )

        algorithm = algorithm_box.get()
        direction = direction_box.get()

        result = calculate_disk_scheduling(
            requests, head, cylinders, algorithm, direction
        )

        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)

        result_box.insert(tk.END, "DISK SCHEDULING RESULTS\n")
        result_box.insert(tk.END, "=" * 38 + "\n\n")

        result_box.insert(tk.END, f"Algorithm: {algorithm}\n")
        result_box.insert(tk.END, f"Disk Cylinders: 0 to {cylinders - 1}\n")
        result_box.insert(tk.END, f"Initial Head Position: {head}\n\n")

        result_box.insert(tk.END, "Head Movement Sequence:\n")
        result_box.insert(
            tk.END,
            " -> ".join(map(str, result["sequence"])) + "\n\n"
        )

        result_box.insert(
            tk.END,
            f"Individual Movements: {result['movements']}\n"
        )
        result_box.insert(
            tk.END,
            f"Total Head Movement: {result['total']} cylinders\n"
        )
        result_box.insert(
            tk.END,
            f"Average Head Movement: {result['average']:.2f} cylinders\n"
        )

        result_box.config(state="disabled")

    except ValueError as error:
        messagebox.showerror("Input Error", str(error))


def clear_fields():
    cylinder_entry.delete(0, tk.END)
    head_entry.delete(0, tk.END)
    request_entry.delete(0, tk.END)

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")


# ==========================================
# APPLICATION WINDOW
# ==========================================

root = tk.Tk()
root.title("Disk Scheduling Algorithm Simulator")
root.geometry("500x620")
root.resizable(False, False)
root.configure(bg="#edf2f7")



tk.Label(
    root,
    text="DISK SCHEDULING",
    font=("Arial", 20, "bold"),
    bg="#edf2f7",
    fg="#1e293b"
).pack(pady=(15, 0))

tk.Label(
    root,
    text="ALGORITHM SIMULATOR",
    font=("Arial", 13, "bold"),
    bg="#edf2f7",
    fg="#2563eb"
).pack()

tk.Label(
    root,
    text="Operating System | Disk Management",
    font=("Arial", 9),
    bg="#edf2f7",
    fg="#64748b"
).pack(pady=(2, 12))


frame = tk.Frame(root, bg="white", padx=18, pady=12)
frame.pack(padx=20, fill="x")


def create_label(text, row):
    tk.Label(
        frame,
        text=text,
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#334155"
    ).grid(row=row, column=0, sticky="w", pady=7)


create_label("Number of Cylinders:", 0)

cylinder_entry = tk.Entry(frame, font=("Arial", 10), width=23)
cylinder_entry.grid(row=0, column=1, padx=8)

create_label("Initial Head Position:", 1)

head_entry = tk.Entry(frame, font=("Arial", 10), width=23)
head_entry.grid(row=1, column=1, padx=8)

create_label("Disk Request Queue:", 2)

request_entry = tk.Entry(frame, font=("Arial", 10), width=23)
request_entry.grid(row=2, column=1, padx=8)

tk.Label(
    frame,
    text="Example: 21, 43, 65, 99, 120",
    font=("Arial", 8),
    bg="white",
    fg="#64748b"
).grid(row=3, column=1, sticky="w", padx=8)

create_label("Algorithm:", 4)

algorithm_box = ttk.Combobox(
    frame,
    values=["FIFO", "SSTF", "LOOK", "ELEVATOR", "C-SCAN"],
    state="readonly",
    width=20
)
algorithm_box.grid(row=4, column=1, padx=8)
algorithm_box.set("FIFO")

create_label("Head Direction:", 5)

direction_box = ttk.Combobox(
    frame,
    values=["Up", "Down"],
    state="readonly",
    width=20
)
direction_box.grid(row=5, column=1, padx=8)
direction_box.set("Up")



buttons = tk.Frame(root, bg="#edf2f7")
buttons.pack(pady=12)

tk.Button(
    buttons,
    text="CALCULATE",
    command=calculate,
    font=("Arial", 10, "bold"),
    bg="#2563eb",
    fg="white",
    width=14,
    pady=6,
    cursor="hand2"
).grid(row=0, column=0, padx=6)

tk.Button(
    buttons,
    text="CLEAR",
    command=clear_fields,
    font=("Arial", 10, "bold"),
    bg="#64748b",
    fg="white",
    width=14,
    pady=6,
    cursor="hand2"
).grid(row=0, column=1, padx=6)


# ==========================================
# SIMULATION RESULTS
# ==========================================

tk.Label(
    root,
    text="SIMULATION RESULTS",
    font=("Arial", 11, "bold"),
    bg="#edf2f7",
    fg="#1e293b"
).pack(pady=(2, 5))

result_box = tk.Text(
    root,
    height=11,
    width=57,
    font=("Consolas", 9),
    bg="white",
    fg="#1e293b",
    padx=10,
    pady=8,
    wrap="word",
    state="disabled"
)
result_box.pack(padx=20, pady=(0, 12))



root.mainloop()
