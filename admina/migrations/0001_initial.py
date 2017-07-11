# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Describe', models.TextField(max_length=200, null=True)),
                ('State', models.PositiveIntegerField(default=0)),
                ('SendTime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Content', models.TextField(max_length=200)),
                ('IsUse', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Creation',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Describe', models.TextField(max_length=200, null=True)),
                ('Name', models.CharField(max_length=20)),
                ('IsUse', models.BooleanField(default=True)),
                ('Img', models.ImageField(upload_to='photos/creation')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Priority', models.PositiveIntegerField(default=0)),
                ('Type', models.PositiveIntegerField(default=0)),
                ('Date', models.DateField(auto_now_add=True)),
                ('IsRead', models.BooleanField(default=False)),
                ('Content', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('creation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Praise_Creation_set', to='admina.Creation')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(max_length=20, unique=True)),
                ('Description', models.TextField(max_length=200)),
                ('StartTime', models.DateField(auto_now_add=True)),
                ('EndTime', models.DateField()),
                ('Statue', models.PositiveIntegerField(default=0)),
                ('Number', models.PositiveIntegerField(default=1)),
                ('Img', models.ImageField(upload_to='photos/project')),
                ('Summary', models.TextField(max_length=200, null=True)),
                ('Progress', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project2ProjectLabel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Project2ProjectLabel_Project_set', to='admina.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLabel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectLabelName', models.CharField(max_length=20)),
                ('IsUse', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProjectLabel_Project_set', to='admina.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Identity', models.PositiveIntegerField(default=0)),
                ('Evaluate', models.TextField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProjectUser_Project_set', to='admina.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('StartTime', models.DateField(auto_now_add=True)),
                ('EndTime', models.DateField(null=True)),
                ('Describe', models.TextField(max_length=200)),
                ('State', models.PositiveIntegerField(default=0)),
                ('Times', models.PositiveIntegerField(default=1)),
                ('PredictNuber', models.PositiveIntegerField(default=1)),
                ('RecruitedNuber', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Recruit_Project_set', to='admina.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ReportDate', models.DateField(auto_now_add=True)),
                ('DealTime', models.DateField(null=True)),
                ('State', models.PositiveIntegerField(default=0)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Report_Comment_set', to='admina.Comment')),
                ('creation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Report_Creation_set', to='admina.Creation')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Report_Project_set', to='admina.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Level', models.PositiveIntegerField(default=0)),
                ('Value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreChange',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Event', models.CharField(max_length=30, null=True)),
                ('Date', models.DateField(auto_now_add=True)),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ScoreChange_Score_set', to='admina.Score')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=10, unique=True)),
                ('Account', models.CharField(max_length=20, unique=True)),
                ('PassWord', models.CharField(max_length=20)),
                ('Identity', models.PositiveSmallIntegerField(default=0)),
                ('Sex', models.PositiveSmallIntegerField(default=0)),
                ('Email', models.EmailField(max_length=32, unique=True)),
                ('Score', models.PositiveIntegerField(default=0)),
                ('RegistTime', models.DateField(auto_now_add=True)),
                ('Phone', models.CharField(max_length=12)),
                ('Img', models.ImageField(null=True, upload_to='photos/user')),
                ('Introduction', models.TextField(max_length=200, null=True)),
                ('School', models.CharField(max_length=20, null=True)),
                ('Institude', models.CharField(max_length=20, null=True)),
                ('Major', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User2UserLabel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User2UserLabel_User_set', to='admina.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserLabel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('IsUse', models.BooleanField(default=True)),
                ('Name', models.CharField(max_length=20, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserLabel_Project_set', to='admina.Project')),
            ],
        ),
        migrations.AddField(
            model_name='user2userlabel',
            name='userLabel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User2UserLabel_UserLabel_set', to='admina.UserLabel'),
        ),
        migrations.AddField(
            model_name='scorechange',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ScoreChange_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Report_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProjectUser_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='project2projectlabel',
            name='projectLabel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Project2ProjectLabel_ProjectLabel_set', to='admina.ProjectLabel'),
        ),
        migrations.AddField(
            model_name='praise',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Praise_Project_set', to='admina.Project'),
        ),
        migrations.AddField(
            model_name='praise',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Praise_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Message_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='follow',
            name='Follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Follow_Follower_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='follow',
            name='creation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Follow_Creation_set', to='admina.Creation'),
        ),
        migrations.AddField(
            model_name='follow',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Follow_Project_set', to='admina.Project'),
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Follow_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='creation',
            name='projectlabel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Creation_ProjectLabel_set', to='admina.ProjectLabel'),
        ),
        migrations.AddField(
            model_name='creation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Creation_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='creation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comment_Creation_set', to='admina.Creation'),
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comment_Project_set', to='admina.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment_User_set', to='admina.User'),
        ),
        migrations.AddField(
            model_name='apply',
            name='recruit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Apply_Recruit_set', to='admina.Recruit'),
        ),
        migrations.AddField(
            model_name='apply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Apply_User_set', to='admina.User'),
        ),
    ]