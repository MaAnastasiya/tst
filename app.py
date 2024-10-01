from flask import Flask, request, Response

app = Flask(__name__)

# Маршрут /login/
@app.route('/login/', methods=['GET'])
def login():
response = Response("itmo411642")
response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
response.headers['Access-Control-Allow-Origin'] = '*'
return response

# Маршрут /sample/
@app.route('/sample/', methods=['GET'])
def sample():
def task(x):
return x * (x ** 2)

try:
# Получаем параметр 'x' из URL и пытаемся преобразовать его в число
x = request.args.get('x', type=int)
if x is None:
raise ValueError("Parameter 'x' is missing or not an integer.")

# Выполняем задачу
result = task(x)

# Возвращаем результат
response = Response(str(result))
response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
response.headers['Access-Control-Allow-Origin'] = '*'
return response

except ValueError as e:
# Если параметр 'x' некорректный или отсутствует, возвращаем ошибку
response = Response(str(e))
response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
response.headers['Access-Control-Allow-Origin'] = '*'
return response, 400

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)
