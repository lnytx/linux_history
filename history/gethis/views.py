from django.http.response import HttpResponse
from django.shortcuts import render

from connect_database.connect_mysql import update_sql, select_table

def index(request):
    return render(request, 'home.html')

# Create your views here.
def home(request):
    if request.method == 'GET':
        if  not request.GET.get('history_id'):
            return HttpResponse("history_id null")
        if not request.GET.get('history_ip', ''):
            return HttpResponse("history_ip null")
        if not request.GET.get('history_user', ''):
            return HttpResponse("history_user null")
        if not request.GET.get('history_datetime', ''):
            return HttpResponse("history_datetime null")
        if not request.GET.get('history_command', ''):
            return HttpResponse("history_command null")
        history_id=request.GET.get('history_id', 'id')
        history_ip=request.GET.get('history_ip', 'ip')
        history_user=request.GET.get('history_user', 'user')
        history_datetime=request.GET.get('history_datetime', 'time')
        history_command=request.GET.get('history_command', 'command')
        list=[]
        #print("输出信息",history_id,history_ip,history_user,history_datetime,history_command)
        list.append(history_id)
        list.append(history_ip)
        list.append(history_user)
        list.append(history_datetime)
        list.append(history_command)
        print("list",list)
        update_sql(list)
        return render(request, 'home.html', {'list': list})
    else:
        return HttpResponse("非法提交！")
    
"""
=事件任务前端加载方法
"""
def get_result(request):
    ServerHistory_string=''
    lastid=""
    i=0
    for e in select_table():
        print("lastid",type(e),e)
        #list_str=e.split(',')
        list_str=e[0]
        ServerHistory_string+="<font color=#cccccc>"+e[1]+ \
        "</font>&nbsp;&nbsp;\t"+ e[3]+"&nbsp;&nbsp;\t"+str(e[4])+"\t # <font color=#fff000>"+e[5]+"</font></br>"
        i+=1
    print("str",ServerHistory_string)
    #ServerHistory_string+="@@"+str(i)+'</br>'
    return HttpResponse(ServerHistory_string)