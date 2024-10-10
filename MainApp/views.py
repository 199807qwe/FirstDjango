from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# Create your views here.


def home(request):
    context = {

        "name": "Иванов  Петр  Семенович",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html" , context)


def items_page(request):
    context = {


    }

author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru",
}

items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]

def about(request):
    text=f"""
        Имя: {author["Имя"]}<br>
        Отчество:{author["Отчество"]}<br>
        Фамилия: {author["Фамилия"]}<br>
        телефон: {author["телефон"]}<br>
        email: {author["email"]}<br>
    """
    return HttpResponse(text)  # или return "<br>".join([f"{key}: {value}" for key, value in user_info.items()])

def get_item(request , item_id: int):
    """Trigger item_id back element list """
    for item  in items:
        if item  ['id'] == item_id:
            result = f"""
            <h2> Name: {item['name']}</h2>
            <p> Cost:{item['quantity']}</p>
            <p> <a href ='/items'> back to items list</a>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'Item with id={item_id} not found')

# def get_items(request):
#     result =  "<h1> List product</h1><ol>"
#     for item in items:
#         result += f"""<li><a href='/item/{item["id"]}'> {item["name"]} </a> </li>"""
#     result += "</ol>"
#     return HttpResponse(result)

def get_items(request):
    context = {

        "items":items
    }
    return render(request,"items_list.html", context)
    


