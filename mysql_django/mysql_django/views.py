from django.shortcuts import render
from login.models import Employee, Employeeforms, Member, Memberform
from django.db.models import Q
from .forms import SearchForm
from django.core.paginator import Paginator

def employee_create(request):
    if request.method == 'POST':
        form_1 = Employeeforms(request.POST)
        if form_1.is_valid():
            form_1.save()
    else:
        form_1 = Employeeforms()
    return render(request, 'index.html', {'form':form_1})

def employee_read(request):
    data = Employee.objects.all()
    return render(request, 'read.html', {'data':data})

def employee_seach(request):
    if request.method == 'POST':
        kw = request.POST.get('name', '')
        form = SearchForm(request.POST, initial={'name': kw})
    else:
        kw = request.GET.get('name','')
        form = SearchForm(initial={'name': kw})
    data = Employee.objects.filter(Q(fistname__contains=kw)| Q(lastname__contains=kw))[:10]
    return render(request, 'SearchForm.html', {'form':form, 'data':data})

def employee_edit(request):
    data = Employee.objects.all()
    return render(request, 'edit.html', {'data':data})

#เฉพาะฟังก์ชั่นที่เกี่ยวข้องกับพาธ emloyee/updata/<int:id>/
def employee_updata(request, id):
    if request.method == 'POST':
        row = Employee.objects.get(id=id) #อ่านข้อมูลเดิม

        #กำหนดข้อมูลเดิมให้กับโมเดลฟอร์ม เพื่อเปรียเทียบกับข้อมูลใหม่ที่รับเข้ามา
        form = Employeeforms(instance=row, data=request.POST)

        if form.is_valid():
            form.save()
    else:
        row = Employee.objects.get(id=id)
        form = Employeeforms(initial=row.__dict__)
    return render(request, 'updata.html', {'form': form})

def employee_delete(request, id):
    Employee.objects.get(id=id).delete()

    data = Employee.objects.filter()[:10]
    return render(request, 'edit.html', {'data':data})

def employee_login(request):
    if request.method == 'POST':
        confirm_pswd = request.POST.get('confrim_pswd', '')
        save = request.POST.get('save', False)
        #...นำค่าไปใช้ตามที่ต้องการ
        form = Memberform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Memberform()
    return render(request, 'login.html', {'form':form})

def pagination_pvnx(request, pg):
    if pg == None:
        pg = 1
    
    rows = Employee.objects.all().order_by('id')
    pgn = Paginator(rows, 2)
    page = pgn.get_page(pg)
    return render (request, 'pagination_pvnx.html', {'page':page})

def pagination_number(request, pg):
    if pg == None:
        pg = 1
    
    rows = Employee.objects.all().order_by('id')
    pgn = Paginator(rows, 2)
    page = pgn.get_page(pg)
    return render (request, 'pagination_num.html', {'page':page})

