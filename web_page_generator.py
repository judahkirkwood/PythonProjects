import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Label for instructions
        self.instructions_label = Label(self.master, text="Enter custom text or click the Default HTML page button.")
        self.instructions_label.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 5))

        # Entry for user input
        self.custom_text_entry = Entry(self.master, width=50)
        self.custom_text_entry.grid(row=1, column=0, columnspan=2, padx=(10, 10), pady=(5, 10))

        # Button setup for Submit Custom Text
        self.btn_custom = Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.customHTML)
        self.btn_custom.grid(row=2, column=1, padx=(10, 5), pady=(10, 10))

        # Button setup for Default HTML
        self.btn_default = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=2, column=0, padx=(5, 10), pady=(10, 10))

    def defaultHTML(self):
        html_text = "Stay tuned for our amazing summer sale!"
        self.generateHTML(html_text)

    def customHTML(self):
        html_text = self.custom_text_entry.get()
        self.generateHTML(html_text)

    def generateHTML(self, html_text):
        html_file = open("index.html", "w")
        html_content = f"<html>\n<body>\n<h1>{html_text}</h1>\n</body>\n</html>"
        html_file.write(html_content)
        html_file.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

