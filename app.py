from flask import Flask, request, render_template_string
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Cyber Encryption App</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, sans-serif;
}

body{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#0f172a,#1e293b,#2563eb);
    overflow:hidden;
}

.container{
    width:90%;
    max-width:700px;
    padding:40px;
    border-radius:20px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
    box-shadow:0 8px 32px rgba(0,0,0,0.3);
    color:white;
    text-align:center;
    animation:fadeIn 1s ease;
}

h1{
    margin-bottom:10px;
    font-size:38px;
}

.subtitle{
    color:#cbd5e1;
    margin-bottom:30px;
}

textarea{
    width:100%;
    height:160px;
    padding:15px;
    border:none;
    border-radius:12px;
    outline:none;
    resize:none;
    font-size:16px;
    background:rgba(255,255,255,0.1);
    color:white;
}

textarea::placeholder{
    color:#cbd5e1;
}

.buttons{
    margin-top:20px;
    display:flex;
    justify-content:center;
    gap:20px;
    flex-wrap:wrap;
}

button{
    padding:14px 30px;
    border:none;
    border-radius:12px;
    font-size:16px;
    cursor:pointer;
    transition:0.3s;
    color:white;
    font-weight:bold;
}

.encrypt{
    background:#22c55e;
}

.decrypt{
    background:#ef4444;
}

button:hover{
    transform:translateY(-3px) scale(1.05);
    opacity:0.9;
}

.result-box{
    margin-top:30px;
    text-align:left;
    background:rgba(255,255,255,0.1);
    padding:20px;
    border-radius:12px;
    word-wrap:break-word;
}

.result-title{
    margin-bottom:10px;
    color:#93c5fd;
}

.result{
    color:#ffffff;
    line-height:1.5;
}

.footer{
    margin-top:20px;
    font-size:14px;
    color:#cbd5e1;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

</style>
</head>

<body>

<div class="container">

    <h1>🔐 Cyber Encryption App</h1>

    <p class="subtitle">
        Secure your messages using modern cryptographic encryption
    </p>

    <form method="POST">

        <textarea
        name="text"
        placeholder="Enter your text here..."
        ></textarea>

        <div class="buttons">

            <button class="encrypt"
            name="action"
            value="encrypt">
            Encrypt
            </button>

            <button class="decrypt"
            name="action"
            value="decrypt">
            Decrypt
            </button>

        </div>

    </form>

    <div class="result-box">

        <h3 class="result-title">Result</h3>

        <p class="result">
            {{ result }}
        </p>

    </div>

    <div class="footer">
        Built with Flask + Cryptography
    </div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    result = "Your encrypted/decrypted text will appear here."

    if request.method == "POST":

        text = request.form["text"]

        try:

            if request.form["action"] == "encrypt":

                encrypted = cipher.encrypt(text.encode())

                result = encrypted.decode()

            elif request.form["action"] == "decrypt":

                decrypted = cipher.decrypt(text.encode())

                result = decrypted.decode()

        except:

            result = "❌ Invalid encrypted text"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)