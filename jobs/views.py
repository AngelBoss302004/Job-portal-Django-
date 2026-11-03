from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads



# Create your views here.

job_list = []
job_id = 1

@method_decorator(csrf_exempt, name='dispatch')
class AddJobView(View):

    def post(self, request):

        global job_id

        request_body = request.body
        form_data = loads(request_body)

        job = {
            "id": job_id,
            "company_name": form_data.get("company_name"),
            "job_title": form_data.get("job_title"),
            "location": form_data.get("location"),
            "salary": form_data.get("salary"),
            "job_type": form_data.get("job_type"),
            "experience": form_data.get("experience")
        }

        job_list.append(job)
        job_id += 1

        data = {
            "message": "Job added successfully"
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class GetAllJobsView(View):

    def post(self, request):

        data = {
            "jobs": job_list
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class GetOneJobView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        id = form_data.get("id")

        for job in job_list:

            if job["id"] == id:

                data = {
                    "job": job
                }

                return JsonResponse(data)

        data = {
            "message": "Job not found"
        }

        return JsonResponse(data, status=404)
@method_decorator(csrf_exempt, name='dispatch')
class UpdateJobView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        id = form_data.get("id")

        for job in job_list:

            if job["id"] == id:

                job["company_name"] = form_data.get(
                    "company_name", job["company_name"]
                )

                job["job_title"] = form_data.get(
                    "job_title", job["job_title"]
                )

                job["location"] = form_data.get(
                    "location", job["location"]
                )

                job["salary"] = form_data.get(
                    "salary", job["salary"]
                )

                job["job_type"] = form_data.get(
                    "job_type", job["job_type"]
                )

                job["experience"] = form_data.get(
                    "experience", job["experience"]
                )

                data = {
                    "message": "Job updated successfully"
                }

                return JsonResponse(data)

        data = {
            "message": "Job not found"
        }

        return JsonResponse(data, status=404)
@method_decorator(csrf_exempt, name='dispatch')
class DeleteJobView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        id = form_data.get("id")

        for job in job_list:

            if job["id"] == id:

                job_list.remove(job)

                data = {
                    "message": "Job deleted successfully"
                }

                return JsonResponse(data)

        data = {
            "message": "Job not found"
        }

        return JsonResponse(data, status=404)