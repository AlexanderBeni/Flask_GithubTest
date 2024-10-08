#from flask import Flask
#app = Flask(__name__)
#@app.route("/") 
#def hello_world(): 
#    return "Hello, AlexanderBenitez!"
#if __name__ == "__pipmain__": app.run(debug=True)

#from flask import Flask, render_template, request

#app = Flask(__name__)

#@app.route('/')
#def home():
 #   return render_template('home.html', title='Home')

#@app.route('/about')
#def about():
#    return render_template('about.html', title='About')

#@app.route('/contact', methods=['GET', 'POST'])
#def contact():
   # if request.method == 'POST':
  #      name = request.form.get('name')
 #       email = request.form.get('email')
#        return f'Thank you {name}, we will contact you at {email}.'
#    return render_template('contact.html', title='Contact')

#if __name__ == '__main__':
#    app.run(debug=True)





from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/myflaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    db.create_all()
    return "Database and Product table created!"

@app.route('/add-product/<product_name>/<price>')
def add_product(product_name, price):
    new_product = Product(product_name=product_name, price=float(price))
    db.session.add(new_product)
    db.session.commit()
    return f"Added product: {product_name} with price {price}"

@app.route('/products')
def products():
    products = Product.query.all()
    output = ""
    for product in products:
        output += f"Product: {product.product_name}, Price: {product.price}<br>"
    return output

if __name__ == '__main__':
    app.run(debug=True)
