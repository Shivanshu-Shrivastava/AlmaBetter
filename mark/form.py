from django import forms


class create_input(forms.Form):
    Name = forms.CharField(initial='Write your Name', label='Name', max_length=100)
    Roll_No = forms.IntegerField(max_value=1030, min_value=1001, label='Roll no')

    Marks_maths = forms.IntegerField(max_value=100, min_value=0, label='Marks In Math')
    Marks_physics = forms.IntegerField(max_value=100, min_value=0, label='Marks In physics')
    Marks_chemistry = forms.IntegerField(max_value=100, min_value=0, label='Marks In chemistry')
