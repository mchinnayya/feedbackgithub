from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from dynamicform.models import DynamicFormMaster,FeedbackLayout
from dynamicform.layout.forms import FeedbackLayoutForm

class LayoutCreate(CreateView):
    model = FeedbackLayout
    fields = '__all__'

    form_class = FeedbackLayoutForm
    template_name = 'layout/layout_create.html'

    def get(self, request, formmasterid):
        layoutform = FeedbackLayoutForm()

        context = {
            'layoutform': layoutform,
            'formmasterid': formmasterid
        }
        return render(self.request, self.template_name, context)

    def post(self, request, formmasterid):
        layout = FeedbackLayout()
        layout.form_master = DynamicFormMaster.objects.filter(id__iexact=formmasterid).first()
        layout.description_left_1 = self.request.POST.get('description_left_1')
        layout.description_left_2 = self.request.POST.get('description_left_2')
        layout.description_left_3 = self.request.POST.get('description_left_3')
        layout.description_right_1 = self.request.POST.get('description_right_1')
        layout.description_right_2 = self.request.POST.get('description_right_2')
        layout.description_right_3 = self.request.POST.get('description_right_3')
        layout.save()

        return redirect('dynamicform:dynamicform_list')


# def formfield_update(request, pk):
#     formfield = DynamicFormField.objects.get(pk=pk)
#     fieldform = DynamicFormFieldForm(request.POST or None, instance=formfield)
#     if request.method == 'POST':
#         if fieldform.is_valid():
#             formfield.field_title = request.POST.get('field_title')
#             formfield.field_type = request.POST.get('field_type')
#             formfield.field_hihhen = request.POST.get('field_hihhen')
#             formfield.field_description = request.POST.get('field_description')
#             formfield.save()
#             return redirect('dynamicform:dynamicform_view')
#     else:
#         fieldform = DynamicFormFieldForm(instance=formfield)
#     return render(request, 'formfield/formfield_update.html', {'fieldform': fieldform, 'pk': pk})
