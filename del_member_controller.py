#http://localhost/m_del/ ---> 대응 컨트롤러 만들기(del_member_con)
#접속되면 "del page"라는 글자를 보여준다.
from flask import Flask, render_template, request  #from의 flask와 import의 Flask는 다른거에요
app= Flask(__name__)

@app.route('/m_del/') #methods는 여기서는 안적어도 문제 없데요
def del_member_controller()-> 'html': #이름 달라야 합니다. def 정의하다 라는 뜻입니다.
    print("from m_reg.html")
    return "del page"

app.run(debug=True)