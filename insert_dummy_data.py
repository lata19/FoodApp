from Database.database import *

# db_add_new_category("Doručak", "Breakfast", "Frühstück")
# db_add_new_category("Ručak", "Lunch", "Mittagessen")
# db_add_new_category("Večera", "Dinner", "Abendessen")
# db_add_new_category("Desert", "Desert", "Nachtisch")

dorucak = db_get_category_by_name("Doručak")
rucak = db_get_category_by_name("Ručak")
mittagessen = db_get_category_by_name("Mittagessen")
lunch = db_get_category_by_name("Lunch")

# db_add_new_recipe(
#     "Piletina s tjesteninom",
#     "Piletina",
#     "Piletina 300g, Tjestenina 180g, Vrhnje a kuhanje 300ml, Začini po želji",
#     "Piletinu ispeći na tavi i kada je gotovo dodati vrhnje za kuhanje. Skuhati tjesteninu. Kada je tjestenina godotva preliti umakom i piletinom.",
#     "60",
#     "150",
#     "15",
#     "45 minuta",
#     rucak,
#     "",
# )
# db_add_new_recipe(
#     "Jaja s tostom",
#     "Jaja",
#     "4 jaja",
#     "Jaja ispeći i poslužiti s tostom. Sol i papar po izboru.",
#     "50",
#     "36",
#     "20",
#     "10 minuta",
#     dorucak,
#     "",
# )
# db_add_new_recipe(
#     "Griz na mlijeku s kakaom",
#     "Griz",
#     "Griz 300g, kakao instant prah 50g",
#     "Skuhati griz i posipati s kakao napitkom",
#     "25",
#     "60",
#     "5",
#     "6 minuta",
#     dorucak,
#     "",
# )

# db_add_new_recipe(
#     "Kobasice s kiselim kupusom",
#     "Kobasice",
#     "Kobasice 250g, kiseli kupus 120g",
#     "Skuhati kobasice. Kiseli kupus prziti na tavi i kada se kobasice skuhaju dodati ih u tavu. Prziti ih jos par minuta i zajedno posluziti.",
#     "60",
#     "40",
#     "50",
#     "25 minuta",
#     mittagessen,
#     "",
# )

# db_add_new_recipe(
#     "Grah",
#     "Grah",
#     "Grah 150g",
#     "Skuhati grah.",
#     "50",
#     "32",
#     "17",
#     "60 minuta",
#     lunch,
#     "",
# )

# db_delete_recipe(6)

# db_add_new_recipe(
#     "Salata",
#     "Rajčica",
#     "Rajčica 100g, Krastavci 150g, Sir 30g",
#     "Pomiješati salatu i začiniti.",
#     "15",
#     "10",
#     "18",
#     "5 minuta",
#     lunch,
#     "Foto/Recipe_Foto/Salata.png",
# )

# db_add_new_category("Snack", "Snack", "Snack")
