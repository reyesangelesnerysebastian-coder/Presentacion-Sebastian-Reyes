from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# CONFIGURACION DEL CORREO
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'reyes.angeles.nerysebastian@gmail.com'
app.config['MAIL_PASSWORD'] = 'khqazodxhsdbyrms'

mail = Mail(app)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']

    msg = Message(
        subject=f"Nuevo mensaje de {nombre}",
        sender=app.config['MAIL_USERNAME'],
        recipients=['reyes.angeles.nerysebastian@gmail.com']
    )

    msg.body = f"""
Nombre: {nombre}
Correo: {email}

Mensaje:
{mensaje}
"""

    mail.send(msg)

    return "Mensaje enviado correctamente"

if __name__ == "__main__":
    app.run(debug=True)