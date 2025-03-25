from flask import Flask, render_template, request

app = Flask(__name__)

def calcular(num1, num2, operation):
    """Realiza la operación matemática según el tipo especificado."""
    try:
        num1, num2 = float(num1), float(num2)
        operaciones = {
            "sum": num1 + num2,
            "subtract": num1 - num2,
            "multiply": num1 * num2,
            "divide": num1 / num2 if num2 != 0 else "Error: División por cero"
        }
        return operaciones.get(operation, "Error: Operación no válida")
    except ValueError:
        return "Error: Ingresa números válidos"

@app.route("/")
def home():
    return "Bienvenido a la calculadora"

@app.route("/calculadora", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        result = calcular(request.form.get("num1"), request.form.get("num2"), request.form.get("operation"))
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)