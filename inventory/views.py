from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Products

class InventoryView(APIView):
    def get(self, request):
        try:
            data = []
            id = request.GET.get('product_id')
            if id:
                product_info_obj = Products.objects.get(product_id=id)

                data.append({
                        'product_id': product_info_obj.product_id,
                        'product_name': product_info_obj.product_name,
                        'vendor': product_info_obj.vendor,
                        'mrp': product_info_obj.mrp,
                        'batch_no': product_info_obj.batch_no,
                        'batch_date': product_info_obj.batch_date,
                        'quantity': product_info_obj.quantity,
                        'status': product_info_obj.status
                    })

            else:

                product_info_obj = Products.objects.all()

                for info in product_info_obj:
                    data.append({
                        'product_id': info.product_id,
                        'product_name': info.product_name,
                        'vendor': info.vendor,
                        'mrp': info.mrp,
                        'batch_no': info.batch_no,
                        'batch_date':info.batch_date,
                        'quantity': info.quantity,
                        'status': info.status
                    })
            return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable to retreive data"
            }
            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='appliaction/json', status=500)

    def post(self, request):
        try:

            # product_id = request.data.get('product_id')
            product_name = request.data.get('product_name')
            vendor = request.data.get('vendor')
            mrp = request.data.get('mrp')
            batch_no = request.data.get('batch_no')
            batch_date = request.data.get('batch_date')
            quantity = request.data.get('quantity')
            status = request.data.get('status')

            product_info_obj = Products(product_name=product_name, vendor=vendor, mrp=mrp,
                                        batch_no=batch_no, batch_date=batch_date, quantity=quantity, status=status)

            product_info_obj.save()

            success = {
                "msg": "Product has been successfully added.",
            }

            return HttpResponse(json.dumps(success, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable to add the product."
            }
            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)


    def put(self, request):
        try:
            p_id = request.data.get('product_id')
            p_name = request.data.get('product_name')
            p_vendor = request.data.get('vendor')
            p_mrp = request.data.get('mrp')
            p_batch_no = request.data.get('batch_no')
            p_batch_date = request.data.get('batch_date')
            p_quantity = request.data.get('quantity')
            p_status = request.data.get('status')

            if p_id is not None and p_id is not '':
                product_info_obj = Products.objects.get(product_id=p_id)
                product_info_obj.product_name = p_name
                product_info_obj.vendor = p_vendor
                product_info_obj.mrp = p_mrp
                product_info_obj.batch_no = p_batch_no
                product_info_obj.batch_date = p_batch_date
                product_info_obj.quantity = p_quantity
                product_info_obj.status = p_status

                product_info_obj.save()
                success = {
                    "msg": "Product has been updated successfully."
                }

                return HttpResponse(json.dumps(success, cls=DjangoJSONEncoder), content_type='application/json',
                                    status=200)

        except:
            error = {
                "msg": "Unable to update the product."
            }
            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

    def delete(self, request):
        try:
            product_id = request.GET.get('product_id')

            del_product = Products(product_id=product_id)
            del_product.delete()

            success = {
                "msg": "Product has been deleted successfully."
            }
            return HttpResponse(json.dumps(success, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:
            error = {
                "msg": "Unable to delete the product."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)