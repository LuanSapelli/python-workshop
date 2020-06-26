from app import app
from flask_cors import CORS
from routes import person, debt, credit_card, earn, spent

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(debug=True)

