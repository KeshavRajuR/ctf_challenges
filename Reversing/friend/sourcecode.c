#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#

void secret()
{
    int a1=0x66;
    int a2=0x6c;
    int a3=0x61;
    int a4=0x67;
    int a5=0x7b;
    int a6=0x31;
    int a7=0x5f;
    int a8=0x68;
    int a9=0x34;
    int a10=0x76;
    int a11=0x33;
    int a12=0x5f;
    int a13=0x37;
    int a14=0x68;
    int a15=0x33;
    int a16=0x5f;
    int a17=0x56;
    int a18=0x31;
    int a19=0x72;
    int a20=0x75;
    int a21=0x35;
    int a22=0x7d;
}

int main()
{
	char pwd[100];

    printf("Enter password to see the secret :");
    scanf("%s", pwd);

    printf("Alright checking if you've entered the right password \n");
    sleep(1);
    printf("Loading\n");

    for(int i=0; i<10; ++i)
    {
        printf(" . ");
        fflush(stdout);
        sleep(1);
    }

    printf("\nWRONG PASSWORD :|\n");
    

	return 0;
}