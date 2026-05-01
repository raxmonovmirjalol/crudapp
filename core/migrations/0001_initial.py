from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to='core.action')),
            ],
            options={'ordering': ['order', 'id']},
        ),
    ]
