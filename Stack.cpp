#include<stdio.h>
#include<stdlib.h>
struct node
{
	int val;
	struct node *next;
};

struct stack
{
	int size;
	struct node *top;
};

bool isempty(struct stack *s)
{
	return(s->size==0);
};

void push(struct stack *s,int i)
{
	struct node *n=(struct node*)malloc(sizeof(struct node));
	n->val=i;
	n->next=s->top;
	s->top=n;
	(s->size)++;
}

struct node pop(struct stack *s)
{
	struct node *n=(struct node*)malloc(sizeof(struct node));
	if(isempty(s))
	{
		return(*n);
	}
	n=s->top;
	s->top=s->top->next;
	return(*n);
}

int peek(struct stack *s)
{	
	return(s->top->val);
}

int main()
{	
	struct stack *s=(struct stack*)malloc(sizeof(struct stack));
	s->size=0;
	push(s,2);
	printf("%d",peek(s));
}
  