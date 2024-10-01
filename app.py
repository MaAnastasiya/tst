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

    # Получаем параметр 'x' из URL
    x = request.args.get('x', type=int)

    # Если x не передан, возвращаем 404 Not Found
    if x is None:
        return Response("Not Found", status=404)  # Возвращаем 404

    # Выполняем задачу
    result = task(x)

    # Возвращаем результат
    response = Response(str(result))
    response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
