
def students_proc(request):
    url = request.scheme + '://' + request.get_host()
    return {'PORTAL_URL': url}