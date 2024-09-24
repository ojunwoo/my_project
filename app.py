from flask import Flask, render_template, redirect, url_for, session, request
PORT=80
HOST="0.0.0.0"
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management

# Simulating a product catalog
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000},
    {'id': 2, 'name': 'Phone', 'price': 500},
    {'id': 3, 'name': 'Tablet', 'price': 300},
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Add selected product to cart
    if 'cart' not in session:
        session['cart'] = []

    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        session['cart'].append(product)

    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True,host=HOST,port=PORT)
