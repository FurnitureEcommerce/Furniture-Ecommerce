import re
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import UserProfile, Address

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'phone', 'username', 'password']

    def validate_full_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Full name must be at least 3 characters.")
        if not re.match(r'^[A-Za-z ]+$', value):
            raise serializers.ValidationError("Full name must contain only letters and spaces.")
        return value

    def validate_email(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise serializers.ValidationError("Enter a valid email address.")
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def validate_phone(self, value):
        if not re.match(r'^\+?[1-9]\d{1,3}[6-9]\d{9}$', value):
            raise serializers.ValidationError("Enter a valid phone number with country code.")
        if value.count("0") >= 12:
            raise serializers.ValidationError("Invalid phone number.")
        if CustomUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone number is already registered.")
        return value

    def validate_username(self, value):
        if not re.search(r'[^A-Za-z0-9]', value):
            raise serializers.ValidationError("Username must contain at least one special character.")
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must include at least one uppercase letter.")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Password must include at least one lowercase letter.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Password must include at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("Password must include at least one special character.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    user_input = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user_input = data.get('user_input')
        password = data.get('password')

       
        try:
            user = User.objects.get(Q(email=user_input) | Q(username=user_input))
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or username")

        
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        
        if not user.is_active:
            raise serializers.ValidationError("Account is blocked or inactive")

        data['user'] = user
        return data
    

   

class UserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    phone = serializers.CharField(source='user.phone', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'phone', 'gender', 'dob', 'profile_image']

    def validate_dob(self, value):
        from datetime import date
        if value >= date.today():
            raise serializers.ValidationError("DOB cannot be in the future")
        return value


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def validate_address_line1(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Address Line 1 must be at least 5 characters")
        return value

    def validate_city(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("City must only contain letters")
        return value

    def validate_district(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("District must only contain letters")
        return value

    def validate_state(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("State must only contain letters")
        return value

    def validate_pincode(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("Pincode must be a 6-digit number")
        return value
