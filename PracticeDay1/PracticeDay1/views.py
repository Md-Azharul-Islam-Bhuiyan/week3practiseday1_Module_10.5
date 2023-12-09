from django.shortcuts import render
import datetime

def home(request):
    d = { "author":'Rakib', 'age': 20, 'lst':['Rakib','is', 'a', 'Teacher'],
         'birthday': datetime.datetime.now(), 'val':'i\'m Jamal', 
         'value': 12,
         'num_messages': 4,
         'dtag':'<p>This <em>should be</em> fun!</p>', 
         'student':[
        {'roll': 1, 'name': 'Karim', 'age': 15},
        {'roll': 2, 'name': 'Rahim', 'age': 14},
        {'roll': 3, 'name': 'Sofiq', 'age': 16}
    ]}

    return render(request, 'home.html', context = d);