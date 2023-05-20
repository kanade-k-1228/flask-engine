# flask-engine

```
$ export FLASK_APP=app
$ python3 -m flask run
```

## 仕様

`{` と `}` で囲われた部分を Python スクリプトとして解釈し実行する。

各スクリプト終了時、ローカル変数 `ret` の値でスクリプト部を置換する。

```
<p>{ret='Hello World'}</p>
>> 
<p>Hello World</p>
```

`ret`を除く変数のスコープはグローバル。`ret`はスクリプト実行ごとに空文字列になる。

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
