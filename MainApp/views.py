from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    text  =  """
    <h1>we  are learnin django</h1>
    <strong>Author<strong>:<i>Ivanov</i>
    """
    return HttpResponse(text)


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about')
def about():
    user_info = {
        "Имя": "Иван",
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
        "телефон": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }
    return jsonify(user_info)  # или return "<br>".join([f"{key}: {value}" for key, value in user_info.items()])

if __name__ == '__main__':
    app.run(debug=True)
