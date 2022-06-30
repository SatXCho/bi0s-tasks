#include <stdio.h>
int main()
{
    int n, a, b, c, sum = 0;
    scanf("%d\n%d\n%d\n%d", &a, &b, &c, &n);
    for (int i = 0; i < n; i++){
        if (a > b && b > c){
            sum = sum + a;
            if (a > 0){
                a = a - 1;
            }
        }
        else if (b > a && b > c){
            sum = sum + b;
            if (b > 0){
                b = b - 1;
            }
        }
        else{
            sum = sum + c;
            if (c > 0)
            {
                c = c - 1;
            }
        }
    }
    printf("%d", sum);
    return 0;
}