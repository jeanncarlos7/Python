from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
  return('API está no ar')

@app.route('/retorna_maior')
def retorna_maior():
  num1 = int(request.args.get('num1'))
  num2 = int(request.args.get('num2'))

  if (num1 > num2):
    maior = num1
  else:
    maior = num2

  resposta = {'Maior':maior}

  return jsonify(resposta)



app.run(host='0.0.0.0')