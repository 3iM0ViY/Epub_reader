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

class OpenBook(tk.Toplevel):
    def __init__(self, master, book, title):
        super().__init__(master, bg=BACKGROUND_COLOR)
        self.book = book
        self.book_title = title
        self.master = master
        self.master.title(title)
        self.master.configure(bg=BACKGROUND_COLOR)
        self.master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.master.wm_state('zoomed')
        self.master.resizable(0, 0)
        self.get_content()

        pages = ["This is page 1", "This is page 2", "This is page 3", "This is page 4"]
        
        self.pages = pages
        self.current_page = 0
        self.create_widgets()

    def get_content(self):
        for item in self.book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                self.content = item.get_content()
                print("content received")
                # print(content)

    def create_widgets(self):
        # Create title label
        self.master.title_label = tk.Label(self, text=self.book_title, font=("Arial", 16), bg=BACKGROUND_COLOR)
        self.master.title_label.pack(side="top", pady=10)

        # Create page frame
        self.master.page_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        self.master.page_frame.pack(side="top", pady=20)

        # Create left and right buttons
        left_button = tk.Button(
            self.page_frame,
            text="<",
            font=("Arial", 14),
            bg=PRIMARY_COLOR,
            fg="white",
            width=BUTTON_WIDTH,
            activebackground=PRIMARY_COLOR_PRESSED,
            command=self.turn_left,
        )
        left_button.pack(side=tk.LEFT)

        right_button = tk.Button(
            self.page_frame,
            text=">",
            font=("Arial", 14),
            bg=PRIMARY_COLOR,
            fg="white",
            width=BUTTON_WIDTH,
            activebackground=PRIMARY_COLOR_PRESSED,
            command=self.turn_right,
        )
        right_button.pack(side=tk.RIGHT)


        # Create page labels
        self.left_page_label = tk.Label(self.page_frame, text=self.pages[self.current_page], font=("Arial", 12), bg=BACKGROUND_COLOR)
        self.left_page_label.pack(side="left", padx=20)

        if len(self.pages) > 1:
            self.current_page = 1
            self.right_page_label = tk.Label(self.page_frame, text=self.pages[self.current_page], font=("Arial", 12), bg=BACKGROUND_COLOR)
            self.right_page_label.pack(side="right", padx=20)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="horizontal")
        self.scrollbar.pack(side="bottom", fill="x")
        
        # Bind scrollbar to page frame
        self.page_frame.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.page_frame.xview)

    def turn_left(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.right_page_label.config(text=self.pages[self.current_page])
            self.left_page_label.config(text=self.pages[self.current_page - 1])

    def turn_right(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.left_page_label.config(text=self.pages[self.current_page])
            if self.current_page < len(self.pages) - 1:
                self.right_page_label.config(text=self.pages[self.current_page + 1])
            else:
                self.right_page_label.config(text="")

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
