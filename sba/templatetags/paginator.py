from django import template

register = template.Library()

@register.inclusion_tag('sba/tags/paginator.html')
def paginator(model, query_params=None, adjacent_pages=3):
    start_page = max(model.number - adjacent_pages, 1)
    if start_page <= 2:
        start_page = 1

    end_page = min(model.number + adjacent_pages, model.paginator.num_pages)
    if end_page >= model.paginator.num_pages - 1:
        end_page = model.paginator.num_pages

    pages = range(start_page, end_page + 1)

    query_tokens = []
    for key, value in query_params.iteritems():
        if key != 'page':
            query_tokens.append('%s=%s' % (key, value))

    if query_tokens:
        querystring = '&' + '&'.join(query_tokens)
    else:
        querystring = ''

    return {
        'model': model,
        'pages': pages,
        'show_first': 1 not in pages,
        'show_last': model.paginator.num_pages not in pages,
        'last': model.paginator.num_pages,
        'querystring': querystring
    }
