from flask import Flask, jsonify
from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
CORS(app)


@app.route("/ping/<IpConsulta>", methods=["GET","POST"])
def processar_ping(IpConsulta):

    IP = IpConsulta

    param = "-n" if os.name == "nt" else "-c"

    resultado = subprocess.run(
    ["ping", param, "1", IP],
    capture_output=True,
    text=True
)
    primerioParammetro = resultado.stdout.find(f"100%") != -1
    segundpParammetro = resultado.stdout.find("inacess") != -1
    terceiroParammetro = resultado.stdout.find("novamente") != -1

    analise = primerioParammetro + segundpParammetro + terceiroParammetro == 0

    if analise:
        return jsonify({
            "sucesso":True
        })
    else:
         return jsonify({
            "sucesso":False
        })

while True:
    app.run(debug=True)