from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'sssdhgclshfsh;shd;jshjhsjhjhsjldchljk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website1.db'




# these lines below are supposed to be the /about page to be shown to the unknown user (either registered or not)

names = ["Andrea", "Elena", "Edoardo", "Francesco"]
posts = [
    {
        'author': 'Mohammad',
        'title': 'Flask session 1',
        'content': 'please continue....',
        'date_posted': '19 Oct. 2020'
    },
    {
        'author': 'Andrea',
        'title': 'Flask session 2',
        'content': 'please continue....',
        'date_posted': '19 Oct. 2020'
    },
    {
        'author': 'Edoardo',
        'title': 'Flask session 3',
        'content': 'please continue....',
        'date_posted': '19 Oct. 2020'
    },
    {
        'author': 'Sina',
        'title': 'Flask session 4',
        'content': 'please continue....',
        'date_posted': '19 Oct. 2020'
    }
]


@app.route('/bloglayout')
@app.route('/index')
@app.route('/')
def posthtml_layout():
    return render_template('blog-2.html', posts=posts, name_website='Blog IS 2020 Platform')


from model import *
from form import FormRegistration



    # errore su preparation
#   pizza1= Recipe(name='pizza1', preparation=)
@app.before_first_request
def setup():
    db.create_all()
    pizza1 = Recipe(name='pizza1')
    """
    pizza1.preparation = 'To have prepare a good neapolitan pizza1 you will need 425 g of 00 flour, 250 g of water , 1/4 g of fresh yeast and 13 g of salt. For the topping 200 g of tomatoe sauce, 10 g of EVO oil and 50 g of vegan mozzarella Prepare dough, use the wood oven in your kitchen and it is ready. Bon appeitt!'
    pizza1.recipes.append(Food(name='00 flour', vegan=True, lactose_free=True, gluten_free=False))
    pizza1.recipes.append(Food(name='water', vegan=True, lactose_free=True, gluten_free=True))
    pizza1.recipes.append(Food(name='salt', vegan=True, lactose_free=True, gluten_free=True))
    pizza1.recipes.append(Food(name='fresh yeast', vegan=True, lactose_free=True, gluten_free=True))
    pizza1.recipes.append(Food(name='tomato sauce', vegan=True, lactose_free=True, gluten_free=True))
    pizza1.recipes.append(Food(name='vegan mozzarella', vegan=True, lactose_free=True, gluten_free=True))"""
    db.session.add(pizza1)
    db.session.commit()

#l'errore e in questa parte sopra. una volta che lo mando non va piu

if __name__ == '__main__':
    app.run()
