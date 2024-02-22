from flask import Flask, render_template, request, flash
import forms
from flask_wtf.csrf import CSRFProtect
from flask import g

app=Flask(__name__)
app.secret_key='esta es mi clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.before_request
def before_request():
    g.nombre='Mario'
    print("before 1")

@app.after_request
def after_request(response):
    print('after 3')
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    print("alumno: {}".format(g.nombre))
    alumno_clase = forms.UserForm(request.form)
    nom = ""
    apa = ""
    ama = ""
    edad = None
    if request.method=='POST' and alumno_clase.validate():
        nom=alumno_clase.nombre.data
        
        apa=alumno_clase.apaterno.data
        ama=alumno_clase.amaterno.data
        edad=alumno_clase.edad.data
        print('Nombre: {}'.format(nom))
        print('apaterno: {}'.format(apa))
        print('amaterno: {}'.format(ama))

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos.html", form=alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<h1>Saludos desde Hola prueba nueva<h1>"

@app.route("/Saludo")
def saludo():
    return "<h1>Saludos desde Saludo<h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "Hola: " + nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "Numero: {}".format(n1)

@app.route("/numero/<int:id>/<string:nom>")
def func(id, nom):
    return "ID: {} Nomrbe: {}".format(id, nom)

@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1,n2):
    return "La suma {} + {} = {}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default/<string:d>")
def func3(d="Dario"):
    return "El nombre de user es: " + d

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
    else:
        return '''
        <form action="/calcular" method="POST">
            <label id="n1">N1:</label>
            <input type="text" name="n1"><br>
            <label id="n2">N2:</label>
            <input type="text" name="n2"><br>
            <input type="submit">
        </form>
        '''

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado")
def result():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))

if __name__ == "__main__":
    app.run(debug=True)
