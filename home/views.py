from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def index(request):
    # Page from the theme 
    line_list = ['S1','S3']
    eqp_list = ['WSPDC1', 'WSPDC2']
    return render(request, 'pages/index.html',{'line_list' : line_list})

def bc_typography(request):
    return render(request, 'pages/bc_typography.html')

def get_eqplist(request):
    selected_value = request.GET.get('selected_value')
    
    # 여기에서 선택된 값에 따라 다른 옵션을 반환하는 로직을 추가할 수 있습니다.
    if selected_value == 'S1':
        options = ['WSPDC1','WSPDC2','WSPDC3']
    elif selected_value == 'S3':
        options = ['WUARB01','WUARB02']
    
    return JsonResponse({'options': options})

def get_ppid(request):
    line = request.GET.get('line')
    eqp_id = request.GET.get('eqp_id')
    print(line, eqp_id)
    # 여기에서 선택된 값에 따라 다른 옵션을 반환하는 로직을 추가할 수 있습니다.
    options = ['PWTEST','PWTEST2']
    print(options)
    return JsonResponse({'options': options})


def process_data(request):
    if request.method == 'POST':
        eqp_id = request.POST.get('select-eqp')
        ppid = request.POST.get('select-ppid')

        try:    # 여기에서 입력 필드에 대한 유효성 검사 또는 처리를 수행합니다.
            if eqp_id and ppid:
                print(eqp_id , ppid)
                # 입력 필드가 모두 채워져 있다면 처리를 계속합니다.
                # 이 부분에서 추가적인 로직을 구현합니다.
                return JsonResponse({'options': eqp_id})

        except Exception as e:
            return JsonResponse({'error': str(e)})