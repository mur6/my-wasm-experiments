#include <stdlib.h>
#include <emscripten.h>

#ifdef __cplusplus
extern "C" {
#endif

void EMSCRIPTEN_KEEPALIVE only_malloc(int a)
{
    char * buffer = (char*)malloc(sizeof(char) * 128);
}

#ifdef __cplusplus
}
#endif
