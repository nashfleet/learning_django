from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from .models import Invitation
from .forms import InvitationForm

@login_required
def new_invitation(request):
  if request.method == 'POST':
    invitation = Invitation(from_user=request.user)
    form = InvitationForm(data=request.POST, instance=invitation)
    if form.is_valid():
      form.save()
      return redirect('userprofile_home')
  else:
    form = InvitationForm()
  return render(request, "tictactoe/new_invitation.html", {'form': form})

@login_required
def accept_invitation(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
            invitation.delete()
            return HttpResponse("Invitation Accepted!")
        else:
            invitation.delete()
            return redirect('userprofile_home')
    else:
        return render(request, "tictactoe/accept_invitation.html", {'invitation': invitation})