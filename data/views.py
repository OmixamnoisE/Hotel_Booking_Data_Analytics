from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Sum
from django.db.models import Count
from datetime import datetime
import urllib
from .models import Agents, Hotels, Reservations, Companies, Customers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    try:
        agent_count = Agents.objects.count()
        company_count = Companies.objects.count()
        customer_count = Customers.objects.count()
        hotel_count = Hotels.objects.count()
        reservation_count = Reservations.objects.count()

        repeat_guest_count = Customers.objects.filter(is_repeated_guest=True).count()

        reservations_per_hotel = Reservations.objects.values('hotel_id', 'hotel__hotel_name').annotate(
            count=Count('hotel_id')).order_by('-count')

        hotels_labels = [item['hotel__hotel_name'] for item in reservations_per_hotel]
        hotels_values = [item['count'] for item in reservations_per_hotel]

        cancelled_reservations = Reservations.objects.filter(reservation_status='Canceled').count()
        checked_out_reservations = Reservations.objects.filter(reservation_status='Check-Out').count()
        no_show_reservations = Reservations.objects.filter(reservation_status='No-Show').count()

        total_reservations = reservation_count

        cancelled_percent = (cancelled_reservations / total_reservations) * 100 if total_reservations else 0
        checked_out_percent = (checked_out_reservations / total_reservations) * 100 if total_reservations else 0
        no_show_percent = (no_show_reservations / total_reservations) * 100 if total_reservations else 0

        hotels = Hotels.objects.values_list('hotel_name', flat=True).distinct() 
        reservation_statuses = Reservations.objects.values_list('reservation_status', flat=True).distinct() 
        countries = Customers.objects.values_list('country', flat=True).distinct()
        customer_types = Reservations.objects.values_list('customer_type', flat=True).distinct() 
        agents = Agents.objects.values_list('agent_name', flat=True).distinct()

        print(f"Distinct reservation statuses: {reservation_statuses}")

        reservations_per_country = Reservations.objects.values('customer__country').annotate(reservation_count=Count('reservation_id'))

        country_data = {item['customer__country']: item['reservation_count'] for item in reservations_per_country}

        print(f"Country Data: {country_data}")

        age_group_data = Reservations.objects.aggregate(
            total_adults=Sum('adults'),
            total_children=Sum('children'),
            total_babies=Sum('babies')
        )

        age_group_dict = {
            'Adults': age_group_data['total_adults'] if age_group_data['total_adults'] else 0,
            'Children': age_group_data['total_children'] if age_group_data['total_children'] else 0,
            'Babies': age_group_data['total_babies'] if age_group_data['total_babies'] else 0
        }

        room_type_data = Reservations.objects.values('reserved_room_type', 'assigned_room_type') \
                                            .annotate(count=Count('reservation_id'))

        reserved_room_data = {}
        assigned_room_data = {}

        for item in room_type_data:
            if item['reserved_room_type']:
                reserved_room_data[item['reserved_room_type']] = item['count']
            if item['assigned_room_type']:
                assigned_room_data[item['assigned_room_type']] = item['count']

        omixamnoise = {
            'agent_count': agent_count,
            'company_count': company_count,
            'customer_count': customer_count,
            'hotel_count': hotel_count,
            'reservation_count': reservation_count,
            'repeat_guest_count': repeat_guest_count,
            'hotels_labels': hotels_labels,
            'hotels_values': hotels_values,
            'hotels': hotels,
            'reservation_statuses': reservation_statuses,
            'countries': countries,
            'customer_types': customer_types,
            'agents': agents,

            'cancelled_percent': cancelled_percent,
            'checked_out_percent': checked_out_percent,
            'no_show_percent': no_show_percent,

            'country_data': country_data,

            'age_group_data': age_group_dict,

            'reserved_room_data' : reserved_room_data,
            'assigned_room_data' : assigned_room_data,
        }
        return render(request, 'data/dashboard.html', omixamnoise)

    except Exception as e:
        print(f"Error in dashboard view: {e}")
        return render(request, 'data/dashboard.html', {'error': 'Unable to fetch data'})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'data/login.html')

def signup(request):
    return render(request, 'data/signup.html')

