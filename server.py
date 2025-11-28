from flask import Flask, jsonify
from flask_cors import CORS
import os
import subprocess
import re

app = Flask(__name__)
CORS(app)

@app.route("/ping/<ip>", methods=["GET", "POST"])
def ping_host(ip):

    try:
        # -n (Windows) / -c (Linux)
        param = "-n" if os.name == "nt" else "-c"

        resultado = subprocess.run(
            ["ping", param, "1", ip],
            capture_output=True,
            text=True,
            timeout=5
        )

        saida = resultado.stdout.lower()

        if resultado.returncode != 0:
            return jsonify({"sucesso": False})

        padroes_falha = [
            "100%",
            "inacess",  
            "host unreachable",
            "tempo esgotado",
            "time out",
            "novamente"
        ]

        for p in padroes_falha:
            if p in saida:
                return jsonify({"sucesso": False})

        return jsonify({"sucesso": True})

    except Exception as e:
        return jsonify({"erro": str(e), "sucesso": False}), 500


if __name__ == "__main__":
    app.run(debug=True)
