from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from demo1.models import User


def index(request):
    print(1111)
    return HttpResponse('吔屎啦')

def temp(request):
    return render(request,'qqq.html')


'''
动态界面
'''
def dynamic(request):
    list=[1,2,3,4,5]
    msg='动态界面'
    # context 字典对象
    context={'list':list,'msg':msg}
    return  render(request,'li.html',context=context    #SELECT * FROM Users    return  render(request,'user.html',{'users':})users
)

# 结合数据库动态获取数据(mysql)

def test_db(request):
    users=User.objects.all()
