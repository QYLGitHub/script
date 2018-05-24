# -*- coding:utf-8 -*-
def flatten(iterable=None, item=None):
    """将任何嵌套的可迭代对象展平
    example:
    ```
        >>> from flatten import flatten
        >>> data = [1,2,3,4,[1,2,3, {1,2,3,4}, (1,2,3,4, (1,2,3,4)), {1:2,4:5}]]
        >>> print(flatten(data))
        ... [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, {1: 2, 4: 5}]
    ```
    :param iterable: 嵌套的可迭代对象 type: iterable
    :param item: None
    :return: 已经展平的list type: list
    """
    if iterable is None:
        iterable = self.__item
    if item is None:
        item = []
    if not iterable:
        return item
    for i in iterable:
        if not isinstance(i, (list, tuple, set)):
            item.append(i)
        else:
            flatten(iterable=i, item=item)
    return item


if __name__ == '__main__':
    data = [1, 2, 3, 4, [1, 2, 3, {1, 2, 3, 4}, (1, 2, 3, 4, (1, 2, 3, 4)), {1: 2, 4: 5}]]
    print(flatten(data))
