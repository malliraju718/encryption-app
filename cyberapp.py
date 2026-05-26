from flask import Flask, request, render_template_string
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate Secret Key
key = Fernet.generate_key()
cipher = Fernet(key)

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Cyber Shield Encryption</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
    background:#020617;
    color:white;
}

/* Animated Background */

body::before{
    content:'';
    position:absolute;
    width:200%;
    height:200%;
    background:
    radial-gradient(circle,#2563eb22 1px,transparent 1px);
    background-size:40px 40px;
    animation:moveBg 20s linear infinite;
}

@keyframes moveBg{
    from{
        transform:translate(0,0);
    }
    to{
        transform:translate(-200px,-200px);
    }
}

.container{
    position:relative;
    z-index:2;
    width:90%;
    max-width:750px;
    padding:40px;
    border-radius:25px;
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(14px);
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:
    0 0 20px #2563eb88,
    0 0 60px #2563eb44;
    animation:fadeIn 1s ease;
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

.title{
    text-align:center;
    font-size:42px;
    margin-bottom:10px;
    color:#60a5fa;
    text-shadow:0 0 15px #3b82f6;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:20px;
}

.clock{
    text-align:center;
    margin-bottom:20px;
    color:#93c5fd;
    font-size:18px;
}

textarea{
    width:100%;
    height:170px;
    padding:18px;
    border:none;
    border-radius:15px;
    background:#0f172a;
    color:white;
    font-size:16px;
    resize:none;
    outline:none;
    border:1px solid #334155;
}

textarea:focus{
    border:1px solid #3b82f6;
    box-shadow:0 0 10px #2563eb88;
}

.buttons{
    margin-top:25px;
    display:flex;
    justify-content:center;
    gap:15px;
    flex-wrap:wrap;
}

button{
    padding:14px 28px;
    border:none;
    border-radius:12px;
    font-size:15px;
    font-weight:bold;
    cursor:pointer;
    transition:0.3s;
    color:white;
}

.encrypt{
    background:#16a34a;
}

.decrypt{
    background:#dc2626;
}

.clear{
    background:#475569;
}

.copy{
    background:#2563eb;
}

button:hover{
    transform:translateY(-4px) scale(1.05);
    box-shadow:0 0 20px rgba(255,255,255,0.2);
}

.result-box{
    margin-top:30px;
    background:#0f172a;
    border-radius:15px;
    padding:20px;
    border:1px solid #334155;
}

.result-title{
    color:#60a5fa;
    margin-bottom:12px;
}

.result{
    line-height:1.6;
    word-wrap:break-word;
}

.footer{
    margin-top:25px;
    text-align:center;
    color:#94a3b8;
    font-size:14px;
}

.typing{
    overflow:hidden;
    white-space:nowrap;
    border-right:2px solid #60a5fa;
    width:0;
    animation:
    typing 3s steps(40,end) forwards,
    blink .7s infinite;
}

@keyframes typing{
    from{
        width:0;
    }
    to{
        width:100%;
    }
}

@keyframes blink{
    50%{
        border-color:transparent;
    }
}

</style>

</head>

<body>

<div class="container">

<h1 class="title">🔐 Cyber Shield</h1>

<p class="subtitle typing">
Advanced Secure Text Encryption System
</p>

<div class="clock" id="clock"></div>

<form method="POST">

<textarea
name="text"
placeholder="Enter your secret message here..."
></textarea>

<div class="buttons">

<button
class="encrypt"
name="action"
value="encrypt">
Encrypt
</button>

<button
class="decrypt"
name="action"
value="decrypt">
Decrypt
</button>

<button
type="button"
class="copy"
onclick="copyText()">
Copy Result
</button>

<button
type="button"
class="clear"
onclick="clearText()">
Clear
</button>

</div>

</form>

<div class="result-box">

<h3 class="result-title">Result</h3>

<p class="result" id="result">
{{ result }}
</p>

</div>

<div class="footer">
Built using Flask + Cryptography | Cyber Security Project
</div>

</div>

<script>

function copyText(){

    const text =
    document.getElementById("result").innerText;

    navigator.clipboard.writeText(text);

    alert("Result copied!");
}

function clearText(){

    document.querySelector("textarea").value = "";
}

function updateClock(){

    const now = new Date();

    document.getElementById("clock").innerHTML =
    now.toLocaleTimeString();
}

setInterval(updateClock,1000);

updateClock();

</script>

</body>
</html>

"""

@app.route("/", methods=["GET", "POST"])

def home():

    result = "Your encrypted/decrypted message appears here..."

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

    return render_template_string(
        HTML,
        result=result
    )

if __name__ == "__main__":

    app.run(debug=True)