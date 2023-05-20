# flask-engine

```
$ export FLASK_APP=app
$ python3 -m flask run
```

## 仕様

`{` と `}` で囲われた部分（スクリプトブロック）を Python スクリプトとして解釈し実行する。

ファイルを先頭から読み取り、スクリプトブロックを見つけ次第、逐次スクリプトを実行する。スクリプトブロックの実行完了後、ローカル変数 `ret` の値でスクリプト部を置換する。

```
<p>{ret = "Hello World"}</p> >> <p>Hello World</p>
```

`ret` を除き、スコープはグローバル。`ret` はスクリプトブロック実行ごとに空文字列になる。

```
{i = 2; ret += str(i)} >> 2
{i += 2; ret += str(i)} >> 4
```

Pythonの組込関数が使える。モジュールのインポートも可能。

```
{
import numpy as np
ret = str(np.mean(range(10)))
} >> 4.5
```
