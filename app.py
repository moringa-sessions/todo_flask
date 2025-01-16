from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import User, Tags, Todo, db
app = Flask(__name__)

# migration initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
migrate = Migrate(app, db)
db.init_app(app)

# import all functions in views
from views import *


app.register_blueprint(user_bp)
app.register_blueprint(tags_bp)
app.register_blueprint(todo_bp)