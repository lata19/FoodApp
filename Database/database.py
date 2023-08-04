from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    Float,
    DateTime,
    ForeignKey,
    create_engine,
    update,
    or_,
)
from sqlalchemy.orm import declarative_base, Session, relationship
import datetime

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "Recipes"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    staple_food = Column(String)
    ingredients = Column(Text, nullable=False)
    preparation = Column(Text, nullable=False)
    proteins = Column(Float)
    carbs = Column(Float)
    fats = Column(Float)
    prep_time = Column(String)
    category = Column(Integer, ForeignKey("Categories.id"), nullable=False)
    category_name = relationship("Category", back_populates="recipe_category")
    photo = Column(String)


class Category(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True)
    name_hr = Column(String, nullable=False)
    name_en = Column(String, nullable=False)
    name_de = Column(String, nullable=False)
    recipe_category = relationship("Recipe", back_populates="category_name")


db_engine = create_engine("sqlite:///Database/RecipeApp.db")
Base.metadata.create_all(db_engine)


# FUNCTIONS
# Add new recipe
def db_add_new_recipe(
    name,
    staple_food,
    ingredients,
    preparation,
    proteins,
    carbs,
    fats,
    prep_time,
    category,
    photo,
):
    with Session(bind=db_engine) as session:
        recipe_exists = session.query(Recipe).filter(Recipe.name == name).one_or_none()
        if not recipe_exists:
            recipe = Recipe(
                name=name,
                staple_food=staple_food,
                ingredients=ingredients,
                preparation=preparation,
                proteins=proteins,
                carbs=carbs,
                fats=fats,
                prep_time=prep_time,
                category=category.id,
                photo=photo,
            )
            session.add(recipe)
            session.commit()
        return recipe_exists


def db_get_all_recipes():
    with Session(bind=db_engine) as session:
        return session.query(Recipe).all()


def db_get_recipes_by_category(category):
    with Session(bind=db_engine) as session:
        return session.query(Recipe).filter(Recipe.category == category).all()


def db_update_recipe(
    id,
    name,
    staple_food,
    ingredients,
    preparation,
    proteins,
    carbs,
    fats,
    prep_time,
    category,
    photo,
):
    with Session(bind=db_engine) as session:
        recipe = session.query(Recipe).filter(Recipe.id == id)
        recipe.update(
            {
                "name": name,
                "staple_food": staple_food,
                "ingredients": ingredients,
                "preparation": preparation,
                "proteins": proteins,
                "carbs": carbs,
                "fats": fats,
                "prep_time": prep_time,
                "category": category,
                "photo": photo,
            }
        )
        session.commit()


def db_delete_recipe(id):
    with Session(bind=db_engine) as session:
        session.query(Recipe).filter(Recipe.id == id).delete()
        session.commit()


# Categories
# Add category
def db_add_new_category(name_hr, name_en, name_de):
    with Session(bind=db_engine) as session:
        category = Category(name_hr=name_hr, name_en=name_en, name_de=name_de)
        session.add(category)
        session.commit()


# Get categories
def db_get_all_categories():
    with Session(bind=db_engine) as session:
        return session.query(Category).all()


def db_get_category_by_name(name):
    with Session(bind=db_engine) as session:
        category = (
            session.query(Category)
            .filter(
                or_(
                    Category.name_hr == name,
                    Category.name_en == name,
                    Category.name_de == name,
                )
            )
            .one_or_none()
        )
        return category


def db_get_category_by_id(id):
    with Session(bind=db_engine) as session:
        return session.query(Category).filter(Category.id == id).one()
