from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from demoapp.models import IrisData
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import numpy as np
import joblib
import os

filePath = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'ml-models/IrisModel.pkl')
IrisModel = joblib.load(filePath)

def predictIrisFlowerClass(input):
  output = IrisModel.predict(input)
  return 'Iris ' + output[0]

def index (request):      
  return render(request, 'index.html')

def submitData(request):
  if request.method == 'POST':
    emailTo = request.POST.get('email')
    sepalLength = request.POST.get('sepal_length')
    sepalWidth = request.POST.get('sepal_width')
    petalLength = request.POST.get('petal_length')
    petalWidth = request.POST.get('petal_width')
    
    isAllFieldFilled = emailTo and sepalLength and sepalWidth and petalLength and petalWidth

    if isAllFieldFilled:
      results = predictIrisFlowerClass(np.array([[sepalLength, sepalWidth, petalLength, petalWidth]]))
      data = {
        'sepal_length': sepalLength,
        'sepal_width': sepalWidth,
        'petal_length': petalLength,
        'petal_width': petalWidth,
        'result': results,
        'image': 'images/' + results.split()[1] + '.jpg'
      }
      htmlMessage = render_to_string('emailTemplate.html', data)
      textMessage = strip_tags(htmlMessage)
      email = EmailMultiAlternatives(
          "Here's the prediction result",
          textMessage,
          'Iris Classification 📨 <' + settings.EMAIL_HOST_USER + '>',
          [emailTo]
      )
      email.attach_alternative(htmlMessage, 'text/html')
      
      irisData = IrisData(
          email=emailTo,
          sepal_length=sepalLength,
          sepal_width=sepalWidth,
          petal_length=petalLength,
          petal_width=petalWidth,
          prediction_result=results,
          date=timezone.now()
      )
      
      irisData.save()
      email.send()
      
      messages.success(request, 'Result: ' + results)
      
    else:
      messages.warning(request, 'Please fill all fields!')
  
  return HttpResponseRedirect(reverse('home'))
  # return render(request, 'emailTemplate.html', data)
