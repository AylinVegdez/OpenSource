
#Aplicación básica de Flask
from flask import Flask, render_template
app = Flask(__name__)
#agregar configuracion desde archivo configuracion.txt
app.config.from_object('configuracion.DevConfig')

@app.route('/') # Creando una rutas con decoradores

def index(): # Creando una vista
    #return '<h1 style="color:blue;">Hola desde aqui ...</h1>'
    cursos=['java','python','html','css']
    data={
        'titulo':'Pagina principal',
        'saludo':'Pasale',
        'cursos':cursos,
        'numero_cursos':len(cursos)
    }
    return render_template('index.html',data=data,nombre='Martha')

@app.route('/login')
def login():
    data={
        'titulo':'Login de usuario',
        'email':'aylin.vega930@gmail.com',
        'password':'**********'
    }
    return render_template('login.html', data=data)

if __name__ == '__main__':
    app.run()#debug=True, port=5000)