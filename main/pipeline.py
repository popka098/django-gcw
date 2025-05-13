from django.contrib.auth.models import User
from main.models import Profile

def update_profile_from_google(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        profile = Profile.objects.get(user=user)
        profile.first_name = response.get('given_name', '')
        profile.last_name = response.get('family_name', '')
        profile.email = response.get('email', '')
        profile.save()