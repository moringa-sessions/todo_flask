from flask import jsonify, request, Blueprint
from models import db, User, Tags, Todo

todo_bp= Blueprint("todo_bp", __name__)

# ==================================TO--DO======================================
@todo_bp.route("/todo/add", methods=["POST"])
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
# READ - Get All Todos)
@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    todo_list = [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "user_id": todo.user_id,
            "tag_id": todo.tag_id,
            "deadline": todo.deadline,
            "user": {"id":todo.user.id, "username": todo.user.username, "email": todo.user.email},
            "tag": {"id": todo.tag.id, "name":todo.tag.name}
        } for todo in todos
    ]    

    return jsonify(todo_list), 200
    

# READ - Get Todo by ID
@todo_bp.route("/todo/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        todo_details = {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "user_id": todo.user_id,
            "tag_id": todo.tag_id,
            "deadline": todo.deadline.strftime('%Y-%m-%d')
        }
        return jsonify(todo_details), 200
    
    else:
        return jsonify({"error": "Todo not found"}), 406

# UPDATE
@todo_bp.route("/todo/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()
    todo = Todo.query.get(todo_id)

    if todo:

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
            # Apply updates
            todo.title = title
            todo.description = description
            todo.user_id = user_id
            todo.tag_id = tag_id
            todo.deadline = deadline_date

            db.session.commit()
            return jsonify({"success": "Todo updated successfully"}), 200

    else:
        return jsonify({"error": "Todo not found"}), 406


# DELETE
@todo_bp.route("/todo/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 406


    db.session.delete(todo)
    db.session.commit()
    return jsonify({"success": "Todo deleted successfully"}), 200

