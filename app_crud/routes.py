from flask import Blueprint, jsonify, request, abort
from models import db, User

bp = Blueprint('user', __name__)

@bp.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        username=data['username'],
        first_name=data['firstName'],
        last_name=data['lastName'],
        email=data['email'],
        phone=data['phone']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "username": user.username,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "email": user.email,
        "phone": user.phone
    })

@bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.first_name = data['firstName']
    user.last_name = data['lastName']
    user.email = data['email']
    user.phone = data['phone']
    db.session.commit()
    return jsonify({"message": "User updated successfully"})

@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 204
