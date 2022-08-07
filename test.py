huga: str = "HUGA"

def test(hoge: str) -> str:
    print(f"{hoge}{huga}出力")
    return hoge

if __name__ == "__main__": 
    test("test")
