from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

# Маршрут /login/
@app.route('/login/', methods=['GET'])
def login():
    response = Response("itmo411642")
    response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
    return response

# Маршрут /sample/
@app.route('/sample/', methods=['GET'])
def sample():
    def task(x):
        return x * (x ** 2)

    # Получаем параметр 'x' из URL
    x = request.args.get('x', type=int)

    if x is not None:
        # Выполняем задачу
        result = task(x)
    
        # Возвращаем результат
        response = Response(str(result))
        response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
