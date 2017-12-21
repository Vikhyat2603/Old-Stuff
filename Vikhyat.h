#include<stdio.h>
float sqrt(float num)
{
	float c=0;
	float c2=1000;
	while(1)
	{
 	    if((c*c)>(num-(0.000001*num)) && (c*c)<(num+(0.000001*num)))
 		{	
	    	break;
		}
		if((c+c2)*(c+c2)>num)
		{
			c2/=10;
			c=0;
		}
		c+=c2;
	}
	return c;
}
float cbrt(float num)
{
	float c=0;
	float c2=1000;
	while(1)
	{
 	    if((c*c*c)>(num-(0.000001*num)) && (c*c*c)<(num+(0.000001*num)))
 		{	
	    	break;
		}
		if((c+c2)*(c+c2)*(c+c2)>num)
		{
			c2/=10;
			c=0;
		}
		c+=c2;
	}
	return c;
}
float powerf(float a,int b)
{
 int i;
 float ret=1;
 for(i=1;i<=b;i++)
 {
 	ret*=a;
 }
}
