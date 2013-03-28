from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from registration.forms import RegistrationFormTermsOfService

urlpatterns = patterns('invitation.views',
    url(r'^invite/complete/$',
                direct_to_template,
                {'template': 'invitation/invitation_complete.html'},
                name='invitation_complete'),
    url(r'^invite/$',
                'invite',
                name='invitation_invite'),
    url(r'^invited/(?P<invitation_key>\w+)/$', 
                'invited',
                name='invitation_invited'),
    url(r'^register/$',
                'register',
                { 'backend': 'registration.backends.default.DefaultBackend' },
                name='registration_register'),
    url(r'^invite_request/$',
                'invite_request',
                name='invitation_request'),
    url(r'^invite_request/complete/$',
                direct_to_template,
                {'template': 'invitation/invitation_request_complete.html'},
                name='invitation_request_complete'),
)
