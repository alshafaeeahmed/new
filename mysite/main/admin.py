from django.contrib import admin
from .models import Volunteer
from .models import Elderly
from .models import Maneger
from .models import Review

admin.site.register(Volunteer)
admin.site.register(Elderly)
admin.site.register(Maneger)
admin.site.register(Review)