

import tkinter as tk
from tkinter import *
import tkinter.filedialog
from datetime import datetime, timedelta
import os

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("File Transfer")

        self.source_dir_label = Label(self, text="Source Directory:")
        self.source_dir_label.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir_entry = Entry(self, width=50)
        self.source_dir_entry.grid(row=0, column=1, padx=(0, 10), pady=(30, 0))

        self.sourceDir_btn = Button(self, text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=2, pady=(30, 0))

        self.destination_dir_label = Label(self, text="Destination Directory:")
        self.destination_dir_label.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir_entry = Entry(self, width=50)
        self.destination_dir_entry.grid(row=1, column=1, padx=(0, 10), pady=(15, 10))

        self.desDir_btn = Button(self, text="Select Destination", width=20, command=self.chooseDestination)
        self.desDir_btn.grid(row=1, column=2, pady=(15, 10))

        self.transfer_btn = Button(self, text="Transfer Files", width=20, command=self.chooseFiles)
        self.transfer_btn.grid(row=2, column=0, columnspan=3, pady=(15, 10))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir_entry.delete(0, END)
        self.source_dir_entry.insert(0, selectSourceDir)

    def chooseDestination(self):
        selectDestinationDir = tkinter.filedialog.askdirectory()
        self.destination_dir_entry.delete(0, END)
        self.destination_dir_entry.insert(0, selectDestinationDir)

    def chooseFiles(self):
        source_directory = self.source_dir_entry.get()
        destination_directory = self.destination_dir_entry.get()

        recently_modified_files = self.find_recently_modified_files(source_directory)

        if recently_modified_files:
            print("Recently modified/created files:")
            for file_path in recently_modified_files:
                print(file_path)
            # Add code here to transfer files to the destination directory
            print(f"Transferring files to: {destination_directory}")

        else:
            print("No recently modified/created files within the last 24 hours.")

    def find_recently_modified_files(self, directory, hours=24):
        current_time = datetime.now()
        threshold_time = current_time - timedelta(hours=hours)

        recently_modified_files = []

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                if modified_time >= threshold_time:
                    recently_modified_files.append(file_path)

        return recently_modified_files


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    App.grid(row=0, column=0)
    root.mainloop()


