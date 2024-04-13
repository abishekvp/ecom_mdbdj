from django.contrib.auth.models import Group

new_group, created = Group.objects.get_or_create(name='user_admin')
new_group, created = Group.objects.get_or_create(name='per_user')
new_group, created = Group.objects.get_or_create(name='plumber')
new_group, created = Group.objects.get_or_create(name='prime')
