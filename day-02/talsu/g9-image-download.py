import requests, re

# VIP 이미지 다운로드
def downloadVipImage(goodsno):
    print('download ' + goodsno + ' ...')
    # 이미지 Request
    imgRes = requests.get('http://image.g9.co.kr/g/' + goodsno + '/n')
    # 파일을 열고 기록 한다.
    f = open(goodsno + '.jpg', 'wb')
    f.write(imgRes.content)
    f.close()

# G9 메인 페이지요청
res = requests.get('http://www.g9.co.kr');

# 정규 표현식으로 상품번호를 추출한다
regex = re.compile('\/Display\/VIP\/Index\/(\d+)')
matches = regex.findall(res.text)

# 상품번호를 순회 하며
for match in list(set(matches)):
    # VIP 이미지 다운로드 함수 호출
    downloadVipImage(match)
