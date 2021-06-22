# Simple wasm function test
単純なCの関数をwasmにコンパイルして、Javascriptから使用するサンプル。
## Prerequisite
emscriptenをインストールしていること。

## コード
```javascript
let importObject = { imports: { imported_func: arg => console.log(arg) } };
fetch('main.wasm').then(response =>
  response.arrayBuffer()
).then(bytes =>
  WebAssembly.instantiate(bytes, importObject)
).then(obj => obj.instance.exports.int_add(3, 9)).then(num => console.log(num));
```
wasmでエクスポートされた`int_add`を呼び出すJavascriptのコード。
## Build
```
emcc --no-entry main.cpp -s EXPORTED_FUNCTIONS="['_int_add']" -o main.wasm
```
## 確認方法
```
$ python3 -m http.server 8001
```

ブラウザで`localhost:8001`を開くと、3+9の結果である`12`が、コンソールログに出力されていることが確認できる。

