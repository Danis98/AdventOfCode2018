words = open("day9.input", "r").read().rstrip().split(" ")

players = int(words[0])
marbles = int(words[6])*100+1

class DoublyLinkedCircularList:
    def __init__(self):
        self.elem_ctr = 0
        self.elem = {}
        self.next = {}
        self.prev = {}
        self.ptr = None

    # add after pointed element
    def add(self, e):
        if self.ptr == None:
            self.ptr = 0
            self.elem[self.ptr] = e
            self.next[self.ptr] = self.ptr
            self.prev[self.ptr] = self.ptr
        else:
            nxt = self.next[self.ptr]
            self.elem[self.elem_ctr] = e
            self.prev[self.elem_ctr] = self.ptr
            self.next[self.elem_ctr] = nxt

            self.next[self.ptr] = self.elem_ctr
            self.prev[nxt] = self.elem_ctr
        self.elem_ctr += 1

    # remove element
    def remove(self):
        self.next[self.prev[self.ptr]] = self.next[self.ptr]
        self.prev[self.next[self.ptr]] = self.prev[self.ptr]
        n_ptr = self.next[self.ptr]
        self.elem.pop(self.ptr)
        self.next.pop(self.ptr)
        self.prev.pop(self.ptr)
        self.ptr = n_ptr

    def advance_ptr(self):
        self.ptr = self.next[self.ptr]

    def retreat_ptr(self):
        self.ptr = self.prev[self.ptr]

    def get_elem(self):
        return self.elem[self.ptr]

    def print_list(self):
        if self.ptr == None:
            return "()"
        s = "(%r)-" % self.elem[self.ptr]
        p = self.next[self.ptr]
        while p != self.ptr:
            s += ">%r-" % self.elem[p]
            p = self.next[p]
        s += "\n^"+("-"*(len(s)-2))+"|"
        return s

scores = {i:0 for i in range(players)}

lst = DoublyLinkedCircularList()
lst.add(0)

for i in range(1, marbles):
    if i % 23 == 0:
        player = i % players
        for j in range(7):
            lst.retreat_ptr()
        scores[player] += i + lst.get_elem()
        lst.remove()
    else:
        lst.advance_ptr()
        lst.add(i)
        lst.advance_ptr()
print(max(scores.values()))
