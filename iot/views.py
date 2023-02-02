from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SecFile
from django.views import generic

# request.method가 POST로 오면 파일 저장
# 성공시 success 출력, 실패시 fail 출력
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        file_name = request.POST['file_name']
        sec_file =  request.FILES['sec_file']
        model = SecFile(file_name = file_name, sec_file = sec_file)
        model.save()
        
        print('upload_file', file_name, sec_file)
        msg = { 'result' : 'success'}
    
    else:
        msg = { 'result' : 'fail'}
    
    return JsonResponse(msg)

# 저장된 파일 리스트 확인하는 클래스
class SecFileListView(generic.ListView):
    model = SecFile
    template_name = 'iot/sec_file_list.html'
    context_object_name = 'sec_files'


# 저장된 파일 열어보기
class SecFileDetailView(generic.DetailView):
    model = SecFile
    template_name = 'iot/sec_file_detail.html'
    context_object_name = 'imgfile'



