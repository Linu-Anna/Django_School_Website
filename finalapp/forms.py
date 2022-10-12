# from django import forms
#
# # from persons.models import Person, City
#
# from finalapp.models import Course,Person
#
#
# class PersonCreationForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['course'].queryset = Course.objects.none()
#
#         if 'department' in self.data:
#             try:
#                 deparment_id = int(self.data.get('department'))
#                 self.fields['course'].queryset = Course.objects.filter(deparment_id=deparment_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['course'].queryset = self.instance.department.course.order_by('name')