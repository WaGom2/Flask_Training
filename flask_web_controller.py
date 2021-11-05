from flask import Flask, render_template, request  #from의 flask와 import의 Flask는 다른거에요
app= Flask(__name__) #name 앞뒤에 _두개 입니다. 주의하시고요.
#####################
#htto://localhost/m_serch/ --->> 대응컨트롤러(search_member_con)
#http://localhost/m_del/ --->(del_member_con)

@app.route('/') #methods는 여기서는 안적어도 문제 없데요
def homepage_controller()-> 'html': #이름 달라야 합니다. def 정의하다 라는 뜻입니다.
    print("from m_reg.html")
    return render_template('m_reg.html')
#http://localhost/m_reg/ 라고 접속하면 이곳을 처리하게됨
@app.route('/m_reg/', methods=['POST']) # post로 전송된것을 받음
def add_member_controller()-> 'html': #오타조심 
    inputid= request.form['m_name']
    inputpad= request.form['m_addr']
    inputtel= request.form['m_tel']
    print("from m_reg.html")  #cmd 창에 결과가 찍힘
    return render_template("return.html") # 브라우저에 결과가 찍힘
#########################
app.run(debug=True) # app.run 은 실제로 이 앱을 작동시킨다는 말이다.
                    # 만약 app.run의 명령어가 없으면 위에 코드가 맞아도 실행되지 않습니다.
                    # 수정할 수 있는 부분은 True 부분입니다. False 라고 하면 메세지가 뜬다고? 대소문자 구분 조심하세요

# line 7의 값이 /니깐 브라우저에 localhost:5000을 입력하면
# 정의된 함수가 실행되니다.  함수가 문제 없다면 return 값처럼 m_reg.html 으로 가겠지! render_template가 그 브라우저로 이동하라는 말인듯
# m_reg.html 브라우저가 실행되면 정보를 입력하고 send를 누르면 /m_reg/ 여기로 가라고 명령했자나
# 그래서 m_reg.html 에서 /m_reg/로 넘어와서 자연스럽게 두번째 컨트롤러가 실행되는 거지 여기는 m_reg.html 에서 들어온 post 값으로 하려는 일을해
# 함수가 문제 없으면 다시 리턴값 그래서 결국 return.html로 이동하게 되는거