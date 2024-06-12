import sys
import os

# Add the top-level project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from financial_dashboard.backend.flask_app import app

if __name__ == '__main__':
    app.run(debug=True)
