#include <stdio.h>

void swap(int *a, int *b) {
    int c;
    c = *a;
    *a = *b;
    *b = c;
}

int main() {
    int a = 0;
    int b = 1;

    printf("%d, %d\n", a, b);
    swap(&a, &b);
    printf("%d, %d\n", a, b);
}
