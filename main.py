import http.client
import json
import requests

# URL 및 매개변수 설정
url = "/v1/usernames/validate?request.username=KKLUX&request.birthday=1337-04-20"

# 연결 설정
conn = http.client.HTTPSConnection("auth.roblox.com")

# 디스코드 웹훅 URL
webhook_url = "https://discord.com/api/webhooks/1193400866854686862/2Ffrz5tdnuEFuEsHbrcw52KFt2z_4DtS-kSKWvp4S2C1MwuFRBkim6keJub_mpFFOKAu"

while True:
    # 요청 보내기
    conn.request("GET", url)

    # 응답 받기
    res = conn.getresponse()
    data = res.read()

    # JSON 파싱
    json_data = json.loads(data)
    message = json_data.get("message")

    if message == "Username is valid":
        print("예아!")

        payload = {
            "content": "로블록스에서 닉네임 : KKLUX이 사용 가능합니다!. @everyone (이전에 KKLUX는 밴당함)"
        }
        response = requests.post(webhook_url, json=payload)

        payload = {
            "content": ">name KKLUX"
        }
        response = requests.post(webhook_url, json=payload)
        break  # 유효한 이름이 발견되면 루프를 종료합니다.
    else:
        print("닉네임이 사용 중입니다.")

# 연결 닫기
conn.close()
