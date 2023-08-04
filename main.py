import random
from typing import Optional, Tuple, Union

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Screens import new_recipe, recipe


class FoodApp(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.font = ctk.CTkFont("Rockwell")
        self.geometry("800x600")
        self.iconbitmap("Foto/menu.ico")
        self.title("Food App")
        self.resizable(True, True)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.language_var = ctk.StringVar(value="Hrvatski")
        self.create_start_screen(self.language_var)

    def language_change(self, language):
        if language == "Hrvatski" or language == "Croatian" or language == "Kroatisch":
            self.breakfast_button_var.set("Doručak")
            self.lunch_button_var.set("Ručak")
            self.dinner_button_var.set("Večera")
            self.desert_button_var.set("Desert")
            self.new_recipe_button_var.set("Dodaj recept")
            self.random_recipe_button_var.set("Random recept")
            self.language_optionmenu.configure(
                values=["Hrvatski", "Engleski", "Njemački"]
            )
            self.language_optionmenu.set("Hrvatski")
        elif language == "Engleski" or language == "English" or language == "Englisch":
            self.breakfast_button_var.set("Breakfast")
            self.lunch_button_var.set("Lunch")
            self.dinner_button_var.set("Dinner")
            self.desert_button_var.set("Desert")
            self.new_recipe_button_var.set("Add new recipe")
            self.random_recipe_button_var.set("Random recipe")
            self.language_optionmenu.configure(values=["Croatian", "English", "German"])
            self.language_optionmenu.set("English")
        elif language == "Deutsch" or language == "German" or language == "Njemački":
            self.breakfast_button_var.set("Frühstück")
            self.lunch_button_var.set("Mittagessen")
            self.dinner_button_var.set("Abendessen")
            self.desert_button_var.set("Nachtisch")
            self.new_recipe_button_var.set("Füg ein neues Rezept hinzu")
            self.random_recipe_button_var.set("Zufälliges Rezept")
            self.language_optionmenu.configure(
                values=["Kroatisch", "Englisch", "Deutsch"]
            )
            self.language_optionmenu.set("Deutsch")

    def clear_self(self):
        for child in self.winfo_children():
            child.destroy()

    def create_start_screen(self, language):
        self.clear_self()
        start_screen_frame = ctk.CTkFrame(self)
        start_screen_frame.grid(column=0, row=0, sticky="nsew")
        start_screen_frame.grid_columnconfigure(0, weight=1)
        start_screen_frame.grid_rowconfigure((0, 2), weight=1)
        start_screen_frame.grid_rowconfigure(1, weight=5)

        # Header frame
        header_frame = ctk.CTkFrame(start_screen_frame)
        header_frame.grid(column=0, row=0, sticky="ew", pady=0)
        header_frame.columnconfigure(0, weight=1)
        header_frame.rowconfigure(0, weight=1)

        logo_image = ctk.CTkImage(
            light_image=Image.open("Foto/recipe1.png"),
            dark_image=Image.open("Foto/recipe.png"),
            size=(175, 175),
        )
        logo_label = ctk.CTkLabel(header_frame, image=logo_image, text="")
        logo_label.grid(column=0, row=0, padx=25, pady=25, sticky="ew")

        # Main menu frame
        main_menu_frame = ctk.CTkFrame(start_screen_frame)
        main_menu_frame.grid(column=0, row=1, sticky="nsew")
        main_menu_frame.columnconfigure(0, weight=1)
        main_menu_frame.rowconfigure(0, weight=1)

        # Buttons frame
        buttons_frame = ctk.CTkFrame(main_menu_frame)
        buttons_frame.grid(column=0, row=0, sticky="nsew")
        buttons_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        buttons_frame.rowconfigure((0, 1), weight=1)

        breakfast_logo = ctk.CTkImage(
            light_image=Image.open("Foto/breakfast1.png"),
            dark_image=Image.open("Foto/breakfast.png"),
            size=(50, 50),
        )
        self.breakfast_button_var = ctk.StringVar(value="Doručak")
        breakfast_button = ctk.CTkButton(
            buttons_frame,
            image=breakfast_logo,
            textvariable=self.breakfast_button_var,
            compound="top",
            command=lambda: self.create_new_screen(self.breakfast_button_var.get()),
        )
        breakfast_button.grid(column=0, row=0, padx=10, pady=10, ipadx=10)

        lunch_logo = ctk.CTkImage(
            light_image=Image.open("Foto/lunch1.png"),
            dark_image=Image.open("Foto/lunch.png"),
            size=(50, 50),
        )
        self.lunch_button_var = ctk.StringVar(value="Ručak")
        lunch_button = ctk.CTkButton(
            buttons_frame,
            image=lunch_logo,
            textvariable=self.lunch_button_var,
            compound="top",
            command=lambda: self.create_new_screen(self.lunch_button_var.get()),
        )
        lunch_button.grid(column=1, row=0, padx=10, pady=10, ipadx=10)

        snack_logo = ctk.CTkImage(
            light_image=Image.open("Foto/snack1.png"),
            dark_image=Image.open("Foto/snack.png"),
            size=(50, 50),
        )
        self.snack_button_var = ctk.StringVar(value="Snack")
        snack_button = ctk.CTkButton(
            buttons_frame,
            image=snack_logo,
            textvariable=self.snack_button_var,
            compound="top",
            command=lambda: self.create_new_screen(self.snack_button_var.get()),
        )
        snack_button.grid(column=2, row=0, padx=10, pady=10, ipadx=10)

        dinner_logo = ctk.CTkImage(
            light_image=Image.open("Foto/dinner1.png"),
            dark_image=Image.open("Foto/dinner.png"),
            size=(50, 50),
        )
        self.dinner_button_var = ctk.StringVar(value="Večera")
        dinner_button = ctk.CTkButton(
            buttons_frame,
            image=dinner_logo,
            textvariable=self.dinner_button_var,
            compound="top",
            command=lambda: self.create_new_screen(self.dinner_button_var.get()),
        )
        dinner_button.grid(column=3, row=0, padx=10, pady=10, ipadx=10)

        desert_logo = ctk.CTkImage(
            light_image=Image.open("Foto/desert1.png"),
            dark_image=Image.open("Foto/desert.png"),
            size=(50, 50),
        )
        self.desert_button_var = ctk.StringVar(value="Desert")
        desert_button = ctk.CTkButton(
            buttons_frame,
            image=desert_logo,
            textvariable=self.desert_button_var,
            compound="top",
            command=lambda: self.create_new_screen(self.desert_button_var.get()),
        )
        desert_button.grid(column=4, row=0, padx=10, pady=10, ipadx=10)

        new_recipe_logo = ctk.CTkImage(
            light_image=Image.open("Foto/add1.png"),
            dark_image=Image.open("Foto/add.png"),
            size=(50, 50),
        )
        self.new_recipe_button_var = ctk.StringVar(value="Dodaj recept")
        new_recipe_button = ctk.CTkButton(
            buttons_frame,
            image=new_recipe_logo,
            textvariable=self.new_recipe_button_var,
            compound="top",
            command=lambda: self.create_new_screen("new_recipe"),
        )
        new_recipe_button.grid(column=1, row=1, padx=10, pady=10, ipadx=10)

        random_recipe_logo = ctk.CTkImage(
            light_image=Image.open("Foto/random1.png"),
            dark_image=Image.open("Foto/random.png"),
            size=(50, 50),
        )
        self.random_recipe_button_var = ctk.StringVar(value="Random recept")
        random_recipe_button = ctk.CTkButton(
            buttons_frame,
            image=random_recipe_logo,
            textvariable=self.random_recipe_button_var,
            compound="top",
        )
        random_recipe_button.grid(column=3, row=1, padx=10, pady=10, ipadx=10)

        # Footer frame
        footer_frame = ctk.CTkFrame(start_screen_frame)
        footer_frame.grid(column=0, row=2, sticky="ew")

        self.language_optionmenu = ctk.CTkOptionMenu(
            footer_frame,
            variable=self.language_var,
            values=["Hrvatski", "Engleski", "Njemački"],
            command=self.language_change,
        )
        self.language_optionmenu.grid(column=0, row=0, padx=25, sticky="w")
        self.language_change(language)

    def create_new_screen(self, screen):
        self.clear_self()
        if screen == "new_recipe":
            new_recipe.NewRecipe(self, self.language_var.get())
        else:
            recipe.Recipe(self, self.language_var.get(), screen)


if __name__ == "__main__":
    app = FoodApp()
    app.mainloop()
