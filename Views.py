from django.shortcuts import render

# Create your views here.
def volumecalculation(request):
    context={}
    context['volume'] = "0"
    context['l'] = "0"
    context['b'] = "0"
    context['w'] = "0"
    if request.method == 'POST':
        l = request.POST.get('length','0')
        b = request.POST.get('breadth','0')
        w = request.POST.get('width','0')
        volume = int(l) * int(b) * int(w)
        context['volume'] = volume
        context['l'] = l
        context['b'] = b
        context['w'] = w
    return render(request,'mathapp/volume.html',context)