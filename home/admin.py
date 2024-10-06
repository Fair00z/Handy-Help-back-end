from django.contrib import admin
from . models import Worker_Detail,Worker_Dashboard,Worker,Client,Comment,Client_Detail,Client_Dashboard,Job_post

# Register your models here.
admin.site.register(Worker_Detail)
admin.site.register(Worker_Dashboard)
admin.site.register(Client_Dashboard)
admin.site.register(Worker)
admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(Client_Detail)
admin.site.register(Job_post)