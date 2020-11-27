from app import db

from sqlalchemy import Table, Text

# association table
recipe_foods = db.Table('recipe_foods',
                        db.Column('Recipe_name', db.String(50), db.ForeignKey('Recipe.name')),
                        db.Column('Food_name', db.String(50), db.ForeignKey('Food.name')))

class User(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    lactose_free = db.Column(db.Boolean, nullable=False)
    gluten_free = db.Column(db.Boolean, nullable=False)

#recipe_foods = db.ForeignKey('recipe_foods')
#qui ho fatto la class refernce come una stringa (??)


class Recipe(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    #ingredient = db.relationship('Food', secondary=recipe_foods, backref=db.backref('recipes'))
    preparation = db.Column(db.String(20000), nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    lactose_free = db.Column(db.Boolean, nullable=False)
    gluten_free = db.Column(db.Boolean, nullable=False)
    #va bene ripetere tre volte tre attributi? sono ridondanti? come evitarlo?

class Food(db.Model):
    #__tablename__ = 'foods'
    name = db.Column(db.String(50), primary_key=True)
    recipe = db.relationship('Recipe',secondary=recipe_foods, backref=db.backref('recipes', lazy='dynamic'))
    carbs = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    fiber = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)
    gCO2 = db.Column(db.Integer, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    lactose_free = db.Column(db.Boolean, nullable=False)
    gluten_free = db.Column(db.Boolean, nullable=False)





#we create the association table. it is not a class, because we will not use it.
#even though we have this association table, ther's nothing to update this association table
#i have to create a conncetion between  these three table
# i am giong to do this by putting connection in the food model.
#i add a third field, attribute to the food model. it will create the conncetion betwen foods and asso. table
#it is connected to the recipe and to the recipe_foods thorugh secondary
#the field added in food is like it was added to the asso. table.
#lazy: is useful to manage heavy data
