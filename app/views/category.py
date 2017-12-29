'''
API to handle category requests
'''
from flask import Blueprint, jsonify, request
import app.models.category as category_model
import mysql.connector as mysql
import app.config.mysql as mysql_ext_cfg

category = Blueprint('category', __name__)
mysql_config = mysql_ext_cfg.mysql_config


@category.route('/', methods=['GET'])
def get_category():
    cnx = mysql.connect(**mysql_config)
    cursor = cnx.cursor()
    query = ("SELECT id, title, description FROM category WHERE parentid IS NULL ORDER BY title")
    cursor.execute(query)
    categories = [ { 'categoryid': i[0], 'title': i[1], 'description': i[2]} for i in cursor.fetchall()]
    cursor.close()
    cnx.close()
    status_code = 200
    response = {'categories': categories}
    return jsonify(response), status_code

@category.route('/<category_id>', methods=['GET'])
def get_subcategory(category_id):
    cnx = mysql.connect(**mysql_config)
    cursor = cnx.cursor()
    query = ("SELECT id, title, description FROM category WHERE parentid = %d ORDER BY title" % int(category_id))
    cursor.execute(query)
    categories = [ { 'categoryid': i[0], 'title': i[1], 'description': i[2]} for i in cursor.fetchall()]
    cursor.close()
    cnx.close()
    status_code = 200
    response = {'categories': categories}
    return jsonify(response), status_code

@category.route('/updates/<target_date>', methods=['GET'])
def get_updates(target_date):
    cnx = mysql.connect(**mysql_config)
    cursor = cnx.cursor()
    query = ("SELECT id, title, description FROM category WHERE lastupdatedt > %s" % target_date)
    cursor.execute(query)
    categories = [ { 'categoryid': i[0], 'title': i[1], 'description': i[2]} for i in cursor.fetchall()]
    cursor.close()
    cnx.close()
    status_code = 200
    response = {'categories': categories}
    return jsonify(response), status_code

