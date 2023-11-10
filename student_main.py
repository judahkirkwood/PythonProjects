# Python Version:   3.11.6
#
# Author:           Judah Kirkwood
#
# Purpose:          Student Tracking App, Demonstrating OOP, Tkinter GUI module,
#                   using Tkinter Parent and Child relationships.
#
# Tested OS:        This code was written and tested to work with Windows 11.




import tkinter as tk
from tkinter import messagebox

class StudentTrackingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Tracking")

        # Initialize variables to store student information
        self.students = []

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Form to submit student information
        tk.Label(self.master, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Email:").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Current Course:").grid(row=4, column=0, padx=10, pady=5)

        self.first_name_entry = tk.Entry(self.master)
        self.last_name_entry = tk.Entry(self.master)
        self.phone_entry = tk.Entry(self.master)
        self.email_entry = tk.Entry(self.master)
        self.course_entry = tk.Entry(self.master)

        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)
        self.course_entry.grid(row=4, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.master, text="Submit", command=self.submit_student)
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Display section for the list of students
        tk.Label(self.master, text="List of Students", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=10)

        self.student_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=5)
        self.student_listbox.grid(row=7, column=0, columnspan=2, pady=5)
        self.student_listbox.bind("<<ListboxSelect>>", self.on_student_select)

        delete_button = tk.Button(self.master, text="Delete Selected", command=self.delete_student)
        delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def submit_student(self):
        # Get values from the entry widgets
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        course = self.course_entry.get()

        # Validate if all fields are filled
        if not all([first_name, last_name, phone, email, course]):
            messagebox.showwarning("Error", "Please fill in all fields.")
            return

        # Create a string to represent the student
        student = f"{first_name} {last_name} - {phone} - {email} - {course}"

        # Add the student to the list and update the listbox
        self.students.append(student)
        self.update_student_listbox()

        # Clear the entry fields after submission
        self.clear_entries()

    def update_student_listbox(self):
        # Clear the listbox
        self.student_listbox.delete(0, tk.END)

        # Populate the listbox with student information
        for student in self.students:
            self.student_listbox.insert(tk.END, student)

    def clear_entries(self):
        # Clear entry fields
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)

    def on_student_select(self, event):
        pass  # You can add functionality here if needed

    def delete_student(self):
        selected_index = self.student_listbox.curselection()
        if selected_index:
            # Remove the selected student from the list
            self.students.pop(selected_index[0])

            # Update the listbox
            self.update_student_listbox()

            # Display a confirmation message
            messagebox.showinfo("Success", "Selected student has been deleted.")
        else:
            messagebox.showwarning("Error", "Please select a student to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentTrackingApp(root)
    root.mainloop()

