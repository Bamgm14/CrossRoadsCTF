#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void encrypt(char* str, int len){
for (int i = 0; i < len; i++){
	str[i] ^= i; 
}
}

void someCleanUpstuff(){
	char ch = getc(stdin);
	while (!ch){
		ch = getc(stdin);
	}
}

int main(){
unsigned int keyCode;
scanf("%d", &keyCode);

if (keyCode > 0xEEFBEEF){
	puts("First phase passed..");
} else { exit(1); }
if (keyCode & 1){
	puts("Second phase passed..");
} else { exit(1); }
if (!(keyCode & (keyCode+1))){
	puts("Third phase passed..");
} else { exit(1); }
if (!(keyCode >> 29)){
	puts("Fourth phase passed..");
} else {exit(1);}

puts("\nNow for the final verification! Enter the super secret password: \n");

char buf[100];
someCleanUpstuff();

fgets(buf,100, stdin);
encrypt(buf,100);
if (!strncmp(buf,"CSq@PC}GW}JxxhQ?vN` b&dd+d",26)){
	puts("You did it, Alice!");
}
}
