import tkinter as tk
from tkinter import filedialog

import ebooklib
from ebooklib import epub

# Colors
BACKGROUND_COLOR = "#F9F7E8"
PRIMARY_COLOR = "#FFCE67"
ACCENT_COLOR = "#FAD02C"
BUTTON_WIDTH = 8
PRIMARY_COLOR_PRESSED = "#FFB700"
ACCENT_COLOR_PRESSED = "#E6A100"

# Constants
APP_TITLE = "Epub Reader"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300

class OpenBook:
    def __init__(self, master, book, title):
        self.book = book
        self.master = master
        self.master.title(title)
        self.master.configure(bg=BACKGROUND_COLOR)
        self.master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.master.resizable(0, 0)
        self.get_content()
        # add widgets here

    def get_content(self):
        for item in self.book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                self.content = item.get_content()
                print("content received")
                # print(content)

class BookReader:
    def __init__(self, master):
        self.book = None #default variable for later
        self.master = master
        master.title(APP_TITLE)
        master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        master.configure(bg=BACKGROUND_COLOR)

        # heading
        heading = tk.Label(
            master,
            text="Book Reader",
            font=("Helvetica", 24),
            bg=BACKGROUND_COLOR,
            fg=PRIMARY_COLOR,
            pady=20,
        )
        heading.pack()

        # input file field
        input_frame = tk.Frame(master, bg=BACKGROUND_COLOR)
        input_frame.pack(pady=20)
        input_label = tk.Label(
            input_frame,
            text="Choose an epub file to open:",
            font=("Helvetica", 12),
            bg=BACKGROUND_COLOR,
            fg=PRIMARY_COLOR,
            padx=10,
            pady=10,
        )
        input_label.pack(side=tk.LEFT)
        self.input_var = tk.StringVar()
        input_entry = tk.Entry(
            input_frame,
            textvariable=self.input_var,
            width=25,
            font=("Helvetica", 12),
            bg="white",
            fg=PRIMARY_COLOR,
            borderwidth=2,
            relief=tk.FLAT,
        )
        input_entry.bind("<Button-1>", self.on_input_click)
        input_entry.pack(side=tk.LEFT)

        # buttons
        button_frame = tk.Frame(master, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)
        open_button = tk.Button(
            button_frame,
            text="Open",
            font=("Helvetica", 12),
            bg=PRIMARY_COLOR,
            fg="white",
            width=BUTTON_WIDTH,
            padx=10,
            pady=5,
            relief=tk.FLAT,
            activebackground=PRIMARY_COLOR_PRESSED,
            command=self.on_open_button_press,
        )
        open_button.pack(side=tk.LEFT, padx=10)
        like_button = tk.Button(
            button_frame,
            text="Like",
            font=("Helvetica", 12),
            bg=ACCENT_COLOR,
            fg="white",
            width=BUTTON_WIDTH,
            padx=10,
            pady=5,
            relief=tk.FLAT,
            activebackground=ACCENT_COLOR_PRESSED,
        )
        like_button.pack(side=tk.LEFT, padx=10)
        wish_button = tk.Button(
            button_frame,
            text="Wish",
            font=("Helvetica", 12),
            bg=ACCENT_COLOR,
            fg="white",
            width=BUTTON_WIDTH,
            padx=10,
            pady=5,
            relief=tk.FLAT,
            activebackground=ACCENT_COLOR_PRESSED,
        )
        wish_button.pack(side=tk.LEFT, padx=10)
        read_button = tk.Button(
            button_frame,
            text="Read",
            font=("Helvetica", 12),
            bg=ACCENT_COLOR,
            fg="white",
            width=BUTTON_WIDTH,
            padx=10,
            pady=5,
            relief=tk.FLAT,
            activebackground=ACCENT_COLOR_PRESSED,
        )
        read_button.pack(side=tk.LEFT, padx=10)

    def on_input_click(self, event):
        file_path = filedialog.askopenfilename(
            title="Choose an epub file", filetypes=[("epub files", "*.epub")]
        )
        if file_path:
            # Set input_var to file_path
            self.input_var.set(file_path)

            self.book = epub.read_epub(file_path) #t he variable with the file
            self.book_path = file_path # its location

    def on_open_button_press(self):
        # we need the title of the window to be same as the titke of the book
        book_title = self.book.get_metadata("DC", "title")[0][0] if self.book.get_metadata("DC", "title") else None 

        if book_title:
            root.withdraw()  # hide the main window
            open_window = tk.Toplevel()
            open_window.protocol("WM_DELETE_WINDOW", lambda: self.on_open_window_close(open_window))
            OpenBook(open_window, self.book, book_title)
        else:
            tk.messagebox.showerror(title="Error", message="This EPUB file does not have a title.")

    def on_open_window_close(self, window):
        window.destroy()
        root.deiconify()  # show the main window again


if __name__ == "__main__":
    root = tk.Tk()
    book_reader = BookReader(root)
    root.mainloop()
