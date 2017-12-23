#include <stdio.h>
int main() {
    int a = 1, b = 0, c = 0, d = 0, e = 0, f = 0, h = 0;
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
                if ( (d * e) == b ) {
                    f = 0;
                }
                e += 1;
                printf("I d=%d, e=%d, f=%d, h=%d\n", d, e, f, h);
            } while ( e != b );
            printf("M d=%d, e=%d, f=%d, h=%d\n", d, e, f, h);
            d += 1;
        } while ( d != b );
        if ( f == 0 ) {
            h += 1;
        }
        b += 17;
        printf("O d=%d, e=%d, f=%d, h=%d\n", d, e, f, h);
    } while ( b != c);
    return 0;
}
