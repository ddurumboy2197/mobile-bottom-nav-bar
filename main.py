import tkinter as tk

class BottomNavigationBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile-Friendly Bottom Navigation Bar")
        self.root.geometry("300x500")

        self.bottom_frame = tk.Frame(self.root, bg="#333", height=50)
        self.bottom_frame.pack(fill="x", side="bottom")

        self.nav_buttons = [
            {"text": "Home", "command": self.home},
            {"text": "Search", "command": self.search},
            {"text": "Settings", "command": self.settings}
        ]

        for i, button in enumerate(self.nav_buttons):
            tk.Button(self.bottom_frame, text=button["text"], command=button["command"], bg="#444", fg="#fff", width=10, height=2).grid(row=0, column=i)

    def home(self):
        print("Home button clicked")

    def search(self):
        print("Search button clicked")

    def settings(self):
        print("Settings button clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = BottomNavigationBar(root)
    root.mainloop()
