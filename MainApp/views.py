from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# Create your views here.



items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    context = {
        "name": "Иванов Петр Семенович",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    author = {
    "name": "Иван",
    "middle_name": "Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru",
    }   
    return render(request, "about.html", {"author": author})






def get_item(request , item_id: int):
    """Trigger item_id back element list """
    for item  in items:
        if item  ['id'] == item_id:
            context={"item":item}
            
            return 
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
    


