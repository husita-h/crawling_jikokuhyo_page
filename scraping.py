from xmlrpc.client import boolean
import requests
from bs4 import BeautifulSoup # http://kondou.com/BS4/
import pdb # pdb.set_trace()

URL = 'https://www.city.kita.tokyo.jp/d-shisetu/kurashi/bus/bus.html'

def get_current_element() -> str:
    res  = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    # もっとよい書き方があるはず
    # 文字検索をしたい
    jikokuhyo_element = soup.find("a", id="E1").next_element.next_element.next_element.next_element
    return str(jikokuhyo_element)

def compare_element() -> bool:
    new_element = get_current_element()
    try:
        with open('tmp/old_element.txt', "r") as f:
            old_data = f.read()
            if old_data == new_element:
                print("page is not updated")
                return False
            else:
                print("page is updated!!")
                over_write_current_element(new_element)
                return True
    except:
        print("except is occured")
        # エラーのときに通知したい

def over_write_current_element(new_element: str) -> bool:
    with open('tmp/old_element.txt', "w") as f:
        f.write(new_element)
        return True

if __name__ == "__main__": 
    compare_element()
