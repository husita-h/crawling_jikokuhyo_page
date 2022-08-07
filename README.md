# README

## memo
- pytype
    - https://github.com/google/pytype#config-file
- pylint
    - https://github.com/PyCQA/pylint
- コーディング規約
    - pep8-ja
        - https://pep8-ja.readthedocs.io/ja/latest/
    - https://google.github.io/styleguide/pyguide.html
- anyenv
    - https://github.com/anyenv/anyenv
- venv
    - `python3 -m venv repo_name`
- act
    - GitHub Actionsをローカルで実行するためのツール
    - https://github.com/nektos/act
    - `act イベント --container-architecture linux/amd64`
        - M1 Macの場合は以下のオプションが必要
            - `--container-architecture linux/amd64`

### requirements.txtの作り方

```sh
pip3 freeze >> requirements.txt
# https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-r
# requirements.txtをもとにライブラリをインストールするときはオプションをつける
```

作成した`requirements.txt`を利用して、ライブラリをインストールする
`pip3 install -r requirements.txt`

### やりたいこと
- 古いのを保存しておく
- 文字列で今取得したものと比較する
- 差分があれば、通知する
- 差分があれば、commitする
- PDFをダウンロードする
- ダウンロードしたファイルを文字認識する
- 認識した文字列を時刻表のデータとして使いやすいようにいいかんじに変換する
- DBに保存する
