import requests
from bs4 import BeautifulSoup # http://kondou.com/BS4/
import pdb # pdb.set_trace()

BASE_URL = "https://www.city.kita.tokyo.jp"
URL = f"{BASE_URL}/d-shisetu/kurashi/bus/bus.html"

def get_current_element() -> str:
    res  = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    # もっとよい書き方があるはず
    # 文字検索をしたい
    # pdb.set_trace()
    jikokuhyo_element = soup.find("a", id="E1").next_element.next_element.next_element.next_element
    return str(jikokuhyo_element)

def compare_element() -> bool:
    new_data = get_current_element()
    try:
        with open('tmp/old_data.txt', "r") as f:
            old_data = f.read()
            if old_data == new_data:
                print("Page is not updated")
                return False
            else:
                print("Page is updated!!")
                over_write_current_element(new_data)
                # ページの更新があったときに通知したい
                return True
    except:
        print("Except is occured")
        return False
        # エラーのときに通知したい

def over_write_current_element(new_data: str) -> bool:
    with open("tmp/old_data.txt", "w") as f:
        f.write(new_data)
        return True

# def read_old_data_txt():
#     with open("tmp/old_data.txt", "r") as f:
#         return f.read()

def download_target_file():
    # 保存しているファイルから正規表現で取り出せそう
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    pdf_file_link = soup.find("a", id="E1").next_element.next_element.next_element.next_element.find("a").get('href')
    get_pdf_res = requests.get(f"{BASE_URL}{pdf_file_link}")
    try:
        file = open("tmp/old_time_table.pdf", "wb")
        for chunk in get_pdf_res.iter_content(100000):
            file.write(chunk)
        file.close()
        print("Download completed")
    except:
        print("Except is occured")

if __name__ == "__main__": 
    if compare_element():
        download_target_file()
