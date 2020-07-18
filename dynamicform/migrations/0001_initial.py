# Generated by Django 2.2.8 on 2020-07-05 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicFormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_title', models.CharField(max_length=255)),
                ('field_description', models.CharField(default=True, max_length=500)),
                ('field_type', models.IntegerField()),
                ('field_original_name', models.CharField(blank=True, max_length=50, null=True)),
                ('field_hidden', models.SmallIntegerField(default=0)),
                ('field_order', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DynamicFormMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('form_url', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_left_1', models.TextField(max_length=1000, null=True)),
                ('description_left_2', models.TextField(max_length=1000, null=True)),
                ('description_left_3', models.TextField(max_length=1000, null=True)),
                ('description_right_1', models.TextField(max_length=1000, null=True)),
                ('description_right_2', models.TextField(max_length=1000, null=True)),
                ('description_right_3', models.TextField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('form_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicform.DynamicFormMaster')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackBackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=255)),
                ('imageUrl', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('form_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicform.DynamicFormMaster')),
            ],
        ),
        migrations.CreateModel(
            name='DynamicFormValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.BigIntegerField(null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('dfcustom_1', models.CharField(max_length=10, null=True)),
                ('dfcustom_2', models.CharField(max_length=10, null=True)),
                ('dfcustom_3', models.CharField(max_length=10, null=True)),
                ('dfcustom_4', models.CharField(max_length=10, null=True)),
                ('dfcustom_5', models.CharField(max_length=10, null=True)),
                ('dfcustom_6', models.CharField(max_length=10, null=True)),
                ('dfcustom_7', models.CharField(max_length=10, null=True)),
                ('dfcustom_8', models.CharField(max_length=10, null=True)),
                ('dfcustom_9', models.CharField(max_length=10, null=True)),
                ('dfcustom_10', models.CharField(max_length=10, null=True)),
                ('dfcustom_11', models.CharField(max_length=10, null=True)),
                ('dfcustom_12', models.CharField(max_length=10, null=True)),
                ('dfcustom_13', models.CharField(max_length=10, null=True)),
                ('dfcustom_14', models.CharField(max_length=10, null=True)),
                ('dfcustom_15', models.CharField(max_length=10, null=True)),
                ('dfcustom_16', models.CharField(max_length=10, null=True)),
                ('dfcustom_17', models.CharField(max_length=10, null=True)),
                ('dfcustom_18', models.CharField(max_length=10, null=True)),
                ('dfcustom_19', models.CharField(max_length=10, null=True)),
                ('dfcustom_20', models.CharField(max_length=10, null=True)),
                ('dfcustom_21', models.CharField(max_length=10, null=True)),
                ('dfcustom_22', models.CharField(max_length=10, null=True)),
                ('dfcustom_23', models.CharField(max_length=10, null=True)),
                ('dfcustom_24', models.CharField(max_length=10, null=True)),
                ('dfcustom_25', models.CharField(max_length=10, null=True)),
                ('dfcustom_26', models.CharField(max_length=10, null=True)),
                ('dfcustom_27', models.CharField(max_length=10, null=True)),
                ('dfcustom_28', models.CharField(max_length=10, null=True)),
                ('dfcustom_29', models.CharField(max_length=10, null=True)),
                ('dfcustom_30', models.CharField(max_length=10, null=True)),
                ('dfcustom_31', models.CharField(max_length=10, null=True)),
                ('dfcustom_32', models.CharField(max_length=10, null=True)),
                ('dfcustom_33', models.CharField(max_length=10, null=True)),
                ('dfcustom_34', models.CharField(max_length=10, null=True)),
                ('dfcustom_35', models.CharField(max_length=10, null=True)),
                ('dfcustom_36', models.CharField(max_length=10, null=True)),
                ('dfcustom_37', models.CharField(max_length=10, null=True)),
                ('dfcustom_38', models.CharField(max_length=10, null=True)),
                ('dfcustom_39', models.CharField(max_length=10, null=True)),
                ('dfcustom_40', models.CharField(max_length=10, null=True)),
                ('dfcustom_41', models.CharField(max_length=10, null=True)),
                ('dfcustom_42', models.CharField(max_length=10, null=True)),
                ('dfcustom_43', models.CharField(max_length=10, null=True)),
                ('dfcustom_44', models.CharField(max_length=10, null=True)),
                ('dfcustom_45', models.CharField(max_length=10, null=True)),
                ('dfcustom_46', models.CharField(max_length=10, null=True)),
                ('dfcustom_47', models.CharField(max_length=10, null=True)),
                ('dfcustom_48', models.CharField(max_length=10, null=True)),
                ('dfcustom_49', models.CharField(max_length=10, null=True)),
                ('dfcustom_50', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('form_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicform.DynamicFormMaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='DynamicFormRelateWithAccountAndBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.Branch')),
                ('dynamic_form_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicform.DynamicFormMaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='DynamicFormFieldDropdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropdown_label', models.CharField(max_length=255)),
                ('dropdown_value', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dynamic_form_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicform.DynamicFormField')),
            ],
        ),
        migrations.AddField(
            model_name='dynamicformfield',
            name='dynamic_field_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicform.DynamicFormMaster'),
        ),
    ]