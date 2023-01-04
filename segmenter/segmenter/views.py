from ArticutAPI_Taigi.ArticutAPI_Taigi import ArticutTG
username = ""
apikey = ""
articutTG = ArticutTG(username, apikey)

# Call with ../ArticutAPI_Taigi.ArticutAPI_Taigi(username, apikey).parse(text)
# then output "result_segmentation" separated by space " ".

from django.http import HttpResponse
def home(request):
    text = request.GET["text"]
    resultDICT = articutTG.parse(text)
    output = resultDICT["result_segmentation]
    return HttpResponse(output.replace("/", " ")
