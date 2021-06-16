# Invalid section
## ソース
`main.wat:` 42を返すだけの関数。

## 確認方法
```
$ python3 -m http.server 8001
```

ブラウザで`localhost:8001`を開くと、コンソールログに`42`と出力されることが、safari, chrome共に確認できる。
