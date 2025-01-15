from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import User, Tags, Todo, db
app = Flask(__name__)

# migration initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
migrate = Migrate(app, db)
db.init_app(app)


# User
@app.route("/users")
def fetch_users():
    users = User.query.all()
    user_list = []

    for user in users:
        user_list.append({
            'id':user.id,
            'email':user.email,
            'is_approved': user.is_approved,
            'username':user.username
        })

    return jsonify(user_list)


@app.route("/users", methods=["POST"])
def add_users():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    check_username = User.query.filter_by(username=username).first()
    check_email = User.query.filter_by(email=email).first()

    print("Email ",check_email)
    print("Username",check_username)
    if check_username or check_email:
        return jsonify({"error":"Username/email exists"}),406

    else:
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success":"Added successfully"}), 201


# Update
@app.route("/users/<int:user_id>", methods=["PATCH"])
def update_users(user_id):
    user = User.query.get(user_id)

    if user:
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']

        check_username = User.query.filter_by(username=username and id!=user.id).first()
        check_email = User.query.filter_by(email=email and id!=user.id).first()

    
        if check_username or check_email:
            return jsonify({"error":"Username/email exists"}),406

        else:
            user.username=username
            user.email=email
            user.password=password
          
            db.session.commit()
            return jsonify({"success":"Updated successfully"}), 201

    else:
        return jsonify({"error":"User doesn't exist!"}),406

# Delete
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_users(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"success":"Deleted successfully"}), 200

    else:
        return jsonify({"error":"User your are trying to delete doesn't exist!"}),406



# ==================================TAGS======================================
@app.route("/tags", methods=["POST"])
def add_tag():
    data = request.get_json()
    name = data['name']


    check_name =Tags.query.filter_by(name=name).first()
   
    if check_name:
        return jsonify({"error":"Tag exists"}),406

    else:
        new_tag = Tags(name=name)
        db.session.add(new_tag)
        db.session.commit()
        return jsonify({"success":"Tag added successfully"}), 201
    
# Assignment
# add delete/update/fetch all tags/ fetch 1 tag





# ==================================TO--DO======================================
@app.route("/todo/add", methods=["POST"])
def add_todo():
    data = request.get_json()

    title = data['title']
    description = data['description']
    user_id = data['user_id']
    tag_id = data['tag_id']
    deadline = data['deadline']

    check_user_id =User.query.get(user_id)
    check_tag_id =User.query.get(tag_id)

   
    if not check_tag_id or not check_user_id:
        return jsonify({"error":"Tag/user doesn't exists"}),406

    else:
        new_todo = Todo(title=title, description=description,user_id=user_id, tag_id=tag_id, deadline=deadline)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"success":"Todo added successfully"}), 201
    
# Assignment
# add delete/update/fetch all todos/ fetch 1 todo