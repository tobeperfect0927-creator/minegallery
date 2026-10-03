from pathlib import Path
import base64, re, zipfile
import os
repo=Path(__file__).resolve().parents[1]
os.chdir(repo)
Path('releases').mkdir(exist_ok=True)
root=Path('consumer-web/dist')
css=(root/'style.css').read_text(encoding='utf-8')
css=re.sub(r"@import url\([^;]+;\s*",'',css,count=1)
css=css.replace("'Noto Sans KR',sans-serif","'Malgun Gothic','Apple SD Gothic Neo',sans-serif")
js=(root/'app.js').read_text(encoding='utf-8')
sources={'pottery.jpg':'https://images.pexels.com/photos/6694323/pexels-photo-6694323.jpeg?auto=compress&w=1000','baking.jpg':'https://images.pexels.com/photos/6996298/pexels-photo-6996298.jpeg?auto=compress&w=1000','lake.jpg':'https://images.pexels.com/photos/33495169/pexels-photo-33495169/free-photo-of-tranquil-canoe-on-a-misty-lake-edge.jpeg?auto=compress&w=1000'}
for name,url in sources.items():
    raw=(root/'assets'/name).read_bytes()
    assert raw[:2]==b'\xff\xd8',name
    js=js.replace(url,'data:image/jpeg;base64,'+base64.b64encode(raw).decode())
js=js.replace('외부 사진과 글꼴을 불러오는 과정에서 해당 제공자에게 일반적인 접속 정보가 전달될 수 있습니다.','사진은 이 파일 안에 포함되어 있으며 외부 글꼴을 불러오지 않습니다. 출처 링크는 인터넷 연결 시에만 열 수 있습니다.')
html=(root/'index.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="style.css">','<style>'+css+'</style>').replace('<script src="app.js"></script>','<script>'+js+'</script>')
out=Path('releases/마인갤러리-소비자웹-오프라인.html')
out.write_text(html,encoding='utf-8')
readme='''마인갤러리 소비자 웹 · 오프라인 시제품

1. ZIP 압축을 풀어 주세요.
2. 마인갤러리-소비자웹-오프라인.html 파일을 Chrome 또는 Edge로 열어 주세요.
3. 인터넷 연결이나 설치 없이 사진과 체험 탐색, 예시 예약·취소를 사용할 수 있습니다.

HTML 한 파일에 화면, 사진, 기능이 모두 포함되어 있습니다.
HTML 파일만 다른 컴퓨터로 복사해도 사용할 수 있습니다.

체험·업체·가격·일정은 예시이며 실제 결제·예약·업체 지급은 발생하지 않습니다.
실제 계정이나 결제정보를 입력하지 마세요.
예시 예약은 파일을 새로고침하거나 닫으면 초기화됩니다.
사진 출처 링크를 방문할 때만 인터넷 연결이 필요합니다.

휴대폰·카카오톡의 첨부파일 미리보기에서는 HTML 실행이 제한될 수 있습니다.
컴퓨터 브라우저에서 이용하는 배포본입니다. 앱 설치파일이 아닙니다.
'''
Path('releases/오프라인-사용안내.txt').write_text(readme,encoding='utf-8-sig')
with zipfile.ZipFile('releases/마인갤러리-소비자웹-오프라인.zip','w',zipfile.ZIP_DEFLATED) as z:
    z.write(out,out.name)
    z.writestr('사용안내.txt',readme.encode('utf-8-sig'))
assert '<script src=' not in html and '@import' not in html and '<link rel="stylesheet"' not in html
assert js.count('data:image/jpeg;base64,')==3
print('Created standalone offline HTML and ZIP.')
