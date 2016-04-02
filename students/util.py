from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(objects, size, request, context, var_name='object_list'):
    """
    Paginate objects provided by view.

    :param objects: list of elements;
    :param size: number of objects per page;
    :param request: request object to get url parameters from;
    :param context: context to set new variables into;
    :param var_name: variable name for list of objects.

    :return updated context object
    """

    # apply pagination
    paginator = Paginator(objects, size)

    # try to get page number from request
    page = request.GET.get('page', '1')
    try:
        object_list = paginator.page(page)
    except EmptyPage:
        # if page is out of range
        # deliver last page of results
        object_list = paginator.page(paginator.num_pages)

    # set variables into context

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context
