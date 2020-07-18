from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, DeleteView
from dynamicform.models import DynamicFormField, DynamicFormMaster, DynamicFormFieldDropdown
from dynamicform.formfield.forms import DynamicFormFieldForm, DynamicFormFieldDropdownForm
from common.views import getoriginalName


class FormFieldList(TemplateView):
    model = DynamicFormField
    context_object_name = 'formfield_list'
    template_name = 'dynamicform/dynamicform_details.html'

    def get_context_data(self, **kwargs):
        context = super(FormFieldList, self).get_context_data(**kwargs)
        context['formfields'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class FormFieldDetails(DetailView):
    model = DynamicFormField
    template_name = 'formfield/formfield_details.html'
    fields = ('field_title', 'field_type', 'field_hihhen', 'field_description')

    def get(self, request, pk):
        formfield = DynamicFormField.objects.get(id=pk)
        context = {

            'formfield': formfield

        }
        return render(request, self.template_name, context)


def formfield_update(request, pk):
    formfield = DynamicFormField.objects.get(pk=pk)
    fieldform = DynamicFormFieldForm(request.POST or None, instance=formfield)
    if request.method == 'POST':
        if fieldform.is_valid():
            formfield.field_title = request.POST.get('field_title')
            formfield.field_type = request.POST.get('field_type')
            formfield.field_hihhen = request.POST.get('field_hihhen')
            formfield.field_description = request.POST.get('field_description')
            formfield.save()
            return redirect('dynamicform:dynamicform_view')
    else:
        fieldform = DynamicFormFieldForm(instance=formfield)
    return render(request, 'formfield/formfield_update.html', {'fieldform': fieldform, 'pk': pk})


def formfield_delete(request):
    fieldform = DynamicFormField.objects.get(id=request.POST.get('formfieldid'))
    fieldform.delete()
    return HttpResponse(True)


# dynamic form field with drop down

class FormFieldCreate(CreateView):
    model = DynamicFormField, DynamicFormFieldDropdown
    fields = '__all__'
    form_class = DynamicFormFieldForm, DynamicFormFieldDropdownForm
    template_name = 'formfield/formfield_create.html'

    def get(self, request, formmasterid):
        dropdownform = DynamicFormFieldDropdownForm()
        fieldform = DynamicFormFieldForm()

        context = {
            'fieldform': fieldform,
            'dropdownform': dropdownform,
            'formmasterid': formmasterid,
        }
        return render(self.request, self.template_name, context)

    def post(self, request, formmasterid):
        formmasterid = self.request.POST.get('fielfMasterID')
        fieldType = self.request.POST.get('field_type')
        formfield = DynamicFormField()
        formfield.dynamic_field_master = DynamicFormMaster.objects.filter(id__iexact=formmasterid).first()
        formfield.field_title = self.request.POST.get('field_title')
        formfield.field_type = fieldType
        formfield.field_hidden = self.request.POST.get('field_hidden')
        formfield.field_description = self.request.POST.get('field_description')
        formfield.field_original_name = getoriginalName(formmasterid)
        formfield.save()

        dropdownList = self.request.POST.get('dropdown_label')

        item = 1
        for dropi in dropdownList.split(','):
            dropdownfield = DynamicFormFieldDropdown()
            dropdownfield.dynamic_form_field = DynamicFormField.objects.filter(id__iexact=formfield.id).first()
            dropdownfield.dropdown_label = dropi
            dropdownfield.dropdown_value = item

            dropdownfield.save()
            item = item + 1
        return redirect('dynamicform:dynamicform_view', formmasterid)






