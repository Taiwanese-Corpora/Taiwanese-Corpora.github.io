from django.http import HttpResponse

from ArticutAPI_Taigi.ArticutAPI_Taigi import ArticutTG

username = "phonlab.nthu@gmail.com"
apikey = "IBUYB2Ro*nMe*HWuvmoZnBC+r5FjH3x"
articutTG = ArticutTG(username, apikey)

def home(request):
    text = request.GET['text']
    resultDICT = articutTG.parse(text)
    output = resultDICT['result_segmentation']
    return HttpResponse(output.replace("/", " "))
