#include "lists.h"

/**
 * check_cycle - check if there's a cycle
 *
 * @list: the linked list
 *
 * Return: 1 if there is a cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	while (fast)
	{
		if (fast->next)
			fast = fast->next->next;
		else
			return (0);
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
