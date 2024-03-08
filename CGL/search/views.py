from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

#from wagtail.contrib.search_promotions.models import Query

from wagtail.models import Page

from CGL.blog.models import ArticlePage
from CGL.certificate.models import CertificatesList, CertificatesPage

# To enable logging of search queries for use with the "Promoted search results" module
# <https://docs.wagtail.org/en/stable/reference/contrib/searchpromotions.html>
# uncomment the following line and the lines indicated in the search function
# (after adding wagtail.contrib.search_promotions to INSTALLED_APPS):

# from wagtail.contrib.search_promotions.models import Query

def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)
    # Search
    if search_query:
        
        search_results = Page.objects.live().search(search_query)
    else:
        
        blog_results = ArticlePage.objects.live().search(search_query)
        blog_page_ids = [p.page.ptr_id for p in blog_results]
        
        certificates_results = CertificatesList.live().search(search_query)
        certificates_page_ids = [p.page_ptr.id for p in certificates_results]
        
        page_ids = blog_page_ids + certificates_page_ids 
        search_results = Page.objects.live().filter(id__in=page_ids)
        
    #query = Query.get(search_query)
    
    # Record Hit
    #query.add_hit()
    
    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "includes/search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
