from flask import Flask, request, jsonify

app = Flask(__name__)

datas = [
    {
        'id': 1,
        'nama': 'Toko Bunga',
        'items': [
            {
                'name': 'Bunga Kecombrang',
                'price': 5000
            }
        ]
    },
    {
        'id': 2,
        'nama': 'Toko Buku',
        'items': [
            {
                'name': 'Buku Tangkuban Perahu',
                'price': 10000
            }
        ]
    }
]

@app.route('/store')  # http://127.0.0.1:5000/store
def getAll():
    return jsonify(datas)

@app.route('/store/<int:id>')  # http://127.0.0.1:5000/store/1
def getbyId(id):
    for data in datas:
        if data['id'] == id:
            return jsonify(data)
    return jsonify({'message': 'Data not found'})

@app.route('/store', methods=["POST"])  # http://127.0.0.1:5000/store
def addStore():
    req_data = request.get_json()
    new_data = {
        'id': req_data['id'],
        'nama': req_data['nama'],
        'items': req_data['items']
    }
    datas.append(new_data)
    return jsonify(new_data)

@app.route('/store/<int:id>', methods =["DELETE"]) # http://127.0.0.1:5000/store/1
def deleteStore(id):
    for index, data in enumerate(datas):
        if data["id"] == id:
            deleted_data = datas.pop(index)
            return jsonify({"message" : "Data berhasil dihapus", "data" : deleted_data})
    return jsonify({"message" : "Data tidak ditemukan"}), 404

@app.route('/store/<int:id>', methods=["PUT"])  # http://127.0.0.1:5000/store/1
def updateStore(id):
    req_data = request.get_json()
    for data in datas:
        if data['id'] == id:
            data['nama'] = req_data.get('nama', data['nama'])  # Update nama jika ada, kalau tidak pakai lama
            data['items'] = req_data.get('items', data['items'])  # Update items jika ada, kalau tidak pakai lama
            return jsonify({"message": "Data berhasil diupdate", "data": data})
    return jsonify({"message": "Data tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True)