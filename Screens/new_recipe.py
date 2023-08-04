import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import os

from Database.database import *


class NewRecipe:
    def __init__(self, main, language):
        self.main = main
        self.language = language
        self.create_new_recipe_screen()

    def create_new_recipe_screen(self):
        new_recipe_frame = ctk.CTkFrame(self.main)
        new_recipe_frame.grid(column=0, row=0, sticky="nsew")
        new_recipe_frame.columnconfigure(0, weight=1)
        new_recipe_frame.rowconfigure((0, 2), weight=1)
        new_recipe_frame.rowconfigure(1, weight=10)
        # Header frame
        header_frame = ctk.CTkFrame(new_recipe_frame, height=10)
        header_frame.grid(column=0, row=0, sticky="nsew")
        header_frame.columnconfigure((0, 2), weight=1)
        header_frame.columnconfigure(1, weight=5)
        header_frame.rowconfigure(0, weight=1)
        back_image = ctk.CTkImage(
            light_image=Image.open("Foto/back_button1.png"),
            dark_image=Image.open("Foto/back_button.png"),
            size=(35, 35),
        )
        back_label = ctk.CTkLabel(header_frame, image=back_image, text="")
        back_label.grid(column=0, row=0, padx=5, pady=5, sticky="nw")
        back_label.bind("<Button-1>", self.main.create_start_screen)

        self.screen_name_label_var = ctk.StringVar(value="Dodaj novi recept")
        screen_name_label = ctk.CTkLabel(
            header_frame, textvariable=self.screen_name_label_var
        )
        screen_name_label.grid(column=1, row=0, padx=10, pady=5, sticky="ew")

        logo_image = ctk.CTkImage(
            light_image=Image.open("Foto/recipe1.png"),
            dark_image=Image.open("Foto/recipe.png"),
            size=(35, 35),
        )
        logo_label = ctk.CTkLabel(header_frame, image=logo_image, text="")
        logo_label.grid(column=2, row=0, padx=5, pady=5, sticky="ne")

        # Add recipe frame
        add_recipe_frame = ctk.CTkScrollableFrame(new_recipe_frame)
        add_recipe_frame.grid(column=0, row=1, sticky="nsew")
        add_recipe_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        add_recipe_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        self.name_label_var = ctk.StringVar(value="Naziv recepta")
        name_label = ctk.CTkLabel(add_recipe_frame, textvariable=self.name_label_var)
        name_label.grid(column=0, row=0, padx=10, pady=10)
        self.name_entry = ctk.CTkEntry(add_recipe_frame)
        self.name_entry.grid(column=1, row=0, padx=5, pady=10, ipadx=25)

        self.staple_food_label_var = ctk.StringVar(value="Glavna namirnica")
        staple_food_label = ctk.CTkLabel(
            add_recipe_frame, textvariable=self.staple_food_label_var
        )
        staple_food_label.grid(column=0, row=1, padx=10, pady=10)
        self.staple_food_entry = ctk.CTkEntry(add_recipe_frame)
        self.staple_food_entry.grid(column=1, row=1, padx=5, pady=10, ipadx=25)

        self.ingridients_label_var = ctk.StringVar(value="Sastojci")
        ingridients_label = ctk.CTkLabel(
            add_recipe_frame, textvariable=self.ingridients_label_var
        )
        ingridients_label.grid(column=0, row=2, padx=10, pady=10)
        self.ingridients_textbox = ctk.CTkTextbox(add_recipe_frame)
        self.ingridients_textbox.grid(column=1, row=2, rowspan=2, padx=5, pady=10)

        self.preparation_label_var = ctk.StringVar(value="Priprema")
        preparation_label = ctk.CTkLabel(
            add_recipe_frame, textvariable=self.preparation_label_var
        )
        preparation_label.grid(column=0, row=4, padx=10, pady=10)
        self.preparation_textbox = ctk.CTkTextbox(add_recipe_frame)
        self.preparation_textbox.grid(column=1, row=4, rowspan=2, padx=5, pady=10)

        self.protein_label_var = ctk.StringVar(value="Proteini")
        protein_label = ctk.CTkLabel(
            add_recipe_frame, textvariable=self.protein_label_var
        )
        protein_label.grid(column=2, row=0, padx=10, pady=10)
        self.protein_entry = ctk.CTkEntry(add_recipe_frame)
        self.protein_entry.grid(column=3, row=0, padx=5, pady=10, ipadx=25)

        self.carb_label_var = ctk.StringVar(value="Ugljikohidrati")
        carb_label = ctk.CTkLabel(add_recipe_frame, textvariable=self.carb_label_var)
        carb_label.grid(column=2, row=1, padx=10, pady=10)
        self.carb_entry = ctk.CTkEntry(add_recipe_frame)
        self.carb_entry.grid(column=3, row=1, padx=5, pady=10, ipadx=25)

        self.fat_label_var = ctk.StringVar(value="Masti")
        fat_label = ctk.CTkLabel(add_recipe_frame, textvariable=self.fat_label_var)
        fat_label.grid(column=2, row=2, padx=10, pady=10)
        self.fat_entry = ctk.CTkEntry(add_recipe_frame)
        self.fat_entry.grid(column=3, row=2, padx=5, pady=10, ipadx=25)

        self.prep_time_label_var = ctk.StringVar(value="Vrijeme pripreme")
        prep_time_label = ctk.CTkLabel(
            add_recipe_frame, textvariable=self.prep_time_label_var
        )
        prep_time_label.grid(column=2, row=3, padx=10, pady=10)
        self.prep_time_entry = ctk.CTkEntry(add_recipe_frame)
        self.prep_time_entry.grid(column=3, row=3, padx=5, pady=10, ipadx=25)

        self.category_label_var = ctk.StringVar(value="Kategorija jela")
        category_label = ctk.CTkLabel(
            add_recipe_frame, textvariable=self.category_label_var
        )
        category_label.grid(column=2, row=4, padx=10, pady=10)
        all_categories = db_get_all_categories()
        # TODO predati jezik i na temelju jezika dobit kategorije
        self.category_optionmenu_var = ctk.StringVar()
        self.category_entry = ctk.CTkOptionMenu(
            add_recipe_frame,
            values=[
                all_categories[0].name_hr,
                all_categories[1].name_hr,
                all_categories[2].name_hr,
                all_categories[3].name_hr,
            ],
            variable=self.category_optionmenu_var,
        )
        self.category_entry.grid(column=3, row=4, padx=5, pady=10, ipadx=25)

        self.foto_label_var = ctk.StringVar(value="Fotografija")
        foto_label = ctk.CTkLabel(add_recipe_frame, textvariable=self.foto_label_var)
        foto_label.grid(column=2, row=6, padx=10, pady=10)
        self.foto_entry = ctk.CTkEntry(add_recipe_frame)
        self.foto_entry.grid(column=3, row=6, padx=5, pady=10, ipadx=25)

        self.browse_button_var = ctk.StringVar(value="Odaberi")
        self.browse_button = ctk.CTkButton(
            add_recipe_frame,
            textvariable=self.browse_button_var,
            command=self.browse_photo,
        )
        self.browse_button.grid(column=4, row=6, pady=10)

        buttons_frame = ctk.CTkFrame(add_recipe_frame)
        buttons_frame.grid(column=5, row=0, rowspan=7, padx=10, pady=10)

        self.add_button_var = ctk.StringVar(value="Dodaj recept")
        add_button = ctk.CTkButton(
            buttons_frame, textvariable=self.add_button_var, command=self.add_recipe
        )
        add_button.grid(column=0, row=0, padx=5, pady=10, ipadx=10)

        self.clear_button_var = ctk.StringVar(value="Očisti")
        clear_button = ctk.CTkButton(buttons_frame, textvariable=self.clear_button_var)
        clear_button.grid(column=0, row=1, padx=5, pady=10, ipadx=10)

        # Footer frame
        footer_frame = ctk.CTkFrame(new_recipe_frame, height=30)
        footer_frame.grid(column=0, row=2, sticky="nsew")

    def browse_photo(self):
        file_path = fd.askopenfilename(
            initialdir="C:/",
            title="Odaberi sliku",
            filetypes=[("image", "*.jpg"), ("image", "*.png"), ("image", "*.jpeg")],
        )
        self.image = Image.open(file_path)
        self.foto_entry.insert(0, file_path)

    def add_recipe(self):
        self.image = self.image.save(f"Foto/Recipe_Foto/{self.name_entry.get()}.png")
        category_id = db_get_category_by_name(self.category_entry.get())
        db_add_new_recipe(
            self.name_entry.get(),
            self.staple_food_entry.get(),
            self.ingridients_textbox.get(1.0, ctk.END),
            self.preparation_textbox.get(1.0, ctk.END),
            self.protein_entry.get(),
            self.carb_entry.get(),
            self.fat_entry.get(),
            self.prep_time_entry.get(),
            category_id,
            f"Foto/Recipe_Foto/{self.name_entry.get()}.png",
        )
