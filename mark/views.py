from django.shortcuts import render
from .models import Mark_Class
from .form import create_input
import math


# Create your views here.

def mark_view(request):
    return render(request, 'mark/home.html')


def enter_page_view(request):
    initial_data = {
        ' Roll_No': "It's must be between 1001 to 1020",
        ' Name': 'Write your Name',

    }
    my_form = create_input()

    context = {
        'form': my_form
    }

    if request.method == "POST":
        my_form = create_input(request.POST or None)

        new_roll_no = request.POST.get("Roll no")
        print(new_roll_no)
        new_name = request.POST.get("Name")
        new_math = int(request.POST.get("Marks_maths"))
        new_physics = int(request.POST.get("Marks_physics"))
        new_chemistry = int(request.POST.get("Marks_chemistry"))
        total = new_math + new_physics + new_chemistry
        percentage = round((total / 300) * 100)

        context = {

            'data_list': [

                97,
                95,
                93,
                89,
                88,
                85,
                82,
                78,
                75,
                71,
                67,
                66,
                64,
                63,
                62,
                61,
                59,
                55,
                54,
                1],

            'form': my_form,
            'total': total,
            'percentage': percentage,
            'new_roll_no': new_roll_no,
            'new_name': new_name,
            ' new_math': new_math,
            ' new_physics': new_physics,
            ' new_chemistry': new_chemistry,

        }
        list = context['data_list']
        count = 0
        for i in range(len(list)):
            count += 1
            if percentage > list[i]:
                Rank = count
                if percentage < 33:
                    Rank = "Failed"
                context = {

                    'form': my_form,
                    'total': total,
                    'percentage': percentage,
                    'new_roll_no': new_roll_no,
                    'new_name': new_name,
                    ' new_math': new_math,
                    ' new_physics': new_physics,
                    ' new_chemistry': new_chemistry,
                    'Rank': Rank

                }
                break

    return render(request, 'mark/EnterMarks.html', context)


def view_leaderboard(request):
    Rank = 0
    context = {
        'data': {

            'Navneet': 97,
            'Dheeraj': 95,
            'Rahul': 93,
            'Piyush': 89,
            'Pranjal': 88,
            'Srishti': 85,
            'Devu': 82,
            'Shivam': 78,
            'Raj': 75,
            'Neeraj': 71,
            'Shahash': 67,
            'Mark': 66,
            'Rohan': 64,
            'Ravi': 63,
            'Shaikh': 62,
            'Shakshi': 61,
            'Shivani': 58,
            'Saloni': 55,
            'Preeti': 54,
            'Bhanu': 42, },
        'Rank': Rank

    }
    return render(request, 'mark/leaderboard.html', context)
