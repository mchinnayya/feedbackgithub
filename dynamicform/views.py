from django.conf.urls import url
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView
from django.core.paginator import Paginator
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView

from common.views import feedbackForm, formUrl, feedbackReport
from account.models import Account
from branch.models import Branch
from dynamicform.models import DynamicFormMaster, DynamicFormField, DynamicFormRelateWithAccountAndBranch, \
    DynamicFormValue, FeedbackBackgroundImage, FeedbackLayout, DynamicFormFieldDropdown
from dynamicform.forms import DynamicFormMasterForm, UserAssignForm
from feedback.settings import BASE_URL


class DynamicFormList(TemplateView):
    model = DynamicFormMaster
    context_object_name = 'dynamicform_list'
    template_name = 'dynamicform/dynamicform_list.html'

    paginate_by = 25

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()
        paginator = Paginator(queryset, 25)  # Show 25 contacts per page

        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)

        return contacts

    def get_context_data(self, **kwargs):
        context = super(DynamicFormList, self).get_context_data(**kwargs)
        context['dynamicforms'] = self.get_queryset()
        context['assignform'] =  UserAssignForm(self.request.POST or None)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class DynamicFormDetails(DetailView):
    model = DynamicFormMaster
    template_name = 'dynamicform/dynamicform_details.html'

    def get(self, request, pk):
        dynamicform = DynamicFormMaster.objects.filter(id=pk).first()

        fieldform = DynamicFormField.objects.filter(dynamic_field_master=pk).all().order_by('-id')

        context = {
            'dynamicform': dynamicform,
            'fieldforms': fieldform,

        }

        return render(request, self.template_name, context)


class DynamicFormCreate(CreateView):
    model = DynamicFormMaster
    form_class = DynamicFormMasterForm
    template_name = 'dynamicform/dynamicform_create.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        dynamicformmaster = DynamicFormMaster()
        dynamicformmaster.title = self.request.POST.get('title')
        dynamicformmaster.form_url = formUrl()
        dynamicformmaster.description = self.request.POST.get('description')
        dynamicformmaster.save()
        return redirect('dynamicform:dynamicform_list')

    def form_invalid(self, dynamicform):
        return render(self.request, self.template_name, {'dynamicform': dynamicform})

    def get_context_data(self, **kwargs):
        context = super(DynamicFormCreate, self).get_context_data(**kwargs)
        context["dynamicform"] = self.form_class
        return context



def dynamicform_update(request, pk):
    dynamicformmaster = DynamicFormMaster.objects.get(pk=pk)
    dynamicform = DynamicFormMasterForm(request.POST or None, instance=dynamicformmaster)
    if request.method == 'POST':
        if dynamicform.is_valid():
            dynamicform.title = request.POST.get('title')
            dynamicform.description = request.POST.get('description')
            dynamicform.save()
            return redirect('dynamicform:dynamicform_list')
    else:
        dynamicform = DynamicFormMasterForm(instance=dynamicformmaster)
    return render(request, 'dynamicform/dynamicform_update.html', {'dynamicform': dynamicform, 'pk': pk})


def dynamicform_delete(request):
    dynamicformmaster = DynamicFormMaster.objects.get(id=request.POST.get('dynamicformmasterid'))
    dynamicformmaster.delete()
    return HttpResponse(True)

