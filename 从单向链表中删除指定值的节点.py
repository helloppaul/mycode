class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = Node()
        self.length = 0
    def insert(self, val1, val2):
        cur = self.head
        node = Node(val2)
        while cur:
            if cur.val == val1:
                node.next = cur.next
                cur.next = node
                break
            else:
                cur = cur.next
    def remove(self, val):
        cur = self.head
        pre = None
        while cur:
            if cur.val == val:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def walk(self):
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()


while True:
    try:
        nums = list(map(int, input().split()))
        L = LinkedList()
        L.length, L.head.val = nums[0], nums[1]
        lst = nums[2:-1]
        i, j, pairs = 0, 1, []
        while i < len(lst):
            pairs.append((lst[i], lst[j]))
            i += 2
            j += 2
        for p in pairs:
            L.insert(p[1], p[0])
        L.remove(nums[-1])
        L.walk()
    except:
        break