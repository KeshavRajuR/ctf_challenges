#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 32
char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig)
{
    fprintf(stderr, "%s\n", flag);
    fflush(stderr);
    exit(1);
}

int main()
{
    FILE *flagFile = fopen("flag.txt", "r");
    if (flagFile == NULL)
    {
        printf("The file containing the flag is missing. @challenge-creator to fix this issue.\n");
        exit(0);
    }
    fgets(flag, FLAGSIZE_MAX, flagFile);
    signal(SIGSEGV, sigsegv_handler);
    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    char input[32];
    puts("Go ahead and fill up the jar...\n");
    gets(input);
    printf("Thanks for filling the jar with %s\n", input);
}
