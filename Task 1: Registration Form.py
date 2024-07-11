import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not name or not email or not age or not gender or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number!")
        return
    
    messagebox.showinfo("Success", f"Name: {name}\nEmail: {email}\nAge: {age}\nGender: {gender}")

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set(None)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create a frame for the form
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(padx=10, pady=10)

# Create and place the labels and entry widgets
tk.Label(form_frame, text="Name").grid(row=0, column=0, sticky=tk.W, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Email").grid(row=1, column=0, sticky=tk.W, pady=5)
email_entry = tk.Entry(form_frame)
email_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Age").grid(row=2, column=0, sticky=tk.W, pady=5)
age_entry = tk.Entry(form_frame)
age_entry.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Gender").grid(row=3, column=0, sticky=tk.W, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky=tk.W)
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").grid(row=3, column=2, sticky=tk.W)
tk.Radiobutton(form_frame, text="Other", variable=gender_var, value="Other").grid(row=3, column=3, sticky=tk.W)

tk.Label(form_frame, text="Password").grid(row=4, column=0, sticky=tk.W, pady=5)
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=4, column=1, pady=5)

tk.Label(form_frame, text="Confirm Password").grid(row=5, column=0, sticky=tk.W, pady=5)
confirm_password_entry = tk.Entry(form_frame, show="*")
confirm_password_entry.grid(row=5, column=1, pady=5)

# Create and place the submit, clear, and quit buttons
button_frame = tk.Frame(root, pady=10)
button_frame.pack()

submit_button = tk.Button(button_frame, text="Submit", command=submit_form)
submit_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_form)
clear_button.grid(row=0, column=1, padx=10)

quit_button = tk.Button(button_frame, text="Quit", command=root.quit)
quit_button.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()
