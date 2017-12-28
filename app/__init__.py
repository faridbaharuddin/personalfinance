from flask import Flask

def _initialize_blueprints (application):
    '''
    Register Flask blueprints
    '''
    from app.views.transaction import transaction
    from app.views.category import category
    application.register_blueprint(transaction, url_prefix='/api/v1/transaction')
    application.register_blueprint(category, url_prefix='/api/v1/category')
    
def create_app():
    application = Flask(__name__)
    _initialize_blueprints(application)
    return application