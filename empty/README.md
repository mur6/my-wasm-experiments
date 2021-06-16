# Empty module
[WebAssembly テキストフォーマットを理解する - WebAssembly | MDN](https://developer.mozilla.org/ja/docs/WebAssembly/Understanding_the_text_format) を参考にして行った実験。

## Prerequisite
[WebAssembly/wabt: The WebAssembly Binary Toolkit](https://github.com/WebAssembly/wabt) をインストールしていること。

## ソース

### wat
`main.wat:`
```
(module)
```
空のモジュールである。

## wasmファイルのビルド
```
$ wat2wasm main.wat
```
上記コマンドで、watからwasmに変換することができる。

## 空であることの確認
```
$ xxd main.wasm
00000000: 0061 736d 0100 0000                      .asm....
```
