import requests
from bs4 import BeautifulSoup # http://kondou.com/BS4/
import pdb # pdb.set_trace()
# from git import Repo # https://gitpython.readthedocs.io/en/stable/tutorial.html

URL = 'https://www.city.kita.tokyo.jp/d-shisetu/kurashi/bus/bus.html'

def get_current_element() -> str:
    res  = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    # もっとよい書き方があるはず
    # 文字検索をしたい
    jikokuhyo_element = soup.find("a", id="E1").next_element.next_element.next_element.next_element
    return str(jikokuhyo_element)

def compare_element() -> bool:
    new_data = get_current_element()
    try:
        with open('tmp/old_data.txt', "r") as f:
            old_data = f.read()
            if old_data == new_data:
                print("Page is not updated")
                # commit_diff()
                return False
            else:
                print("Page is updated!!")
                over_write_current_element(new_data)
                # commit_diff()
                return True
    except:
        print("Except is occured")
        return False
        # エラーのときに通知したい

def over_write_current_element(new_data: str) -> bool:
    with open('tmp/old_data.txt', "w") as f:
        f.write(new_data)
        return True

# def commit_diff():
#     repo = git.Repo()

if __name__ == "__main__": 
    compare_element()
