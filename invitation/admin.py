from django.contrib import admin
from invitation.models import InvitationKey, InvitationUser, InvitationRequest, InvitationCode

class InvitationKeyAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'from_user', 'date_invited', 'key_expired')

class InvitationUserAdmin(admin.ModelAdmin):
    list_display = ('inviter', 'invitations_remaining')

admin.site.register(InvitationKey, InvitationKeyAdmin)
admin.site.register(InvitationUser, InvitationUserAdmin)
admin.site.register(InvitationRequest)
admin.site.register(InvitationCode)
