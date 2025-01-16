'''
Este programa realiza un seguimiento de tus rutinas de entrenamiento, series, repeticiones y pesos. 
Permite agregar ejercicios, registrar tu progreso y revisar entrenamientos anteriores. El programa 
se basa en la línea de comandos y comienza permitiendo al usuario elegir cualquiera de las opciones.
Al principio, el usuario puede querer agregar un tipo de ejercicio. Aquí el usuario agrega un ejercicio 
de flexiones y sentadillas. Una vez que el usuario ha agregado algunos tipos de ejercicios, puede registrar 
un ejercicio cada vez que lo realiza. Aquí el usuario ha registrado el ejercicio de flexiones, declarando 3 
series de 10 repeticiones cada una y 0 como peso adicional.
Finalmente, el usuario ve su progreso al elegir la opción 3. El programa muestra que el usuario ha realizado
una sesión y muestra los detalles sobre esa sesión. Puede utilizar programación funcional, procedimental o 
programación orientada a objetos. Para simplificar, no guardamos los datos del usuario en ningún archivo, 
sino que los guardamos dentro del programa temporalmente.
'''

class Exercise:
    def __init__(self, name):
        self.name = name
        self.logs = []

    def log_workout(self, sets, reps, weight):
        self.logs.append({
            'sets': sets,
            'reps': reps,
            'weight': weight
        })


class GymTracker:
    def __init__(self):
        self.exercises = {}

    def add_exercise(self, name):
        name = name.lower()
        if name not in self.exercises:
            self.exercises[name] = Exercise(name)
            print(f"Added exercise: {name.capitalize()}")
        else:
            print("Exercise already exists.")

    def log_workout(self, name, sets, reps, weight):
        name = name.lower()
        if name in self.exercises:
            self.exercises[name].log_workout(sets, reps, weight)
            print(f"Logged {sets} sets of {reps} reps at {weight:.1f} kg for {name.capitalize()}")
        else:
            print("Exercise not found.")

    def view_progress(self):
        if not self.exercises:
            print("No exercises logged yet.")
            return
        
        for exercise in self.exercises.values():
            print(f"\nProgress for {exercise.name.capitalize()}:")
            for log in exercise.logs:
                print(f"  - Sets: {log['sets']}, Reps: {log['reps']}, Weight: {log['weight']} kg")


def main():
    tracker = GymTracker()

    while True:
        print("\n🏋️ Gym Tracker Options:")
        print("1. Add Exercise")
        print("2. Log Workout")
        print("3. View Progress")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            exercise_name = input("Enter exercise name: ")
            tracker.add_exercise(exercise_name)

        elif choice == '2':
            exercise_name = input("Enter exercise name: ")
            sets = int(input("Enter number of sets: "))
            reps = int(input("Enter number of reps: "))
            weight = float(input("Enter weight in kg: "))
            tracker.log_workout(exercise_name, sets, reps, weight)

        elif choice == '3':
            tracker.view_progress()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()