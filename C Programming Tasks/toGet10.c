#include<stdio.h>
#include <math.h>

void ToGet10() {
    int pnum;
    scanf("%i\n", &pnum);
    int marks[pnum];
    int i;
    for (i = 0; i < pnum; i++) {
        scanf("%i", &marks[i]);
    }
    int msum = 0;
    for (i = 0; i < pnum; i++) {
        msum += marks[i];
    }
    float x= 0;
    x = 19*pnum - 2*msum;
    x = ceil(x);
    printf("%i\n", (int)x);
}

int main() {
    ToGet10();
    return 0;
}

