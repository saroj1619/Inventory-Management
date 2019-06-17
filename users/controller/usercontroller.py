from django.shortcuts import render
from rest_framework.views import APIView
from ..models import *
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class UsersDetails(APIView):

    def get(self, request):
        try:

            user_id = request.user.id

            user_obj = Users.objects.get(id=user_id)

            role_obj = User_role.objects.filter(user=user_obj)

            # get role_type and and multiple roles

            data = []

            for role in role_obj:
                data.append({
                    'id': user_id,
                    'role_type': role.role.name,
                    'multi_role_status': role.multiple_role
                })

            return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable to retrieve users."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

    def post(self,request):
        try:

            user_id = request.user.id

            user_obj = Users.objects.get(id=user_id)

            user_request = User_request(user=user_obj)

            user_request.save()

            data = {
                "msg": "request send successfully"
            }

            return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable to send request for admin access."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

class RequestDetails(APIView):

    def get(self,request):
        try:

            request_obj = User_request.objects.filter(status=False)

            data = []

            for obj in request_obj:
                data.append({
                    'request_id': obj.id,
                    'user': obj.user.username,
                    'status': obj.status,
                    'email': obj.user.email,
                    'id': obj.user.id
                })

            return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable to retrieve users."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

    def post(self, request):
        try:
            user = request.data.get('id')
            request_id = request.data.get('request_id')
            role_SM = Roles.objects.get(name='Store Manager')

            multiple_role=True

            # udpate multiple role status for exiting entry
            update_ur_obj = User_role.objects.get(user=user)
            update_ur_obj.multiple_role = multiple_role
            update_ur_obj.save()

            # enter new role for existing user

            user_role_obj = User_role(user_id=user, role=role_SM, multiple_role=multiple_role)

            user_role_obj.save()

            update_request_obj = User_request.objects.get(id=request_id)

            update_request_obj.status=True

            update_request_obj.save()

            success = {
                "msg": "Admin access has been provided to the user.",
            }

            return HttpResponse(json.dumps(success, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable tp give admin access."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)
