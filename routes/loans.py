from flask import Blueprint, request, jsonify
from app import db
from models import Loan, Book, Customer

bp = Blueprint('loans', __name__)

@bp.route('/loans', methods=['POST'])
def add_loan():
    data = request.get_json()
    new_loan = Loan(
        book_id=data.get('book_id'),
        customer_id=data.get('customer_id'),
        loan_date=data.get('loan_date'),
        return_date=data.get('return_date'),
        due_date=data.get('due_date')
    )
    db.session.add(new_loan)
    db.session.commit()
    return jsonify({'message': 'Loan added successfully'}), 201

@bp.route('/loans', methods=['GET'])
def get_loans():
    loans = Loan.query.all()
    result = [
        {
            'id': loan.id,
            'book_id': loan.book_id,
            'customer_id': loan.customer_id,
            'loan_date': loan.loan_date,
            'return_date': loan.return_date,
            'due_date': loan.due_date,
            'returned': loan.returned
        }
        for loan in loans
    ]
    return jsonify(result)

@bp.route('/loans/<int:id>', methods=['PUT'])
def update_loan(id):
    data = request.get_json()
    loan = Loan.query.get_or_404(id)
    loan.book_id = data.get('book_id')
    loan.customer_id = data.get('customer_id')
    loan.loan_date = data.get('loan_date')
    loan.return_date = data.get('return_date')
    loan.due_date = data.get('due_date')
    loan.returned = data.get('returned')
    db.session.commit()
    return jsonify({'message': 'Loan updated successfully'})

@bp.route('/loans/<int:id>', methods=['DELETE'])
def delete_loan(id):
    loan = Loan.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return jsonify({'message': 'Loan deleted successfully'})
