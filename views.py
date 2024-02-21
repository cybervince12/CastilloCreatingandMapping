from django.shortcuts import render
from django.http import HttpResponse

def mission_view(request):
    mission = "The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence."
    return HttpResponse(mission)

def vision_view(request):
    vission = "The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education."
    return HttpResponse(vission)

def objective_view(request):
    objective = "At the College of Computing and Multimedia Studies, we are driven by a steadfast commitment to excellence in every aspect of our work. Our quality objectives serve as the guiding principles that propel us toward continuous improvement and the delivery of exceptional educational experiences."
    return HttpResponse(objective)