# flask-engine

```
$ export FLASK_APP=app
$ python3 -m flask run
```

## 仕様

`{` と `}` で囲われた部分を Python スクリプトとして解釈し実行する。

各スクリプト終了時、ローカル変数`ret`の値でスクリプト部を置換する。

```
<p>{ret='Hello World'}</p>

<p>Hello World</p>
```
