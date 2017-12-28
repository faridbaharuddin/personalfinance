'''
API to handle transaction requests
'''
from flask import Blueprint, jsonify, request
import app.models.category as category_model
category = Blueprint('category', __name__)

@category.route('/', methods=['GET'])
def get_category():
    '''
    Get category from database
    '''
    status_code = 200
    success = True
    response = {'success': success}
    return jsonify(response), status_code

@category.route('/somecategory', methods=['GET'])
def get_subcategory():
    '''
    Get subcategory for a specific category from database
    '''
    status_code = 200
    success = True
    response = {'success': success, 'category': 'somecategory'}
    return jsonify(response), status_code