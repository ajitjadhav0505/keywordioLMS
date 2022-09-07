from django.shortcuts import render
import mysql.connector as sql

em = ''
pwd = ''


# Create your views here.
def loginaction(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="9545295812", database='library')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "EmailAddress":
                em = value
            if key == "Password":
                pwd = value

        c = "select * from user where EmailAddress='{}' and Password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())

        if t == ('ajitjadhav0213@gmail.com','Ajit@9922'):
            return render(request, 'adminpage.html')

        elif t==():
            return render(request, 'errorpage.html')

        else:
            return render(request, "studentpage.html")

    return render(request, 'loginPage.html')