from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from todoapp.extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    todos_collections = mongo.db.flaskapp
    todos = todos_collections.find()
    return render_template('index.html', todos=todos)


@main.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.form.get('add-todo')
    todos_collections = mongo.db.flaskapp
    todos_collections.insert_one({'text': todo_item, 'complete': False})
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todos_collections = mongo.db.flaskapp
    todo_item = todos_collections.find_one({'_id':ObjectId(oid)})
    todo_item['complete'] = True
    todos_collections.save(todo_item)
    return redirect(url_for('main.index'))

@main.route('/delete_completed')
def delete_completed():
    todos_collections = mongo.db.flaskapp
    todos_collections.delete_many({'complete': True})
    return redirect(url_for('main.index'))

@main.route('/delete_all')
def delete_all():
    todos_collections = mongo.db.flaskapp
    todos_collections.delete_many({})
    return redirect(url_for('main.index'))
