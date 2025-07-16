from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cart = {}

@app.route('/add', methods=['POST'])
def add_item():
    data = request.json
    name = data['name']
    price = data['price']
    quantity = data['quantity']

    if name in cart:
        cart[name]['quantity'] += quantity
    else:
        cart[name] = {'price' : price, 'quantity' : quantity}     
    return jsonify({'message': f'You have added {name} (${price}) x {quantity} to cart.'}), 200 

@app.route('/remove', methods=['DELETE'])
def remove_item():
    data = request.json
    name = data.get('name')
    if name in cart:
        del cart[name]
        return jsonify({'message': f'You have deleted {name} from cart'}), 200
    else:
        return jsonify({'message': f'{name} is not in cart!'}), 404

@app.route('/view', methods=['GET'])
def view_cart():
    if not cart:
        return jsonify({'message': f'Your cart is empty!'}), 200
    return jsonify(cart), 200


@app.route('/total', methods=['GET'])
def get_total():
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return jsonify({'total': f'${total:.2f}'}), 200

@app.route('/clear', methods=['DELETE'])
def clear_cart():
    cart.clear()
    return jsonify({'message': f'Cart is cleared!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
