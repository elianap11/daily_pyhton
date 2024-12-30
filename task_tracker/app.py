'''
En este proyecto, crearemos una aplicación web de seguimiento de tareas utilizando Flask y 
MaterializeCSS. Los usuarios podrán agregar tareas a una lista, marcarlas como completadas y eliminarlas. 
Flask se encargará del backend, mientras que MaterializeCSS se utilizará para diseñar el frontend y 
proporcionar un diseño responsivo.

Resultado esperado
La página de inicio mostrará campos de entrada donde los usuarios pueden agregar una descripción de la tarea. 
Cada tarea se mostrará en una lista, con opciones para marcar la tarea como completada o eliminarla. El diseño 
será simple pero atractivo, utilizando MaterializeCSS para una interfaz de usuario limpia y moderna.
'''

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para almacenar tareas
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form.get('task')
    if task_description:
        tasks.append({'description': task_description, 'completed': False})
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)