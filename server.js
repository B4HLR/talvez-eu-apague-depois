const express = require("express");
const { exec } = require("child_process");
const cors = require("cors");

const app = express();
app.use(cors());

// ROTA /ping — quando o botão for clicado no site, chama essa rota
app.get("/ping/:ip", (req, res) => {
    const consultIP = req.params.ip;

    exec(`ping ${consultIP} -n 1`, (err, stdout, stderr) => {
        
        // 🔍 Analisa se o ping funcionou
        let sucesso = false;

        // Se o stdout contém "Resposta de" → ping ok (Windows)
        if (stdout.includes("Resposta de") || stdout.includes("bytes=")) {
            sucesso = true;
        }

        // Se houver erro ou timeout → falso
        if (err || stderr) {
            sucesso = false;
        }

        // Retorna para o cliente
        res.json({ sucesso });
    });
});

app.listen(3000, () => console.log("Servidor rodando na porta 3000"));
