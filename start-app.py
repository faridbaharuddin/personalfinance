#!/usr/bin/env python
from app import create_app
# Gunicorn entry point.
application = create_app()
if __name__ == '__main__':
    # Entry point when run via Python interpreter.
    print("== Running in debug mode ==")
    application.run(host='0.0.0.0', port=5000, debug=True)