'''
API to handle transaction requests
'''
from flask import Blueprint, jsonify, request
import app.models.transaction as transaction_model
transaction = Blueprint('transaction', __name__)
@transaction.route('/', methods=['GET'])
def add_transaction():
    '''
    Put transaction in database
    '''
    status_code = 200
    success = True
    response = {'success': success}
    return jsonify(response), status_code