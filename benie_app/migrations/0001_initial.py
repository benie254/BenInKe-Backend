# Generated by Django 4.2.1 on 2023-06-07 08:43

import benie_app.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=120)),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_published', models.DateField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('words', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=220, null=True)),
                ('message', models.TextField(blank=True, max_length=9000, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, default='Beautiful piece!', max_length=2500, null=True)),
                ('commented_by', models.CharField(blank=True, default='Anonymous', max_length=120, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('replies', models.IntegerField(blank=True, null=True)),
                ('chapter', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('message', models.CharField(default='', max_length=1200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.URLField(blank=True, max_length=1000, null=True)),
                ('img', models.URLField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=120)),
                ('cover', models.URLField(default='', max_length=1000)),
                ('cover_source', models.URLField(blank=True, default='', max_length=1000, null=True)),
                ('excerpt', models.TextField(default='', max_length=2000)),
                ('description', models.TextField(default='', max_length=5000)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('words', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Spoken-Word', 'Spoken-Word'), ('Poetic-Chains', 'Poetic-Chains'), ('Poetic-Notes', 'Poetic-Notes'), ('One-Liners', 'One-Liners'), ('Poems', 'Poems')], default='', max_length=60)),
                ('tag', models.CharField(blank=True, choices=[('love', 'love'), ('life', 'life')], default='', max_length=60, null=True)),
                ('status', models.CharField(blank=True, choices=[('pinned', 'pinned'), ('unpinned', 'unpinned')], default='', max_length=60, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=220, null=True, unique=True)),
                ('date_subscribed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=120)),
                ('author_pic', models.URLField(default='', max_length=1000)),
                ('cover', models.URLField(default='', max_length=1000)),
                ('title', models.CharField(default='', max_length=120)),
                ('description', models.TextField(default='', max_length=5000)),
                ('category', models.CharField(choices=[('short-story', 'short-story'), ('novel', 'novel'), ('novelette', 'novelette'), ('play', 'play'), ('flash-fiction', 'flash-fiction')], default='', max_length=60)),
                ('genre', models.CharField(choices=[('mystery', 'mystery'), ('drama', 'drama'), ('thriller', 'thriller'), ('drama', 'drama'), ('mystery-thriller', 'mystery-thriller'), ('action', 'action'), ('romance', 'romance'), ('teen-fiction', 'teen-fiction')], default='', max_length=60)),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_published', models.DateField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('completed', 'completed'), ('ongoing', 'ongoing')], default='', max_length=60)),
                ('pin', models.CharField(blank=True, choices=[('pinned', 'pinned'), ('unpinned', 'unpinned')], default='', max_length=60, null=True)),
                ('words', models.PositiveIntegerField(blank=True, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('comments', models.IntegerField(blank=True, null=True)),
                ('chaps', models.IntegerField(blank=True, null=True)),
                ('chap1_id', models.IntegerField(blank=True, null=True)),
                ('tagged', models.ManyToManyField(blank=True, null=True, to='benie_app.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=True, default='', max_length=2500, null=True)),
                ('replied_by', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.feedback')),
                ('poem', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.poem')),
                ('story', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.story')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.CharField(blank=True, choices=[('like', 'like'), ('dislike', 'dislike')], default='', max_length=60, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('chapter', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.chapter')),
                ('comment', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.feedback')),
                ('poem', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.poem')),
                ('story', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.story')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=120)),
                ('cover', models.URLField(default='', max_length=1000)),
                ('description', models.TextField(default='', max_length=5000)),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('words', models.PositiveIntegerField(blank=True, null=True)),
                ('chapter', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.chapter')),
                ('story', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.story')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='poem',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.poem'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='story',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.story'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='story',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='benie_app.story'),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with this username already exists.'}, help_text='Required. 60 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=60, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('email', models.EmailField(error_messages={'unique': 'A user with this email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', benie_app.models.MyAccountManager()),
            ],
        ),
    ]
