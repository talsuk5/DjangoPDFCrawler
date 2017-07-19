from django.http import HttpResponse
from myapp.pdf_parser import PdfParser
from myapp.url_filter import UrlFilter
from myapp.sql_adapter import SqlAdapter
import simplejson


# Create your views here.
def documents(request):
    with SqlAdapter() as sql_adapter:
        query_resp = sql_adapter.getAllDocuments()

    retval = []
    if len(query_resp) > 0:
        for resp in query_resp:
            retval.append({resp[0]: resp[1]})

    retval = {"documents:": retval}
    return HttpResponse(simplejson.dumps(retval))


def document(request):
    name = request.GET.get('name', '')
    with SqlAdapter() as sql_adapter:
        retval = sql_adapter.getUrlsForName(name)

    if len(retval) > 0:
        retval = [i[0] for i in retval]

    retval = {"urls:": retval}
    return HttpResponse(simplejson.dumps(retval))


def urls(request):
    with SqlAdapter() as sql_adapter:
        query_resp = sql_adapter.getNumUrlsForName()

    retval = []
    if len(query_resp) > 0:
        for resp in query_resp:
            retval.append({resp[0]: resp[1]})

    retval = {"urls:": retval}
    return HttpResponse(simplejson.dumps(retval))


def upload_file(request):
    name = request.GET.get('name')
    if request.method == 'POST' and name:
        pdf_parser = PdfParser(request.body)
        url_filter = UrlFilter()

        filtered_urls = url_filter.filter(pdf_parser.getParesdWordList())

        with SqlAdapter() as sql_adapter:
            sql_adapter.saveUrls(filtered_urls, name)

        http_resp = HttpResponse("File uploaded successfully")
    else:
        http_resp = HttpResponse("Please provide name parameter and a file")

    return http_resp
