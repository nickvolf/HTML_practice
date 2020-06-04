# Generated by Django 3.0.3 on 2020-06-03 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200603_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseSentenceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.CharField(max_length=120)),
                ('wrong_asnwer1', models.CharField(max_length=120)),
                ('wrong_asnwer2', models.CharField(max_length=120)),
                ('wrong_asnwer3', models.CharField(max_length=120)),
                ('points', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChooseWordQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence_text_pre', models.CharField(max_length=120)),
                ('sentence_text_post', models.CharField(max_length=120)),
                ('correct_answer', models.CharField(max_length=20)),
                ('wrong_asnwer1', models.CharField(max_length=20)),
                ('wrong_asnwer2', models.CharField(max_length=20)),
                ('wrong_asnwer3', models.CharField(max_length=20)),
                ('points', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MCImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_locaction', models.CharField(max_length=120)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='PosNegQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.CharField(max_length=120)),
                ('wrong_asnwer1', models.CharField(max_length=120)),
                ('points', models.PositiveIntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.MCImage')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=120)),
                ('correct_answer', models.CharField(max_length=120)),
                ('wrong_asnwer1', models.CharField(max_length=120)),
                ('points', models.PositiveIntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.MCImage')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='choosewordquestion',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.MCImage'),
        ),
        migrations.AddField(
            model_name='choosesentencequestion',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.MCImage'),
        ),
    ]
