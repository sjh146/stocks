from flask import Flask, request, jsonify, abort
import socket
import json

host="localhost"#챗봇 엔진 서버 IP 주소
port= 11434 #챗봇 엔진 서버 통신 포트
#Flask 애플리케이션

app=Flask(__name__)

#챗봇 엔진 서버와 통신
def get_answer_from_engine(bottype,query):
    # 챗봇 엔진 서버 연결
    mySocket=socket.socket
    mySocket.connect((host,port))

    # 챗봇 엔진 질의 요청
    json_data={
        'Query': query,
        'BotType': bottype
    }
    message=json.dumps(json_data)
    mySocket.send(message.encode())

    #챗봇 엔진 답변 출력
    data= mySocket.recv(2048).decode()
    ret_data=json.loads(data)

    #챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data
#챗봇 엔진 query 전송 API
@app.route('/query/<bot_type>',methods=['POST'])
def query(bot_type):
    body=request.get_json()
    try:
        if bot_type=='TEST':
            #챗봇 API 테스트
            ret =get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret)
        elif bot_type=="KAKAO":
            #카카오톡 처리(10장에서 구현)
            pass
        elif bot_type =="NAVER":
            #네이버토곡 처리
            pass
        else:
            #정의되지 않은 bot type인 경우 404오류
            abort(404)
    except Exception as ex:
        #오류 발생 시 500 오류
        abort(500)
if __name__=='__main__':
    app.run()