import os
import tkinter as tk
from tkinter import filedialog, messagebox
from google_images_search import GoogleImagesSearch

# Function to execute image search
def search_images():
    try:
        api_key = api_key_entry.get()
        cx = cx_entry.get()
        query = query_entry.get()
        num_images = int(num_entry.get())
        file_type = file_type_var.get()
        safe_search = 'active' if safe_var.get() else 'off'
        download_dir = dir_label.cget("text")

        if not all([api_key, cx, query, download_dir]):
            messagebox.showerror("Error", "Please fill all required fields!")
            return

        # Initialize GoogleImagesSearch
        gis = GoogleImagesSearch(api_key, cx)
        _search_params = {
            'q': query,
            'num': num_images,
            'safe': safe_search,
            'fileType': file_type,
        }

        # Perform the search
        gis.search(search_params=_search_params, path_to_dir=download_dir)

        messagebox.showinfo("Success", f"Images downloaded to: {download_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to select directory
def select_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        dir_label.config(text=dir_path)

# Initialize Tkinter
root = tk.Tk()
root.title("Google Images Search")

# API Key and CX
tk.Label(root, text="API Key:").grid(row=0, column=0, sticky="w")
api_key_entry = tk.Entry(root, width=40)
api_key_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="CX:").grid(row=1, column=0, sticky="w")
cx_entry = tk.Entry(root, width=40)
cx_entry.grid(row=1, column=1, pady=5)

# Query and number of images
tk.Label(root, text="Search Query:").grid(row=2, column=0, sticky="w")
query_entry = tk.Entry(root, width=40)
query_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Number of Images:").grid(row=3, column=0, sticky="w")
num_entry = tk.Entry(root, width=10)
num_entry.insert(0, "20")
num_entry.grid(row=3, column=1, sticky="w", pady=5)

# File type and safe search
tk.Label(root, text="File Type:").grid(row=4, column=0, sticky="w")
file_type_var = tk.StringVar(value="jpg")
file_type_menu = tk.OptionMenu(root, file_type_var, "jpg", "png", "bmp")
file_type_menu.grid(row=4, column=1, sticky="w", pady=5)

safe_var = tk.IntVar()
safe_check = tk.Checkbutton(root, text="Safe Search", variable=safe_var)
safe_check.grid(row=5, column=1, sticky="w", pady=5)

# Directory selection
tk.Label(root, text="Download Directory:").grid(row=6, column=0, sticky="w")
dir_label = tk.Label(root, text="Not selected", width=40, anchor="w", relief="sunken")
dir_label.grid(row=6, column=1, pady=5)
dir_button = tk.Button(root, text="Browse", command=select_directory)
dir_button.grid(row=6, column=2, pady=5)

# Start button
start_button = tk.Button(root, text="Start Search", command=search_images)
start_button.grid(row=7, column=1, pady=10)

# Run the application
root.mainloop()
