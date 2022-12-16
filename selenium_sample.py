from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # webdriver_manager 모듈 설치(pip3 install webdriver-manager)

options = Options()
options.add_experimental_option("detach", True) # 자동 꺼짐 방지
options.add_argument("--mute-audio") # 음소거
options.add_argument("disable-gpu") # 그래픽 카드 기능 제거
options.add_argument("User-Agent: Mozilla/5.0 \(Macintosh; Intel Mac OS X 10_15_7\) AppleWebKit/537.36 \(KHTML, like Gecko\) Chrome/108.0.0.0 Safari/5") # User-Agent 헤더 지정
options.add_argument("lang=ko_KR") # 언어 지정
options.add_argument("--no-sandbox") # 오류 나면 해볼 수 있는 옵션
options.add_argument("--disable=dev-shm-usage") # 오류 나면 해볼 수 있는 옵션

service = Service(executable_path=ChromeDriverManager().install()) # chrome driver 최신 유지

browser = webdriver.Chrome(options=options, service=service)

browser.get("https://www.google.com")
