#include <emscripten.h>

#ifdef __cplusplus
extern "C" {
#endif

int EMSCRIPTEN_KEEPALIVE int_add(int a, int b)
{
    return a + b;
}

#ifdef __cplusplus
}
#endif
