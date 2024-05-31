from django.shortcuts import render
from django.http import HttpResponse
from Googleforms.models import GoogleForm
from Surveymonkey.models import SurveyMonkeySurvey
from Typeforms.models import Feedback
from Zendesk.models import ZendeskUser
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request,"index.html")
@login_required
def Googleforms(request):
    googleforms = GoogleForm.objects.all()
    return render(request, "Googleforms.html" ,{'GoogleForm': googleforms})
@login_required
def Surveymonkey(request):
    surveymonkey = SurveyMonkeySurvey.objects.all()
    return render(request, "Surveymonkey.html" ,{'SurveyMonkeySurvey': surveymonkey})
@login_required
def Typeforms(request): 
    typeforms = Feedback.objects.all()
    return render(request, "Typeforms.html" ,{'Feedback': typeforms})
@login_required
def Zendesk(request):
    zendesk = ZendeskUser.objects.all()
    return render(request, "Zendesk.html" ,{'ZendeskUser': zendesk})
@login_required
def forms(request):
    # Your view logic here
    return render(request, 'GoogleForm_form.html')