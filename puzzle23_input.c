#include <stdio.h>

int main()
{
    int a = 1, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;

    b = 81;
    c = b;
    b = b * 100;
    b += 100000;
    c = b;
    c += 17000;
    f = 1;
    d = 2;
    e = 2;
    g = d;
    g *= e;
    g -= b;
    if ( g == 0 ) {
        f = 0;
    }
    e += 1;
    g = e;
    g -= b;
    if ( g != 0 ) {
        goto 15;
    }
    d += 1;
    g = d;
    g -= b;
    if ( g != 0 ) {
        goto 14;
    }
    if ( f == 0 ) {
        h += 1;
    }
    g = b;
    g -= c;
    if ( g == 0 ) {
        printf("h: %d\n", h);
        return 0;
    }
    b += 17;
    goto 12;
}
