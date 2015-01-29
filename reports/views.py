from django.shortcuts import render, Http404, HttpResponse, RequestContext, render_to_response
from .models import Report, Advice
from xhtml2pdf import pisa
import StringIO
from django.template.loader import render_to_string
from .forms import ReportFrom
from django.db.models import Count
import json
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from reportlab.pdfgen import canvas

gov = {
  "blabla":"tn-4431",
  "Sfax"      : "tn-sf",
  "Medenin"   : "tn-me",
  "Tozeur"    : "tn-to",
  "Manouba"   : "tn-mn",
  "Beja"      : "tn-bj",
  "Ben Arous" : "tn-ba",
  "Bizerte"   : "tn-bz",
  "Jendouba"  : "tn-je",
  "Nabeul"    : "tn-nb",
  "Tunis"     : "tn-tu",
  "Kef"       : "tn-kf",
  "Kasserine" : "tn-ks",
  "Gabes"     : "tn-gb",
  "Gafsa"     : "tn-gf",
  "Sidi Bouzid": "tn-sz",
  "Siliana"   : "tn-sl",
  "Mahdia"    : "tn-mh",
  "Monastir"  : "tn-ms",
  "Kairouan"  : "tn-kr",
  "Sousse"    : "tn-ss",
  "Zaghouane" : "tn-za",
  "Kebili"    : "tn-kb",
  "Tataouine" : "tn-ta",
  "Ariana"    : "tn-mn",
}


def index(request):
    reports = Report.objects.all()
    return render(request, 'reports/index.html', locals())


def add_report(request):
    if request.method == 'POST':
        form = ReportFrom(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return advise_me(request, request.POST['type'])
        else:
            print form.errors
    else:
        form = ReportFrom()
    return render(request, 'reports/addreport.html', locals())


def advise_me(request, t):
    advises = Advice.objects.all().filter(type=t)
    return render(request, 'reports/advise.html', locals())


def advises(request):
    advices = Advice.objects.all()
    types = advices.values_list('type')
    d = []
    for i in types:
        d.append([i[0], [j for j in advices.filter(type=i[0])]])
    return render(request, 'reports/advises.html', locals())


def gen_report(request):  # generate pdf
    pass


def get_report(request, i):
    try:
        report = Report.objects.get(id=i)
    except Report.DoesNotExist:
        raise Http404
    return render(request, 'reports/getreport.html', locals())


def aboutus(request):
    return render(request, 'reports/aboutus.html', {})


def mapped(d, w):
    w = str(w)
    dd = {}
    for i in d:
        dd[i[w]] = i[w+'__count']
    return dd


def getstats(request):
    return render(request, 'reports/stat.html', {})


def stats(request):
    nbr_reports = Report.objects.count()
    report_per_gov = Report.objects.values('gouvernorat').order_by()\
        .annotate(Count('gouvernorat'))
    report_per_type = Report.objects.values('type').order_by()\
        .annotate(Count('type'))
    report_per_status = Report.objects.values('status').order_by()\
        .annotate(Count('status'))
    report_per_gov = mapped(report_per_gov, 'gouvernorat')
    for i in report_per_gov.keys():
        report_per_gov[gov[i]] = report_per_gov.pop(i)
    report_per_status = map(list, mapped(report_per_status, 'status').items())
    report_per_gov = map(list, report_per_gov.items())
    report_per_type = map(list, mapped(report_per_type, 'type').items())
    return HttpResponse(json.dumps([nbr_reports,
                                    report_per_type,
                                    report_per_status,
                                    report_per_gov]),
                        content_type="application/json")




def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode(encoding='UTF-8')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def gen_pdf(request, i):
    try:
        report = Report.objects.get(id=i)
    except Report.DoesNotExist:
        raise Http404
    return render_to_pdf('reports/pdftemplate.html', locals())


def printall(request):
    reports = Report.objects.all().order_by('-id')
    return render_to_pdf('reports/pdftemplateall.html', locals())


def support(request, i):
    try:
        r = Report.objects.get(id=i)
    except Report.DoesNotExist:
        raise Http404
    r.votes += 1
    r.save()
    return get_report(request, i)


def nsupport(request, i):
    try:
        r = Report.objects.get(id=i)
    except Report.DoesNotExist:
        raise Http404
    r.votes -= 1
    r.save()
    return get_report(request, i)