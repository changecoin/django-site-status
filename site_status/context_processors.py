from site_status import api

def inject_statuses(request):
    return {"statuses": api.get_statuses()}