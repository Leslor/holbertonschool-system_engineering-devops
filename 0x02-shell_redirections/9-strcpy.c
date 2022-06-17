
#include <stdio.h>

char *_strcpy(char *dest, char *src)
{
	int size = 0;
	int i;
	while (*src != '\0')
	{
		size++;
		src++;
	}
	src -=size;
	for(i = 0; i <= size; i++)
	{
		dest[i]= src[i];
	}
	return (dest);

}


/**
 *  * main - check the code
 *   *
 *    * Return: Always 0.
 *     */
int main(void)
{
		    char s1[98];
			    char *ptr;

				    ptr = _strcpy(s1, "First, solve the problem. Then, write the code\n");
					    printf("%s", s1);
						    printf("%s", ptr);
							    return (0);
}
