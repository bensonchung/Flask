# -*- coding: UTF-8 -*-

stores = [
    {
        "name": "CWB",
        "items": [{'name':'my item 1', 'price': 30 }],
    },
    {
        "name": "IISI",
        "items": [{'name':'my item 2', 'price': 15 }],
    },
]

from flask import Flask, jsonify, request
app = Flask(__name__)

#get /store
@app.route('/store')
def get_stores():
    return jsonify(stores)

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

#get /store/<name>/item data: {name :}/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

#post /store/<name> data: {name :}/item
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price'],
            }
            store['items'].append(new_item)
            return jsonify(new_item)


if __name__ == "__main__":
    app.run(debug=True)
