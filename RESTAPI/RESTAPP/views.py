from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse,JsonResponse
# from django.core.serializers import serialize
from RESTAPP.mixins import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from RESTAPP.utils import is_json
from RESTAPP.forms import EmployeeForm



# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json'})
            return self.render_to_HttpResponse(json_data, status=404)
        p_data = json.loads(data)
        id = p_data.get('id',None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'This request resource with this is not available'})
                return self.render_to_HttpResponse(json_data, status=404)
            json_data= self.serialize([emp,])
            return self.render_to_HttpResponse(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_HttpResponse(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json'})
            return self.render_to_HttpResponse(json_data,status=404)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'resource created succesfully'})
            return self.render_to_HttpResponse(json_data)
        if form.errors():
            json_data = json.dumps(form.errors)
            return self.render_to_HttpResponse(json_data,status=404)

    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json'})
            return self.render_to_HttpResponse(json_data, status=404)
        p_data = json.loads(data)
        id = p_data.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'This request resource with this is not available'})
                return self.render_to_HttpResponse(json_data, status=404)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eadd': emp.eadd,
        }
        original_data.update(provided_data)
        print(original_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'resource updated succesfully'})
            return self.render_to_HttpResponse(json_data)
        if form.errors():
            json_data = json.dumps(form.errors)
            return self.render_to_HttpResponse(json_data, status=404)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json'})
            return self.render_to_HttpResponse(json_data, status=404)
        p_data = json.loads(data)
        id = p_data.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'This request resource with this is not available'})
                return self.render_to_HttpResponse(json_data, status=404)
            status, deleted_item = emp.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'resource deleted succesfully'})
                return self.render_to_HttpResponse(json_data)

            json_data = json.dumps({'msg': 'unable to delete....please try again!!'})
            return self.render_to_HttpResponse(json_data)
        json_data = json.dumps({'msg': 'To perform deletion ID is required'})
        return self.render_to_HttpResponse(json_data, status=404)


@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'This resource is unavailable'})
            return self.render_to_HttpResponse(json_data,status=404)
        else:
            json_data= self.serialize([emp,])
            return self.render_to_HttpResponse(json_data,status=404)

    def put(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No Matched Found'})
            return self.render_to_HttpResponse(json_data,status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json'})
            return self.render_to_HttpResponse(json_data, status=404)
        provided_data = json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eadd':emp.eadd,
        }
        original_data.update(provided_data)
        print(original_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'resource updated succesfully'})
            return self.render_to_HttpResponse(json_data)
        if form.errors():
            json_data = json.dumps(form.errors)
            return self.render_to_HttpResponse(json_data, status=404)



    def delete(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'No Matched Found Not able to perform deletion'})
            return self.render_to_HttpResponse(json_data, status=404)
        status,deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'resource deleted succesfully'})
            return self.render_to_HttpResponse(json_data)

        json_data = json.dumps({'msg': 'unable to delete please try again!!'})
        return self.render_to_HttpResponse(json_data)

# No validation
# class EmployeeDetailCBV(SerializeMixin,View):
#     def get(self,request,id,*args,**kwargs):
#         emp = Employee.objects.get(id=id)
#         json_data= self.serialize([emp,])
#         return HttpResponse(json_data,content_type='application/json')


class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')


@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        try:
            qs = Employee.objects.all()
        except Employee.DoesNotExist:
            return json.dumps({'msg':'Employee not available'})
        else:
            json_data = self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')


    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json'})
            return self.render_to_HttpResponse(json_data,status=404)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'resource created succesfully'})
            return self.render_to_HttpResponse(json_data)
        if form.errors():
            json_data = json.dumps(form.errors)
            return self.render_to_HttpResponse(json_data,status=404)













