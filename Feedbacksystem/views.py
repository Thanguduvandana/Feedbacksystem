from django.shortcuts import render
from django.http import HttpResponse
from Googleforms.models import GoogleForm
from Surveymonkey.models import SurveyMonkeySurvey
from Typeforms.models import Feedback
from Zendesk.models import ZendeskUser
def index(request):
    return render(request,"index.html")
def Googleforms(request):
    googleforms = GoogleForm.objects.all()
    return render(request, "Googleforms.html" ,{'GoogleForm': googleforms})
def Surveymonkey(request):
    surveymonkey = SurveyMonkeySurvey.objects.all()
    return render(request, "Surveymonkey.html" ,{'SurveyMonkeySurvey': surveymonkey})
def Typeforms(request):
    typeforms = Feedback.objects.all()
    return render(request, "Typeforms.html" ,{'Feedback': typeforms})
def Zendesk(request):
    zendesk = ZendeskUser.objects.all()
    return render(request, "Zendesk.html" ,{'ZendeskUser': zendesk})
def forms(request):
    # Your view logic here
    return render(request, 'GoogleForm_form.html')