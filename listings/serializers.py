from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    host_name = serializers.CharField(source='host.username', read_only=True)
    
    class Meta:
        model = Listing
        fields = [
            'listing_id', 'title', 'description', 'price_per_night', 
            'property_type', 'host', 'host_name', 'max_guests', 
            'bedrooms', 'bathrooms', 'created_at'
        ]
        read_only_fields = ['listing_id', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    guest_name = serializers.CharField(source='guest.username', read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'booking_id', 'listing', 'listing_title', 'guest', 'guest_name',
            'check_in', 'check_out', 'total_price', 'status', 'created_at'
        ]
        read_only_fields = ['booking_id', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    guest_name = serializers.CharField(source='guest.username', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'review_id', 'listing', 'guest', 'guest_name', 
            'rating', 'comment', 'created_at'
        ]
        read_only_fields = ['review_id', 'created_at']