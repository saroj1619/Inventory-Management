from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class UsersView(APIView):

    def get(self, request):
        try:
            data = []

            role_SA = Roles.objects.get(name='Store Assistant')

            obj = User_role.objects.filter(multiple_role=False, role=role_SA)

            for info in obj:

                data.append({
                    "name": info.user.username,
                    "id": info.user.id
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
            role_SM = Roles.objects.get(name='Store Manager')

            multiple_role=True

            # udpate multiple role status for exiting entry
            update_ur_obj = User_role.objects.get(user=user)
            update_ur_obj.multiple_role = multiple_role
            update_ur_obj.save()

            # enter new role for existing user

            user_role_obj = User_role(user_id=user, role=role_SM, multiple_role=multiple_role)

            user_role_obj.save()



            success = {
                "msg": "Admin access has been provided to the user.",
            }

            return HttpResponse(json.dumps(success, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable to provide access to the user."
            }
            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

    def put(self, request):
        pass

    def delete(self, request):
        pass