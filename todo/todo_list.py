'''
Crear una aplicación web de lista de tareas pendientes utilizando Flask. Los usuarios pueden 
agregar nuevas tareas y completar y eliminar tareas existentes. Los datos se guardan en un 
archivo database.db. El programa crea el archivo de base de datos la primera vez que se ejecuta
la aplicación web y luego los datos se agregan a la base de datos existente. Usamos sqlite para
manejar la base de datos. En el estilado de la aplicación puede usar CSS puro o Bootstrap.
'''

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para obtener una conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla si no existe
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inicializar la base de datos
init_db()

# Función para agregar una tarea                
def add_task(task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (task, done) VALUES (?, ?)
    ''', (task, False))
    conn.commit()
    conn.close()

# Función para marcar una tarea como completada
def complete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks SET done = 1 WHERE id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()

# Función para eliminar una tarea                
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tasks WHERE id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()

# Función para obtener todas las tareas
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM tasks''')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Rutas de la aplicación web
@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    add_task(task)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)