from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

month_text = {
    "jan": "hello 1",
    "feb": "hello 2",
    "mar": "hello 3",
    "apr": None
}

# Create your views here.

def starting(request):
    lists = ""
    month_list = list(month_text.keys())

    lists = render(request, "challenges/list.html", {
        "months":month_list
    })
    return HttpResponse(lists)

    # for month in month_list:
    #     reverse_path = reverse("month-name", args=[month])
    #     lists += f"<li><a href=\"{reverse_path}\"> {month.capitalize()} </a> </li>"
    #
    # display_list = f"<ul> {lists} </ul>"
    # return HttpResponse(lists)

def index(request, month):
    month_list = list(month_text.keys())

    if month > len(month_list) or month < 1:
        return HttpResponseNotFound("Invalid month number!")

    redirect_month = month_list[month - 1]
    reverse_path = reverse("month-name", args=[redirect_month])

    return HttpResponseRedirect(reverse_path)


def strings(request, month):
    try:
        challenges_text = month_text[month]
        return render( request, "challenges/firstpage.html", {
            "name":month,
            "message": challenges_text
        })
    except:
        error_page = render(request, "404.html")
        return HttpResponseNotFound(error_page)