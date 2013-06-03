from django.contrib import admin
from invitation.models import InvitationKey, InvitationUser, InvitationRequest, InvitationCode


class InvitationKeyAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'from_user', 'date_invited', 'key_expired')


class InvitationUserAdmin(admin.ModelAdmin):
    list_display = ('inviter', 'invitations_remaining')


def invite_user(modeladmin, request, queryset):
    for invitation_request in queryset.all():
        invitation = InvitationKey.objects.create_invitation(request.user)
        invitation.send_to(invitation_request.email)
        invitation_request.invited = True
        invitation_request.save()

invite_user.short_description = "Invite selected invitation requests"


class InvitationRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'invited')
    actions = [invite_user]

admin.site.register(InvitationKey, InvitationKeyAdmin)
admin.site.register(InvitationUser, InvitationUserAdmin)
admin.site.register(InvitationRequest, InvitationRequestAdmin)
admin.site.register(InvitationCode)
