# Simple function export

## Prerequisite
[WebAssembly/wabt: The WebAssembly Binary Toolkit](https://github.com/WebAssembly/wabt) をインストールしていること。

## ソース
### Javascript
```javascript
let importObject = { imports: { imported_func: arg => console.log(arg) } };
fetch('main.wasm').then(response =>
  response.arrayBuffer()
).then(bytes =>
  WebAssembly.instantiate(bytes, importObject)
).then(obj =>
  obj.instance.exports.exported_func()
);
```
### wat
`main.wat:` 42を返すだけの関数。

## wasmファイルのビルド
```
$ wat2wasm main.wat
```
上記コマンドで、watからwasmに変換することができる。

## 確認方法
```
$ python3 -m http.server 8001
```

ブラウザで`localhost:8001`を開くと、コンソールログに`42`と出力されることが、safari, chrome共に確認できる。
