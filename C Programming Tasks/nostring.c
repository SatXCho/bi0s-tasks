#include<stdio.h>
#include<stdlib.h>

int main() {
   char s1[100], s2[100];
   int i=0;
   fgets(s1,100,stdin);
   fgets(s2,100,stdin);

   while (s1[i] == s2[i] && s1[i] != '\0')
      i++;
   if (s1[i] < s2[i])
      printf("First");
   else if (s1[i] > s2[i])
      printf("Second");
   else
      printf("Equal");
   return 0;
}