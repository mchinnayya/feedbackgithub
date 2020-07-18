from django.conf.urls import url
from django.core.files import images
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from dynamicform.models import DynamicFormField, DynamicFormFieldDropdown, DynamicFormMaster,DynamicFormValue
import numpy as np
from feedback.settings import STATICFILES_DIRS, BASE_URL
from static import images


def baseapp(request):
    return render(request, 'layout/app.html', {})



def getoriginalName(formmasterid):
    field_original_name = DynamicFormField.objects.filter(dynamic_field_master_id=formmasterid)
    array1 = np.array(["custom_01","custom_02", "custom_03", "custom_04","custom_05","custom_06","custom_07", "custom_08", "custom_09","custom_10","custom_11","custom_12", "custom_13", "custom_14","custom_15","custom_16","custom_17", "custom_18", "custom_19","custom_20"])
    array2 = np.array([])
    for orgName in field_original_name:
        array2 = np.append(array2, orgName.field_original_name)

    src = np.setdiff1d(array1, array2)[0]
    return src


def formUrl():
    last_form_url = DynamicFormMaster.objects.all().order_by('id').last()
    print (last_form_url)
    if not last_form_url:
         return 'dynamicform/feedback/1'
    form_url = last_form_url.form_url
    formUrl_int = int(form_url.split('dynamicform/feedback/')[-1])
    new_formUrl_int = formUrl_int + 1
    new_formUrl = 'dynamicform/feedback/' + str(new_formUrl_int)
    return new_formUrl


# rec=0
# def autoIncrement():
#  global rec
#  pStart = 1
#  pInterval = 1
#  if (rec == 0):
#   rec = pStart
#  else:
#   rec = rec + pInterval
#  return rec

def feedbackForm(formmasterid):
    field_details = DynamicFormField.objects.filter(dynamic_field_master_id=formmasterid)

    str1 = "<table>"

    for field in field_details:
        print(field.field_type)
        field_dropDown = DynamicFormFieldDropdown.objects.filter(dynamic_form_field_id=field.id)
        if int(field.field_type) == 113:#star
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            label_count = 1
            for fielddropdown in field_dropDown:
                "<tr>"
                if label_count == 1:
                    str1 +="<td>" '<input type="radio"  name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 2:
                    str1 +="<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 3:
                    str1 += "<td>"'<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 4:
                    str1 +="<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 5:
                    str1 += "<td>"'<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                label_count = label_count + 1
                "</tr>"
        elif int(field.field_type) == 114: #Emojee
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            label_count = 1
            for fielddropdown in field_dropDown:
                "<tr>"
                if label_count == 1:
                    str1 +="<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/1.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 2:
                    str1 +="<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/2.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 3:
                    str1 +="<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/3.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 4:
                    str1 += "<td>"'<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/4.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 5:
                    str1 += "<td>"'<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><img src="'+BASE_URL+'static/images/5.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                label_count = label_count + 1
                "</tr>"
        elif field.field_type == 115:#slider
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            label_count = 1
            for fielddropdown in field_dropDown:
                "<tr>"
                if label_count == 1:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>1</button>'"</td>"
                elif label_count == 2:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>2</button>'"</td>"
                elif label_count == 3:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>3</button>'"</td>"
                elif label_count == 4:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>4</button>'"</td>"
                elif label_count == 5:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>5</button>'"</td>"
                elif label_count == 6:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>6</button>'"</td>"
                elif label_count == 7:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>7</button>'"</td>"
                elif label_count == 8:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>8</button>'"</td>"
                elif label_count == 9:
                    str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>9</button>'"</td>"
                elif label_count == 10:
                    str1 += "<td>"'<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/><button type="button" style="width:80px;height:80px;" label="' + fielddropdown.dropdown_label + '"/>10</button>'"</td>"
                label_count =  label_count + 1
                "</tr>"
        elif field.field_type == 116:#multipal choice single select
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            for fielddropdown in field_dropDown:
                "<tr>"
                str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/>'  + fielddropdown.dropdown_label + '</td>'
                "</tr>"

        elif field.field_type == 117:#dropdown list
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            str1 += "<tr>""<td>" '<select  name="' + field.field_original_name + '" class="form-control" />'\
                        '<option selected="selected" disabled>Select:</option>'\
                        '<option value="excellent">excellent</option>' \
                        '<option value="Very Good">Very Good</option>' \
                        '<option value="Good">Good</option>' \
                        '<option value="Avrege">Avrege</option>' \
                        '<option value="Poor">Poor</option>' \
                        '<option value="Very Poor">Very Poor</option>''</select>' "</td>""</tr>"


        elif field.field_type == 118:#text box
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"

            str1 +="<tr>""<td>" '<input type="text" name="' + field.field_original_name + '" class="form-control" />' "</td>""</tr>"
    str1 +="</table>"
    return str1

