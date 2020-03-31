class Entry:
    def __init__(self, hash_code, v, _prev=None, _next=None):
        self.hash_code = hash_code
        self.v = v
        self._prev = _prev
        self._next = _next

    def __str__(self):
        return "Entry{hash_code=%d, v=%s}" % (self.hash_code, self.v)

    def __repr__(self):
        return "Entry{hash_code=%d, v=%s}" % (self.hash_code, self.v)


class LRUCache:
    def __init__(self, max_size):
        self._max_size = max_size
        self._dict = dict()
        self._head = Entry(None, None)
        self._head.prev = self._head
        self._head.next = self._head

    def __setitem__(self, k, v):
        try:
            hash_code = hash(k)
        except TypeError:
            raise
#
#     old_entry = self._dict.get(hash_code)
#     new_entry = Entry(hash_code, v)
#     self._dict[hash_code] = new_entry
#
#     if old_entry:
#      prev = old_entry.prev
#      next = old_entry.next
#      prev.next = next
#      next.prev = prev
#
#     head = self._head
#     head_prev = self._head.prev
#     head_next = self._head.next
#
#     head.next = new_entry
#     if head_prev is head:
#      head.prev = new_entry
#     head_next.prev = new_entry
#     new_entry.prev = head
#     new_entry.next = head_next
#
#     if not old_entry and len(self._dict) > self._max_size:
#      last_one = head.prev
#      last_one.prev.next = head
#      head.prev = last_one.prev
#      self._dict.pop(last_one.hash_code)
#
#     def __getitem__(self, k):
#     entry = self._dict[hash(k)]
#     head = self._head
#     head_next = head.next
#     prev = entry.prev
#     next = entry.next
#
#     if entry.prev is not head:
#      if head.prev is entry:
#      head.prev = prev
#      head.next = entry
#
#      head_next.prev = entry
#      entry.prev = head
#      entry.next = head_next
#
#      prev.next = next
#      next.prev = prev
#
#     # return entry.v
#     #
#     # def get_dict(self):
#     # return self._dict
#
# # if __name__ == "__main__":
# #  cache = LRUCache(2)
# #  inner_dict = cache.get_dict()
# #
# #  cache[1] = 1
# #  assert inner_dict.keys() == [1], "test 1"
# #  cache[2] = 2
# #  assert sorted(inner_dict.keys()) == [1, 2], "test 2"
# #  cache[3] = 3
# #  assert sorted(inner_dict.keys()) == [2, 3], "test 3"
# #  cache[2]
# #  assert sorted(inner_dict.keys()) == [2, 3], "test 4"
# #  assert inner_dict[hash(2)].next.v == 3
# #  cache[4] = 4
# #  assert sorted(inner_dict.keys()) == [2, 4], "test 5"
# #  assert inner_dict[hash(4)].v == 4, "test 6"
#
#
# if __name__ == '__main__':
#     test_entry = Entry(4, "4", "prev", "next")
#     print(test_entry)
#     test_entry
