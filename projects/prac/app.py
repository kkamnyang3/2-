# 아래 2줄은 항상 제일 위에 위치
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# 가운데 부분이 내가 서버 코드를 작성할 곳
@app.route('/') # "/" > URL 주소의 나머지 부분
def home(): #home이라는 함수 이름은 하나만 존재해야 한다
    # 요청이 들어왔을 때 처리하는 코드
    print('요청이 들어왔습니다!')
    return render_template('index.html') # Return 다음 부분이 내가 응답을 줄 내용

   # render_template 이 하는일. {{}}을 찾아서 값을 넣어줌
    

@app.route('/json') 
def test_json(): 
    sample = {'result' : 'sample'}
    return jsonify(sample) # Sample 딕셔너리를 json으로 변환해 리턴


@app.route('/test', methods=['GET']) 
def test_get(): #home이라는 함수 이름은 하나만 존재해야 한다
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result':'success','msg':'이 요청은 GET!'})


@app.route('/test', methods=['POST'])
def test_post():
    # request.form에는 ajax data 정보가 담겨있음
    # request.form 역시 딕셔너리
    # POST 메소드 - request.form - ajax data 세트로 작업함
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify ({'result':'success','msg' : '이 요청은 POST!'})




# 아래 2줄은 항상 제일 아래에 위치   
if __name__ == '__main__':  
   # 0.0.0.0 > 모든 IP에게 오는 요청을 받아주겠음
   # port=5000 > 5000번 포트에 서버를 등록해서 요청을 받아주겠음
   # debug=True > 무언가 에러가 났을 때 에러 메시지를 그대로 보여줌
    app.run('0.0.0.0', port=5000, debug=True)

    