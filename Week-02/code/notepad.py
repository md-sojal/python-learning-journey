# eventhough i said i wouldnt do any thing today i still enned up wanting to do a small programm
# we use tkinter to get gui and use filedialog to get file fith 
#and use messagebox to show users input
import tkinter as tk
from tkinter import filedialog, messagebox
#make funtion to help open new file 1.0 means first to last charecter and tk.end means everything till the text box end will be deleted
def new_file():
    text.delete(1.0, tk.END)

#make a function to open existing file, use ask open file name module and allow only .txt file to open and only files with a path cn open in a read mode
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*,txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# find file path thruog file dialog to save text to do this used asksaveasfile method
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("INfo", "File Saves successfully")

# creating root to call out gui window
root = tk.Tk()
root.title("My Own Text Editor")
root.geometry("800x600")

# creating menu 
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
