from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

from bson import ObjectId

#Inicializando flask
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://admin:Napsster@cluster0.tyj3s.mongodb.net/test'
mongo = PyMongo(app)


#Configuracion
CORS(app)

#Base de datos
db = mongo.db.Empresas


#Rutas
@app.route('/Empresas', methods=['POST'])
def createEmpresa():
    print(request.json)
    id = db.insert({
        'name': request.json['name'],
        'dir': request.json['dir'],
        'Nit': request.json['Nit'],
        'Phone': request.json['Phone']
    })
    return jsonify(str(ObjectId(id)))

@app.route('/Empresas', methods=['GET'])
def getEmpresas():
    Empresa = []
    for doc in db.find():
        Empresa.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'dir': doc['dir'],
            'Nit': doc['Nit'],
            'Phone': doc['Phone']
        })
    return jsonify(Empresa)

@app.route('/Empresas/<id>', methods=['GET'])
def getEmpresa(id):
    empresa = db.find_one({'_id': ObjectId(id)})
    return jsonify({
        '_id': str(ObjectId(empresa['_id'])),
        'name': empresa['name'],
        'dir': empresa['dir'],
        'Nit': empresa['Nit'],
        'Phone': empresa['Phone']
        })


@app.route('/Empresas/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Empresa Deleted'})


@app.route('/Empresas/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {"$set": {
        'name': request.json['name'],
        'dir': request.json['dir'],
        'Nit': request.json['Nit'],
        'Phone': request.json['Phone']
        }})
    return jsonify({'message': 'User Updated'})


if __name__ == "__main__":
    app.run(debug=True)
