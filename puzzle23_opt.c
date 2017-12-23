#include <stdio.h>
int main() {
    int a = 1, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;
    b = 81;
    c = b;
    b = b * 100;
    b += 100000;
    c = b;
    c += 17000;
    printf("count values %d %d\n", b, c);
    do {
        f = 1;
        d = 2;
        do {
            e = 2;
            do {
                g = d;
                g *= e;
                g -= b;
                if ( g == 0 ) {
                    f = 0;
                }
                e += 1;
                g = e;
                g -= b;
                printf("I d=%d, e=%d, f=%d, g=%d, h=%d\n", d, e, f, g, h);
            } while ( g != 0 );
            d += 1;
            g = d;
            g -= b;
            printf("M d=%d, e=%d, f=%d, g=%d, h=%d\n", d, e, f, g, h);
        } while ( g != 0  );
        if ( f == 0 ) {
            h += 1;
        }
        g = b;
        g -= c;
        if ( g == 0 ) {
            return 1;
        }
        b += 17;
        printf("O d=%d, e=%d, f=%d, g=%d, h=%d\n", d, e, f, g, h);
    } while (1);
    return 0;
}
