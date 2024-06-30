from flask import Blueprint, request, jsonify
from app import db
from models import Customer

bp = Blueprint('customers', __name__)

@bp.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(
        name=data.get('name'),
        phone_number=data.get('phone_number'),
        email=data.get('email'),
        address=data.get('address')
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added successfully'}), 201

@bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    result = [
        {
            'id': customer.id,
            'name': customer.name,
            'phone_number': customer.phone_number,
            'email': customer.email,
            'address': customer.address
        }
        for customer in customers
    ]
    return jsonify(result)

@bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json()
    customer = Customer.query.get_or_404(id)
    customer.name = data.get('name')
    customer.phone_number = data.get('phone_number')
    customer.email = data.get('email')
    customer.address = data.get('address')
    db.session.commit()
    return jsonify({'message': 'Customer updated successfully'})

@bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'})
