import tkinter as tk
from tkinter import messagebox, filedialog


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")
        self.root.config(bg="#f0f0f0")

        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.load_tasks)
        file_menu.add_command(label="Save", command=self.save_tasks)
        # file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)

        tk.Label(
            root, text="My To-Do List", font=("Arial", 16, "bold"), bg="#f0f0f0"
        ).pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=5)

        self.task_entry = tk.Entry(frame, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5)

        add_button = tk.Button(
            frame, text="Add Task", command=self.add_task, bg="#0078d7", fg="white"
        )
        add_button.grid(row=0, column=1, padx=5)

        self.listbox = tk.Listbox(root, width=45, height=15, selectbackground="#a6a6a6")
        self.listbox.pack(pady=10)

        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=5)

        tk.Button(
            btn_frame,
            text="Delete",
            command=self.delete_task,
            bg="#e81123",
            fg="white",
            width=10,
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame, text="Clear All", command=self.clear_all, bg="#ffb900", width=10
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            btn_frame,
            text="Mark Done",
            command=self.mark_done,
            bg="#107c10",
            fg="white",
            width=10,
        ).grid(row=0, column=2, padx=5)

        self.status_label = tk.Label(
            root, text="Welcome to To-Do App", bg="#f0f0f0", fg="gray"
        )
        self.status_label.pack(side="bottom", fill="x")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.status_label.config(text=f"Task added: {task}")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected = self.listbox.curselection()[0]
            task = self.listbox.get(selected)
            self.listbox.delete(selected)
            self.status_label.config(text=f"Deleted: {task}")
        except:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_all(self):
        self.listbox.delete(0, tk.END)
        self.status_label.config(text="All tasks cleared.")

    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            if not task.startswith("✔ "):
                self.listbox.delete(index)
                self.listbox.insert(index, "✔ " + task)
                self.status_label.config(text=f"Marked done: {task}")
        except:
            messagebox.showwarning("Selection Error", "Select a task to mark as done.")

    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        if tasks:
            file = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
            )
            if file:
                with open(file, "w") as f:
                    for task in tasks:
                        f.write(task + "\n")
                self.status_label.config(text="Tasks saved successfully.")
        else:
            messagebox.showinfo("No Tasks", "No tasks to save.")

    def load_tasks(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            self.listbox.delete(0, tk.END)
            with open(file, "r") as f:
                for line in f:
                    self.listbox.insert(tk.END, line.strip())
            self.status_label.config(text="Tasks loaded successfully.")

    def show_about(self):
        messagebox.showinfo(
            "About", "To-Do List App\nCreated using Tkinter\nBy: Aditya"
        )


# ---------- Main Program ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
