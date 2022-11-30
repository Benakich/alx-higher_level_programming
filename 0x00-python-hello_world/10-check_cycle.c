#include "lists.h"

/**
 * check_cycle - check for cycle in singly linked list
 * @list: list to check
 * Return: 0 if cycle 1 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	while (list != NULL)
	{
		current = list;
		list = list->next;
		if (current <= list)
			return (1);
	}
	return (0);
}
