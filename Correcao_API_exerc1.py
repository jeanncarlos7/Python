from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
  return('API está no ar')

@app.route('/calcula_somatorio')
def calcula_somatorio():
  n = int(request.args.get('n'))

  soma = 0
  for i in range(1,n+1):
    soma+=i

  resposta = {'Soma':soma}

  return jsonify(resposta)

app.run(host='0.0.0.0')