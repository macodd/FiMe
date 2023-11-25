from django.http import JsonResponse

from patient.models import Patient


class JsonResponseMixin:
    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.accepts("text/html"):
            return response
        else:
            data = {}
            search_data: str = form.cleaned_data.get("search")
            if search_data.isdigit():
                patient_id = int(search_data)
                patient_qs = Patient.objects.filter(id=patient_id)
                if patient_qs.exists():
                    data = {"patients", patient_qs}
            else:
                search_values = search_data.split(",")
                if len(search_values) == 1:
                    last_name = search_values[0].title()
                    patient_qs = Patient.objects.filter(last_name__startswith=last_name)
                    if patient_qs.exists():
                        data = {"patients": patient_qs}
                elif len(search_values) == 2:
                    patient_qs = Patient.objects.filter(
                        first_name__startswith=search_values[1].title(),
                        last_name__startswith=search_values[0].title(),
                    )
                    if patient_qs.exists():
                        data = {"patients": patient_qs}
            return JsonResponse(data)
