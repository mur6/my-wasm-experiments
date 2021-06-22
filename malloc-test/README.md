# DataCount section test
mallocだけを行うCの関数をwasmにコンパイルしたとき、DataCountというセクションが生成されるかどうかを確認するテスト。

## Prerequisite
emscriptenをインストールしていること。

## `-mbulk-memory` なし
`-mbulk-memory` というオプションなしで、mallocだけを行う簡単なCの関数をwasmにコンパイルする。
```
$ emcc --no-entry main.cpp -s EXPORTED_FUNCTIONS="['_only_malloc']" -o main.wasm
$ wasm-objdump -h main.wasm

main.wasm:      file format wasm 0x1

Sections:

     Type start=0x0000000a end=0x00000029 (size=0x0000001f) count: 6
 Function start=0x0000002b end=0x00000041 (size=0x00000016) count: 21
    Table start=0x00000043 end=0x00000048 (size=0x00000005) count: 1
   Memory start=0x0000004a end=0x00000050 (size=0x00000006) count: 1
   Global start=0x00000052 end=0x00000065 (size=0x00000013) count: 3
   Export start=0x00000068 end=0x0000013d (size=0x000000d5) count: 12
     Elem start=0x0000013f end=0x00000146 (size=0x00000007) count: 1
     Code start=0x00000149 end=0x00001b4b (size=0x00001a02) count: 21
     Data start=0x00001b4d end=0x00001b58 (size=0x0000000b) count: 1
```
DataCountというセクションはないことが分かる。

## `-mbulk-memory` つき
今度は `-mbulk-memory` というオプションをつけてコンパイルしてみる。
```
$ emcc --no-entry -mbulk-memory main.cpp -s EXPORTED_FUNCTIONS="['_only_malloc']" -o main.wasm
$ wasm-objdump -h main.wasm

main.wasm:      file format wasm 0x1

Sections:

     Type start=0x0000000a end=0x00000029 (size=0x0000001f) count: 6
 Function start=0x0000002b end=0x00000041 (size=0x00000016) count: 21
    Table start=0x00000043 end=0x00000048 (size=0x00000005) count: 1
   Memory start=0x0000004a end=0x00000050 (size=0x00000006) count: 1
   Global start=0x00000052 end=0x00000065 (size=0x00000013) count: 3
   Export start=0x00000068 end=0x0000013d (size=0x000000d5) count: 12
     Elem start=0x0000013f end=0x00000146 (size=0x00000007) count: 1
DataCount start=0x00000148 end=0x00000149 (size=0x00000001) count: 1
     Code start=0x0000014c end=0x00001b4e (size=0x00001a02) count: 21
     Data start=0x00001b50 end=0x00001b5b (size=0x0000000b) count: 1
```
DataCountというセクションが生成されていることが分かる。
