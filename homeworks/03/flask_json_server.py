from flask import Flask, request, json

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    if request.method == 'POST':
        if version == '1':
            return json.dumps({'version' : 1, 'predict': request.get_json()['predict']})
        else:
            return json.dumps({'version' : 0, 'predict' :request.get_json()['old_predict']})

@app.route("/")
def hello():
    return """Для работы с сервером нужно отправить запрос с помощью requests.post(url, data, headers)
    URL имеет вид url/get_classifier_result/<version>, где <version> - '1' или '0'
    1 - для новой версии, 0 - для старой
    Треьуется отправить файл в формате json. Файл представляет из себя dict 
    {"predict" : i} - при <version> - '1', 
    {"old_predict": i} при <version> - '0'
    Ответом на запрос является dict:
    {"version" : value, "predict" : value}
    На ['version'] возвращается 1 или 0, на ['predict'] отправленное(ые значение)
    """

if __name__ == "__main__":
    app.run()