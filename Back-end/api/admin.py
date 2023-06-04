from django.contrib import admin
# from .models import Driver, Ride
from .models import TaxiDetails, NewDriver, NewRideDetails, Earnings

# admin.site.register(Driver)
# admin.site.register(Ride)

admin.site.register(TaxiDetails)
admin.site.register(NewDriver)
admin.site.register(NewRideDetails)
admin.site.register(Earnings)