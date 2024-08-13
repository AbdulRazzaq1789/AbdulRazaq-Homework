import tkinter as tk
import customtkinter as ctk
from dataclasses import dataclass, field
import typing
import os


class HomeworkApp:
    active_button = None

    @dataclass(eq=False, repr=False)
    class ButtonTabs:
        text: str
        parent: tk.Widget
        outer_instance: typing.Any = field(repr=False, compare=False)
        data: str = None
        state: bool = False

        def __post_init__(self):
            self.button = ctk.CTkButton(self.parent, text=self.text, font=("Arial", 14), corner_radius=0, height=40,
                                        text_color="black", fg_color="transparent", hover_color="#bbb", anchor="w",
                                        command=self.button_action)
            self.button.pack(fill="x", padx=(10, 0))

        def button_action(self):
            for button in self.outer_instance.button_tabs:
                button.button.configure(fg_color="transparent")
            self.button.configure(fg_color="#999")
            self.outer_instance.active_button = self
            self.outer_instance.label_variable.set(self.data)

    def __init__(self, tabs_data):
        self.root = ctk.CTk()
        self.root.geometry("750x400")
        self.root.title("Homework App")
        self.root.resizable(width=False, height=False)
        ctk.set_appearance_mode("light")

        self.tabs_data = tabs_data

        self.side_frame = ctk.CTkScrollableFrame(self.root, width=100, border_width=0, corner_radius=0)
        self.side_frame.pack(side="left", fill="y", expand=False)

        self.main_frame = ctk.CTkScrollableFrame(self.root, border_width=0, corner_radius=0)
        self.main_frame.pack(side="left", fill="both", expand=True)

        self.label_variable = ctk.StringVar()
        self.label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 16), anchor="nw",
                                  textvariable=self.label_variable, justify="left")
        self.label.pack(pady=10, padx=10, fill=ctk.BOTH, expand=True)
        self.label_variable.set("")

        self.button_tabs = []

        self.create_tabs()

        self.root.mainloop()

    def create_tabs(self):
        for line in self.tabs_data:
            content = "".join(line[1])
            button_tab = HomeworkApp.ButtonTabs(line[0], self.side_frame, outer_instance=self,
                                                data=content)
            self.button_tabs.append(button_tab)
        self.button_tabs[0].button_action()


main_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(main_dir, "files")

files = os.listdir(files_dir)
from natsort import natsorted

files = natsorted(files)
os.chdir(files_dir)
lst = []

for f in files:
    try:
        with open(f"{f}", "r") as file:
            data = file.readlines()
        if data:
            title = f
            lst.append((title, data))
    except Exception as e:
        print(f"Error reading file {f}: {e}")

HomeworkApp(lst)
