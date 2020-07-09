from django.core.serializers import serialize
import json
class SerializeMixin(object):
    def serialize(self,qs):
        json_data = serialize('json',qs,fields=('ename','esal'))
        p_data = json.loads(json_data)
        emp_list = []
        for obj in p_data:
            emp_data = obj['fields']
            emp_list.append(emp_data)
        json_data = json.dumps(emp_list)
        return json_data


from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_HttpResponse(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)
