reverse_v1:	借助list来找到倒数第n个元素

reverse:
1. 使用两个指针 fast和slow
2. fast指针先移n步， 然后fast和slow同时移动，这时fast和slow间隔为n
3. 当fast移动链表尾部的时候，slow刚好就是倒数第n个元素