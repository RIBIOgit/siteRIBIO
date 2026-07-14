from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import ContactPage


def contact_list(request):

    q = request.GET.get("q")

    # Base completa
    all_contact = ContactPage.objects.all()

    # Lista filtrada
    contact = all_contact

    if q:
        contact = contact.filter(title__icontains=q)

    paginator = Paginator(contact, 12)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    others = page_obj.object_list if page_obj.object_list else []

    return render(request, "contact/list.html", {
        "contact": others,
        "page_obj": page_obj,
        "q": q,
        "latest_contact": all_contact[:5],
    })


def contact_detail(request, pk):

    item = get_object_or_404(ContactPage, pk=pk)

    # Item anterior
    previous_item = (
        ContactPage.objects
        .filter(pk__lt=item.pk)
        .order_by("-pk")
        .first()
    )

    # Próximo item
    next_item = (
        ContactPage.objects
        .filter(pk__gt=item.pk)
        .order_by("pk")
        .first()
    )

    return render(request, "contact/detail.html", {
        "item": item,
        "previous_item": previous_item,
        "next_item": next_item,
    })