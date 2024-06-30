from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)

from routes import auth, books, customers, loans, images

app.register_blueprint(auth.bp)
app.register_blueprint(books.bp)
app.register_blueprint(customers.bp)
app.register_blueprint(loans.bp)
app.register_blueprint(images.bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
