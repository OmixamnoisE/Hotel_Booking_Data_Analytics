from django.db import models

class Agents(models.Model):
    agent_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agents'

class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    is_repeated_guest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'

class Hotels(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hotels'


class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, models.DO_NOTHING)
    is_canceled = models.IntegerField(blank=True, null=True)
    lead_time = models.IntegerField(blank=True, null=True)
    arrival_date_year = models.IntegerField(blank=True, null=True)
    arrival_date_month = models.CharField(max_length=20, blank=True, null=True)
    arrival_date_week_number = models.IntegerField(blank=True, null=True)
    arrival_date_day_of_month = models.IntegerField(blank=True, null=True)
    stays_in_weekend_nights = models.IntegerField(blank=True, null=True)
    stays_in_week_nights = models.IntegerField(blank=True, null=True)
    adults = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    babies = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    previous_cancellations = models.IntegerField(blank=True, null=True)
    previous_bookings_not_canceled = models.IntegerField(blank=True, null=True)
    reserved_room_type = models.CharField(max_length=1, blank=True, null=True)
    assigned_room_type = models.CharField(max_length=1, blank=True, null=True)
    deposit_type = models.CharField(max_length=50, blank=True, null=True)
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    days_in_waiting_list = models.IntegerField(blank=True, null=True)
    customer_type = models.CharField(max_length=50, blank=True, null=True)
    required_car_parking_spaces = models.IntegerField(blank=True, null=True)
    total_of_special_requests = models.IntegerField(blank=True, null=True)
    reservation_status = models.CharField(max_length=50, blank=True, null=True)
    reservation_status_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservations'
