from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'
    
    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create sample users if they don't exist
        hosts = []
        guests = []
        
        for i in range(1, 4):
            host, created = User.objects.get_or_create(
                username=f'host{i}',
                defaults={
                    'email': f'host{i}@example.com',
                    'first_name': f'Host{i}',
                    'last_name': 'Smith'
                }
            )
            if created:
                host.set_password('password123')
                host.save()
            hosts.append(host)
            
        for i in range(1, 6):
            guest, created = User.objects.get_or_create(
                username=f'guest{i}',
                defaults={
                    'email': f'guest{i}@example.com',
                    'first_name': f'Guest{i}',
                    'last_name': 'Johnson'
                }
            )
            if created:
                guest.set_password('password123')
                guest.save()
            guests.append(guest)
        
        # Sample listings data
        listings_data = [
            {
                'title': 'Cozy Apartment in Downtown',
                'description': 'Beautiful apartment in the heart of the city',
                'price_per_night': 120.00,
                'property_type': 'apartment',
                'max_guests': 4,
                'bedrooms': 2,
                'bathrooms': 1,
            },
            {
                'title': 'Luxury Villa with Pool',
                'description': 'Stunning villa with private pool and ocean view',
                'price_per_night': 350.00,
                'property_type': 'villa',
                'max_guests': 8,
                'bedrooms': 4,
                'bathrooms': 3,
            },
            {
                'title': 'Modern Condo Near Beach',
                'description': 'Recently renovated condo just steps from the beach',
                'price_per_night': 95.00,
                'property_type': 'condo',
                'max_guests': 2,
                'bedrooms': 1,
                'bathrooms': 1,
            },
        ]
        
        # Create listings
        listings = []
        for i, data in enumerate(listings_data):
            listing, created = Listing.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'price_per_night': data['price_per_night'],
                    'property_type': data['property_type'],
                    'host': hosts[i % len(hosts)],
                    'max_guests': data['max_guests'],
                    'bedrooms': data['bedrooms'],
                    'bathrooms': data['bathrooms'],
                }
            )
            listings.append(listing)
        
        # Create sample bookings
        for i in range(10):
            listing = random.choice(listings)
            guest = random.choice(guests)
            check_in = datetime.now().date() + timedelta(days=random.randint(1, 30))
            check_out = check_in + timedelta(days=random.randint(1, 14))
            nights = (check_out - check_in).days
            total_price = nights * float(listing.price_per_night)
            
            Booking.objects.get_or_create(
                listing=listing,
                guest=guest,
                check_in=check_in,
                check_out=check_out,
                defaults={
                    'total_price': total_price,
                    'status': random.choice(['pending', 'confirmed', 'completed'])
                }
            )
        
        # Create sample reviews
        for listing in listings:
            for i in range(random.randint(1, 3)):
                guest = random.choice(guests)
                Review.objects.get_or_create(
                    listing=listing,
                    guest=guest,
                    defaults={
                        'rating': random.randint(4, 5),
                        'comment': f'Great stay at {listing.title}! Would recommend.'
                    }
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully seeded database with '
                f'{len(listings)} listings, '
                f'{Booking.objects.count()} bookings, '
                f'{Review.objects.count()} reviews'
            )
        )