def feedbackReport(formmasterid):
    field_details = DynamicFormField.objects.filter(dynamic_field_master_id=formmasterid)
    total_response = DynamicFormValue.objects.filter(form_master_id=formmasterid)
    for i in total_response:
        print(i.dfcustom_1)

    str1 = "<table>"

    for field in field_details:
        # print(field.field_type)
        field_dropDown = DynamicFormFieldDropdown.objects.filter(dynamic_form_field_id=field.id)
        if int(field.field_type) == 113:#star
            str1 +="<tr>""<td>"   + field.field_title +  '</lavel>'"</td>""</tr>"
            label_count = 1
            for fielddropdown in field_dropDown:
                "<tr>"
                if label_count == 1:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 2:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 3:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 4:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 5:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/star.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                label_count = label_count + 1
                "</tr>"
        elif int(field.field_type) == 114: #Emojee
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            label_count = 1
            for fielddropdown in field_dropDown:
                "<tr>"
                if label_count == 1:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/1.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 2:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/2.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 3:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/3.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 4:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/4.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                elif label_count == 5:
                    str1 +="<td>" '<img src="'+BASE_URL+'static/images/5.png" label="' + fielddropdown.dropdown_label + '"/>'"</td>"
                label_count = label_count + 1
                "</tr>"
        elif field.field_type == 115:#slider
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            label_count = 1
            for fielddropdown in field_dropDown:
                "<tr>"
                if label_count == 1:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>1</button>'"</td>"
                elif label_count == 2:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>2</button>'"</td>"
                elif label_count == 3:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>3</button>'"</td>"
                elif label_count == 4:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>4</button>'"</td>"
                elif label_count == 5:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>5</button>'"</td>"
                elif label_count == 6:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>6</button>'"</td>"
                elif label_count == 7:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>7</button>'"</td>"
                elif label_count == 8:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>8</button>'"</td>"
                elif label_count == 9:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>9</button>'"</td>"
                elif label_count == 10:
                    str1 += "<td>" '<button type="button" style="width:80px;height:80px;"  label="' + fielddropdown.dropdown_label + '"/>10</button>'"</td>"
                label_count =  label_count + 1
                "</tr>"
        elif field.field_type == 116:#multipal choice single select
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            for fielddropdown in field_dropDown:
                "<tr>"
                str1 += "<td>" '<input type="radio" name="' + field.field_original_name + '" class="form-control" value="' + fielddropdown.dropdown_value + '"/>'  + fielddropdown.dropdown_label + '</td>'
                "</tr>"

        elif field.field_type == 117:#dropdown list
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"
            str1 += "<tr>""<td>" '<select  name="' + field.field_original_name + '" class="form-control" />'\
                        '<option selected="selected" disabled>Select:</option>'\
                        '<option value="excellent">excellent</option>' \
                        '<option value="Very Good">Very Good</option>' \
                        '<option value="Good">Good</option>' \
                        '<option value="Avrege">Avrege</option>' \
                        '<option value="Poor">Poor</option>' \
                        '<option value="Very Poor">Very Poor</option>''</select>' "</td>""</tr>"


        elif field.field_type == 118:#text box
            str1 +="<tr>""<td>"  '<lavel>' + field.field_title + '</lavel>'"</td>""</tr>"

            str1 +="<tr>""<td>" '<input type="text" name="' + field.field_original_name + '" class="form-control" />' "</td>""</tr>"
    str1 +="</table>"
    return str1





















