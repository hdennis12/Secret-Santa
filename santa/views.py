from django.shortcuts import render
import random

def home(request):
    if request.method == "POST":
        participants = request.POST.getlist("participants")
        # Shuffle and assign Secret Santa pairs
        random.shuffle(participants)
        pairs = [(participants[i], participants[(i + 1) % len(participants)]) for i in range(len(participants))]
        return render(request, "santa/result.html", {"pairs": pairs})
    return render(request, "santa/home.html")