# ll_utils

Simple Python package to create and show rotated linked lists.

## Example

```python
from ll_utils import create_rotated_linked_list, show_linked_list

arr = [1,2,3,4,5]
head = create_rotated_linked_list(arr, 2)
show_linked_list(head)