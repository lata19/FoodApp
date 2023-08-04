import tkinter as tk
from typing import Any
import os

import customtkinter as ctk
from PIL import Image, ImageTk

from Database.database import *


class Recipe:
    def __init__(self, main, language, meal):
        self.main = main
        self.language = language
        self.meal = meal
        self.language_var = ctk.StringVar(value=self.language)
        self.create_recipe_screen(self.meal)
        self.language_change(self.language, self.all_categories, self.meal)

    def language_change(self, language, all_categories, meal):
        if language == "Hrvatski" or language == "Croatian" or language == "Kroatisch":
            if meal in ["Doručak", "Breakfast", "Frühstück"]:
                self.header_label_var.set("Doručak")
            elif meal in ["Ručak", "Lunch", "Mittagessen"]:
                self.header_label_var.set("Ručak")
            elif meal in ["Večera", "Dinner", "Abendessen"]:
                self.header_label_var.set("Večera")
            elif meal in ["Desert", "Nachtisch"]:
                self.header_label_var.set("Desert")
            elif meal == "Snack":
                self.header_label_var.set("Snack")
            self.name_label_var.set("Naziv recepta")
            self.staple_food_label_var.set("Glavna namirnica")
            self.ingridients_label_var.set("Sastojci")
            self.preparation_label_var.set("Priprema")
            self.protein_label_var.set("Proteini")
            self.carb_label_var.set("Ugljikohidrati")
            self.fat_label_var.set("Masti")
            self.prep_time_label_var.set("Vrijeme pripreme")
            self.category_label_var.set("Kategorija jela")
            self.category_optionmenu.configure(
                values=[
                    all_categories[0].name_hr,
                    all_categories[1].name_hr,
                    all_categories[2].name_hr,
                    all_categories[3].name_hr,
                ]
            )
            self.language_optionmenu.configure(
                values=["Hrvatski", "Engleski", "Njemački"]
            )
            self.language_optionmenu.set("Hrvatski")
            self.edit_switch_var.set("Uredi")
            self.update_button_var.set("Ažuriraj")
            self.delete_button_var.set("Izbriši")
        elif language == "Engleski" or language == "English" or language == "Englisch":
            if meal in ["Doručak", "Breakfast", "Frühstück"]:
                self.header_label_var.set("Breakfast")
            elif meal in ["Ručak", "Lunch", "Mittagessen"]:
                self.header_label_var.set("Lunch")
            elif meal in ["Večera", "Dinner", "Abendessen"]:
                self.header_label_var.set("Dinner")
            elif meal in ["Desert", "Nachtisch"]:
                self.header_label_var.set("Desert")
            self.name_label_var.set("Name of the recipe")
            self.staple_food_label_var.set("The main food")
            self.ingridients_label_var.set("Ingredients")
            self.preparation_label_var.set("Preparation")
            self.protein_label_var.set("Proteins")
            self.carb_label_var.set("Carbohydrates")
            self.fat_label_var.set("Fats")
            self.prep_time_label_var.set("Preparation time")
            self.category_label_var.set("Category")
            self.category_optionmenu.configure(
                values=[
                    all_categories[0].name_en,
                    all_categories[1].name_en,
                    all_categories[2].name_en,
                    all_categories[3].name_en,
                ]
            )
            self.language_optionmenu.configure(values=["Croatian", "English", "German"])
            self.language_optionmenu.set("English")
            self.edit_switch_var.set("Edit")
            self.update_button_var.set("Update")
            self.delete_button_var.set("Delete")
        elif language == "Deutsch" or language == "German" or language == "Njemački":
            if meal in ["Doručak", "Breakfast", "Frühstück"]:
                self.header_label_var.set("Frühstück")
            elif meal in ["Ručak", "Lunch", "Mittagessen"]:
                self.header_label_var.set("Mittagessen")
            elif meal in ["Večera", "Dinner", "Abendessen"]:
                self.header_label_var.set("Abendessen")
            elif meal in ["Desert", "Nachtisch"]:
                self.header_label_var.set("Nachtisch")
            self.name_label_var.set("Name des Rezepts")
            self.staple_food_label_var.set("Das Hauptessen")
            self.ingridients_label_var.set("Zutaten")
            self.preparation_label_var.set("Vorbereitung")
            self.protein_label_var.set("Proteine")
            self.carb_label_var.set("Kohlenhydrate")
            self.fat_label_var.set("Fette")
            self.prep_time_label_var.set("Vorbereitungszeit")
            self.category_label_var.set("Kategorie")
            self.category_optionmenu.configure(
                values=[
                    all_categories[0].name_de,
                    all_categories[1].name_de,
                    all_categories[2].name_de,
                    all_categories[3].name_de,
                ]
            )
            self.language_optionmenu.configure(
                values=["Kroatisch", "Englisch", "Deutsch"]
            )
            self.language_optionmenu.set("Deutsch")
            self.edit_switch_var.set("Bearbeiten")
            self.update_button_var.set("Aktualisieren")
            self.delete_button_var.set("Löschen")
        if self.single_recipe_frame.winfo_ismapped():
            self.create_info_frame(self.recipe, self.language_var.get())

    def create_recipe_screen(self, meal):
        recipe_frame = ctk.CTkFrame(self.main)
        recipe_frame.grid(column=0, row=0, sticky="nsew")
        recipe_frame.columnconfigure(0, weight=1)
        recipe_frame.rowconfigure((0, 2), weight=1)
        recipe_frame.rowconfigure(1, weight=10)

        # Header frame
        header_frame = ctk.CTkFrame(recipe_frame, height=10)
        header_frame.grid(column=0, row=0, sticky="nsew")
        header_frame.columnconfigure((0, 2), weight=1)
        header_frame.columnconfigure(1, weight=10)
        # header_frame.rowconfigure(0, weight=1)

        # Buttons
        header_buttons_frame = ctk.CTkFrame(header_frame, height=10)
        header_buttons_frame.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
        back_image = ctk.CTkImage(
            light_image=Image.open("Foto/back_button1.png"),
            dark_image=Image.open("Foto/back_button.png"),
            size=(35, 35),
        )
        back_label = ctk.CTkLabel(header_buttons_frame, image=back_image, text="")
        back_label.grid(column=0, row=0, padx=5, pady=5)
        back_label.bind(
            "<Button-1>",
            lambda e: self.main.create_start_screen(self.language_var.get()),
        )

        self.header_label_var = ctk.StringVar(value=meal)
        header_label = ctk.CTkLabel(
            header_frame, textvariable=self.header_label_var, height=10
        )
        header_label.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")

        logo_frame = ctk.CTkFrame(header_frame, height=10)
        logo_frame.grid(column=2, row=0, padx=10, pady=10, sticky="nsew")

        # Main frame
        main_recipe_frame = ctk.CTkFrame(recipe_frame)
        main_recipe_frame.grid(column=0, row=1, sticky="nsew")
        main_recipe_frame.columnconfigure((0, 1), weight=1)
        main_recipe_frame.columnconfigure((2, 3, 4), weight=2)
        main_recipe_frame.rowconfigure(0, weight=1)

        # Recipe list
        recipe_list_frame = ctk.CTkScrollableFrame(main_recipe_frame)
        recipe_list_frame.grid(column=0, row=0, columnspan=2, rowspan=9, sticky="nsew")

        # Recipe info
        self.single_recipe_frame = ctk.CTkFrame(main_recipe_frame)
        # Photo
        self.photo_label = ctk.CTkLabel(self.single_recipe_frame, text="")
        self.photo_label.grid(
            column=0, row=0, columnspan=2, rowspan=2, padx=10, pady=10
        )

        self.name_label_var = ctk.StringVar(value="Naziv recepta")
        name_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.name_label_var
        )
        name_label.grid(column=2, row=0, padx=5, pady=10)
        self.name_entry_var = ctk.StringVar(value="")
        self.name_entry = ctk.CTkEntry(
            self.single_recipe_frame, textvariable=self.name_entry_var, state="disabled"
        )
        self.name_entry.grid(column=3, columnspan=2, row=0, padx=5, pady=5, ipadx=25)

        self.staple_food_label_var = ctk.StringVar(value="Glavna namirnica")
        staple_food_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.staple_food_label_var
        )
        staple_food_label.grid(column=2, row=1, padx=5, pady=10)
        self.staple_food_entry_var = ctk.StringVar(value="")
        self.staple_food_entry = ctk.CTkEntry(
            self.single_recipe_frame,
            textvariable=self.staple_food_entry_var,
            state="disabled",
        )
        self.staple_food_entry.grid(column=3, row=1, padx=5, pady=10, ipadx=25)

        self.ingridients_label_var = ctk.StringVar(value="Sastojci")
        ingridients_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.ingridients_label_var
        )
        ingridients_label.grid(column=0, row=2, padx=10, pady=10)
        self.ingridients_textbox_var = ctk.StringVar(value="")
        self.ingridients_textbox = ctk.CTkTextbox(self.single_recipe_frame)
        self.ingridients_textbox.grid(column=1, row=2, rowspan=2, padx=5, pady=10)

        self.preparation_label_var = ctk.StringVar(value="Priprema")
        preparation_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.preparation_label_var
        )
        preparation_label.grid(column=0, row=4, padx=10, pady=10)
        self.preparation_textbox_var = ctk.StringVar(value="")
        self.preparation_textbox = ctk.CTkTextbox(self.single_recipe_frame)
        self.preparation_textbox.grid(column=1, row=4, rowspan=2, padx=5, pady=10)

        self.protein_label_var = ctk.StringVar(value="Proteini")
        protein_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.protein_label_var
        )
        protein_label.grid(column=2, row=2, padx=10, pady=10)
        self.protein_entry_var = ctk.StringVar(value="")
        self.protein_entry = ctk.CTkEntry(
            self.single_recipe_frame,
            textvariable=self.protein_entry_var,
            state="disabled",
        )
        self.protein_entry.grid(column=3, row=2, padx=5, pady=10, ipadx=25)

        self.carb_label_var = ctk.StringVar(value="Ugljikohidrati")
        carb_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.carb_label_var
        )
        carb_label.grid(column=2, row=3, padx=10, pady=10)
        self.carb_entry_var = ctk.StringVar(value="")
        self.carb_entry = ctk.CTkEntry(
            self.single_recipe_frame, textvariable=self.carb_entry_var, state="disabled"
        )
        self.carb_entry.grid(column=3, row=3, padx=5, pady=10, ipadx=25)

        self.fat_label_var = ctk.StringVar(value="Masti")
        fat_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.fat_label_var
        )
        fat_label.grid(column=2, row=4, padx=10, pady=10)
        self.fat_entry_var = ctk.StringVar(value="")
        self.fat_entry = ctk.CTkEntry(
            self.single_recipe_frame, textvariable=self.fat_entry_var, state="disabled"
        )
        self.fat_entry.grid(column=3, row=4, padx=5, pady=10, ipadx=25)

        self.prep_time_label_var = ctk.StringVar(value="Vrijeme pripreme")
        prep_time_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.prep_time_label_var
        )
        prep_time_label.grid(column=2, row=5, padx=10, pady=10)
        self.prep_time_entry_var = ctk.StringVar(value="")
        self.prep_time_entry = ctk.CTkEntry(
            self.single_recipe_frame,
            textvariable=self.prep_time_entry_var,
            state="disabled",
        )
        self.prep_time_entry.grid(column=3, row=5, padx=5, pady=10, ipadx=25)

        self.category_label_var = ctk.StringVar(value="Kategorija jela")
        category_label = ctk.CTkLabel(
            self.single_recipe_frame, textvariable=self.category_label_var
        )
        category_label.grid(column=2, row=6, padx=10, pady=10)

        self.all_categories = db_get_all_categories()
        self.category_optionmenu_var = ctk.StringVar(value="")
        self.category_optionmenu = ctk.CTkOptionMenu(
            self.single_recipe_frame,
            values=[
                self.all_categories[0].name_hr,
                self.all_categories[1].name_hr,
                self.all_categories[2].name_hr,
                self.all_categories[3].name_hr,
            ],
            variable=self.category_optionmenu_var,
            state="disabled",
        )
        self.category_optionmenu.grid(column=3, row=6, padx=5, pady=10, ipadx=25)

        buttons_frame = ctk.CTkFrame(self.single_recipe_frame)
        buttons_frame.grid(column=5, row=0, padx=10, pady=10)

        self.edit_switch_var = ctk.StringVar(value="Uredi")
        self.edit_switch_state_var = ctk.StringVar(value="off")
        edit_switch = ctk.CTkSwitch(
            buttons_frame,
            textvariable=self.edit_switch_var,
            variable=self.edit_switch_state_var,
            onvalue="on",
            offvalue="off",
            command=self.edit_recipe,
        )
        edit_switch.grid(column=0, row=0, padx=10, pady=10)

        self.update_button_var = ctk.StringVar(value="Ažuriraj")
        update_button = ctk.CTkButton(
            buttons_frame, textvariable=self.update_button_var
        )
        update_button.grid(column=0, row=1, padx=10, pady=10, ipadx=10)

        self.delete_button_var = ctk.StringVar(value="Izbriši")
        delete_button = ctk.CTkButton(
            buttons_frame, textvariable=self.delete_button_var
        )
        delete_button.grid(column=0, row=2, padx=10, pady=10, ipadx=10)

        # Footer frame
        footer_frame = ctk.CTkFrame(recipe_frame, height=10)
        footer_frame.grid(column=0, row=2, sticky="nsew")

        self.language_optionmenu = ctk.CTkOptionMenu(
            footer_frame,
            variable=self.language_var,
            values=["Hrvatski", "Engleski", "Njemački"],
            command=lambda e: self.language_change(
                self.language_var.get(),
                self.all_categories,
                self.meal,
            ),
        )
        self.language_optionmenu.grid(column=0, row=0, padx=25, sticky="w")

        category = db_get_category_by_name(meal)
        all_recipes = db_get_recipes_by_category(category.id)

        row = 0
        for recipe in all_recipes:
            self.SingleRecipe(
                self,
                recipe_list_frame,
                recipe,
                recipe.name,
                row,
            )
            row += 1

    def create_info_frame(self, recipe, language):
        self.single_recipe_frame.grid(
            column=2, row=0, columnspan=3, rowspan=9, sticky="nsew"
        )
        self.recipe = recipe

        if recipe.photo == "" or not os.path.exists(recipe.photo):
            img = Image.open("Foto/no_image.png")
        else:
            img = Image.open(recipe.photo)
        image = ctk.CTkImage(dark_image=img, size=(300, 300))
        self.photo_label.configure(image=image)
        self.name_entry_var.set(recipe.name)
        self.staple_food_entry_var.set(recipe.staple_food)
        self.ingridients_textbox.delete(1.0, ctk.END)
        self.ingridients_textbox.insert(ctk.END, recipe.ingredients)
        self.preparation_textbox.delete(1.0, ctk.END)
        self.preparation_textbox.insert(ctk.END, recipe.preparation)
        self.protein_entry_var.set(recipe.proteins)
        self.carb_entry_var.set(recipe.carbs)
        self.fat_entry_var.set(recipe.fats)
        self.prep_time_entry_var.set(recipe.prep_time)
        self.recipe_category = db_get_category_by_id(recipe.category)
        if language == "Hrvatski" or language == "Croatian" or language == "Kroatisch":
            self.category_optionmenu_var.set(self.recipe_category.name_hr)
        elif language == "Engleski" or language == "English" or language == "Englisch":
            self.category_optionmenu_var.set(self.recipe_category.name_en)
        elif language == "Deutsch" or language == "German" or language == "Njemački":
            self.category_optionmenu_var.set(self.recipe_category.name_de)

        self.ingridients_textbox.configure(state="disabled")
        self.preparation_textbox.configure(state="disabled")

    def edit_recipe(self):
        if self.edit_switch_state_var.get() == "on":
            self.edit_switch_state_var.set("on")
            self.name_entry.configure(state="normal")
            self.staple_food_entry.configure(state="normal")
            self.ingridients_textbox.configure(state="normal")
            self.preparation_textbox.configure(state="normal")
            self.protein_entry.configure(state="normal")
            self.carb_entry.configure(state="normal")
            self.fat_entry.configure(state="normal")
            self.prep_time_entry.configure(state="normal")
            self.category_optionmenu.configure(state="normal")
        else:
            self.edit_switch_state_var.set("off")
            self.name_entry.configure(state="disabled")
            self.staple_food_entry.configure(state="disabled")
            self.ingridients_textbox.configure(state="disabled")
            self.preparation_textbox.configure(state="disabled")
            self.protein_entry.configure(state="disabled")
            self.carb_entry.configure(state="disabled")
            self.fat_entry.configure(state="disabled")
            self.prep_time_entry.configure(state="disabled")
            self.category_optionmenu.configure(state="disabled")

    class SingleRecipe:
        def __init__(self, main, parent_frame, recipe, name, row):
            self.main = main
            self.parent_frame = parent_frame
            self.recipe = recipe
            self.name = name
            self.row = row
            self.create_single_recipe()

        def create_single_recipe(self):
            recipe_label = ctk.CTkLabel(self.parent_frame, text=self.name)
            recipe_label.grid(column=0, row=self.row, padx=5, pady=5, sticky="w")

            recipe_label.bind(
                "<Button-1>",
                lambda e: self.main.create_info_frame(self.recipe, self.main.language),
            )
