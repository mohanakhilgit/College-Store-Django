from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.admin.widgets import AdminDateWidget

from .models import Order, Course


class DatePickerInput(forms.DateInput):
    input_type = 'date'

class OrderForm(forms.ModelForm):
    MATERIALS = (
    ('note_book', 'Note Book'),('pencil', 'Pencil'),('pen', 'Pen'),
    ('scale', 'Scale'),
    ('box', 'Box'),
    ('exam_paper', 'Exam Paper')
    )
    dob = forms.DateField(widget=DatePickerInput)
    material = forms.MultipleChoiceField(choices=MATERIALS, widget=CheckboxSelectMultiple)

    class Meta:
        model = Order
        fields = "name", "dob", "age", "gender", "phone", "mail", "address", "department", "course", "purpose", "material"
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
