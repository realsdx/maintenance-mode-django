from maintenance import models

class MaintenanceMiddleware():
    def process_request(self,request):
        try:
            status = models.MainteneceMode.objects.get(pk=1)
        except Exception:
            return None
        
        if request.user.is_staff:
            return None
        else:
            return 