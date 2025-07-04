import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):  # Inherit from tk.Tk
    """
    A simple Tkinter application to display window information.
    """
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.geometry('300x200')
        self.resizable(width=False, height=False)
        self.title('My App')

        self.info_text = tk.Text(self, width=40, height=10)
        self.info_text.pack(side=tk.TOP, padx=5, pady=5)

        # It's better to define methods within the class
        # and use lambda or functools.partial if arguments are needed for commands.
        # Here, self is implicitly passed to instance methods.
        self.info_button = ttk.Button(self, text='Info', command=self.show_info)
        self.info_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.exit_button = ttk.Button(self, text='Exit', command=self.destroy)
        self.exit_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.info_button.focus_set()
        # self.configure(bg='black') # Example of setting background

    def show_info(self):
        """
        Displays information about the Tkinter root window in the text widget.
        """
        self.info_text.delete("1.0", tk.END)

        # Using f-strings for better readability
        info_messages = [
            f"Window Class: {self.winfo_class()}",
            f"Geometry: {self.winfo_geometry()}",
            f"Width: {self.winfo_width()}",
            f"Height: {self.winfo_height()}",
            f"Root X: {self.winfo_rootx()}",
            f"Root Y: {self.winfo_rooty()}",
            f"ID: {self.winfo_id()}",
            f"Name: {self.winfo_name()}",
            f"Window Manager: {self.winfo_manager()}"
        ]

        display_text = "\n".join(info_messages)
        self.info_text.insert("1.0", display_text)

def main():
    """
    Main function to create and run the Tkinter application.
    """
    app = Application()
    app.mainloop()  # The mainloop should be called on the app instance
    return 0

if __name__ == '__main__':
    main()