def dynamicform_search(request):
    if request.method == 'GET':
        queryset = DynamicFormMaster.objects.all().order_by('-id')
        query = request.GET.get("q")
        if query:
                queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()
        paginator = Paginator(queryset, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        dynamicform = paginator.get_page(page)

    return render(request,"dynamicform/dynamicform_search.html",{"name":dynamicform})


def user_assign(request):
    user = request.POST.get('user')
    userassign = DynamicFormRelateWithAccountAndBranch.objects.get(id=user)
    assignform = UserAssignForm(request.POST or None, instance=userassign)
    if request.method == 'POST':
        if assignform.is_valid():
            userassign.user = request.POST.get('user')
            userassign.save()
            return redirect('dynamicform:dynamicform_list')
    else:
        assignform = UserAssignForm(instance=userassign)
    return render(request, 'dynamicform/dynamicform_list.html', {'assignform': assignform})

# def user_assign(request):
#     userassign = DynamicFormRelateWithAccountAndBranch()
#     if request.method == 'POST':
#         userassign.user = Account.objects.get(id=request.POST.get('user'))
#         userassign.branch = Branch.objects.get(id=request.POST.get('branch'))
#         userassign.dynamic_form_master = DynamicFormMaster.get(id=request.POST.get('dynamic_form_master'))
#         userassign.save()
#         return redirect('dynamicform:dynamicform_list')
#     return redirect('dynamicform:dynamicform_list')


class feedbackDetails(TemplateView):
    model = DynamicFormValue
    context_object_name = 'feedback'
    template_name = 'dynamicform/feedback_main.html'

    def get_context_data(self, pk, **kwargs):
        image = FeedbackBackgroundImage.objects.filter(form_master_id=pk)
        layout = FeedbackLayout.objects.get(form_master_id=pk)
        # print(layout.description_left_2)
        context = super(feedbackDetails, self).get_context_data(**kwargs)

        context['feedbackForm'] = feedbackForm(pk)
        context['image'] = image
        context['layout'] = layout
        return context

    def post(self, request, pk):
        dynamicform = DynamicFormValue()
        dynamicform.form_master = DynamicFormMaster.objects.get(id=pk)
        dynamicform.user = Account.objects.get(id=1)
        dynamicform.mobile_number = request.POST.get('mobile_number')
        dynamicform.dfcustom_1 = request.POST.get("custom_01")
        dynamicform.dfcustom_2 = request.POST.get("custom_02")
        dynamicform.dfcustom_3 = request.POST.get("custom_03")
        dynamicform.dfcustom_4 = request.POST.get("custom_04")
        dynamicform.dfcustom_5 = request.POST.get("custom_05")
        dynamicform.dfcustom_6 = request.POST.get("custom_06")
        dynamicform.dfcustom_7 = request.POST.get("custom_07")
        dynamicform.dfcustom_8 = request.POST.get("custom_08")
        dynamicform.dfcustom_9 = request.POST.get("custom_09")
        dynamicform.dfcustom_10 = request.POST.get("custom_10")

        dynamicform.save()

        return redirect('dynamicform:feedback',pk)


# def urlpage_view(request,formmasterid=None):
#
#     image= FeedbackBackgroundImage.objects.filter(form_master_id=formmasterid)
#
#     for i in image:
#
#         print(i.imageUrl)
#     return render(request, 'dynamicform/feedback_main.html',{'image':image})

# class Report(View):
#     template_name = 'dynamicform/feedback_report.html'
#
#     def get(self, request, formmasterid):
#         masterform = DynamicFormMaster.objects.get(id=formmasterid)
#         fieldform = DynamicFormField.objects.filter(dynamic_field_master_id=formmasterid)
#         dropdownlable = DynamicFormFieldDropdown.objects.filter(dynamic_form_field_id=formmasterid)
#         rating_value = DynamicFormValue.objects.filter(form_master_id=formmasterid)
#
#         import mysql.connector
#
#         cnx = mysql.connector.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='feedback_db')
#         import pandas as pd
#
#         # db_connection = sql.connect(host='localhost', database='feedback_db', user='root', password='')
#
#         dataframe = pd.read_sql_query("SELECT * FROM dynamicform_dynamicformvalue",cnx)
#         dataframe1 = dataframe[dataframe["form_master_id"]==formmasterid]
#         # total_response = dataframe1["form_master_id"].count()
#         df1 = dataframe1.dropna(how='all', axis=1)
#         print(df1.shape)
#         total_response=[]
#         column= list(df1.columns)
#         for name in column[2:-4]:
#             data = dataframe1[name].count()
#             total_response.append(data)
#         print(total_response)
#         # for i in rating_value:
#         #     print(i.dfcustom_1.count())
#         context = {
#
#             'masterform': masterform,
#             "dropdownlable":dropdownlable,
#             'fieldform': fieldform,
#             "total_response":total_response
#         }
#
#         return render(request, self.template_name,context)


class Report(TemplateView):
    template_name = 'dynamicform/feedback_report.html'
    context_object_name = 'report'
    def get_context_data(self, formmasterid, **kwargs):
        masterform = DynamicFormMaster.objects.get(id=formmasterid)
        context = super(Report, self).get_context_data(**kwargs)

        context['feedbackReport'] = feedbackReport(formmasterid)
        context['masterform'] = masterform
        return context


# def feedbackform_list_view(request):
#     return render(request, 'dynamicform/formlist.html')

def test(request):

    return HttpResponse(BASE_URL)


def demo(request,formmasterid):
    # field_details = DynamicFormField.objects.filter(dynamic_field_master_id=formmasterid)
    total_response = DynamicFormValue.objects.filter(form_master_id=formmasterid)
    for i in total_response:
        count=i.dfcustom_1
        # print(i.dfcustom_1)
        return HttpResponse(count)