n = int(input())
a = list(map(int, input().split()))

l = set()
for i in range(n//2):
    if a[i] != a[~i]:
        if a[i] > a[~i]:
            l.add((a[~i], a[i]))
        else:
            l.add((a[i], a[~i]))


class UnionFindTree:

    __all__ = ['find_root', 'merge', 'same', 'size']

    def __init__(self, maxsize=10**6):
        assert (maxsize > 0)

        self._n = maxsize # number of nodes
        # parent_or_size[V] ...
        #  if negative : V is the root of the group
        #                and the value*(-1) is the size of the tree
        #  else        : the value is the parent node of V
        self._parent_or_size = [-1]*maxsize

    def find_root(self, a):
        '''Find the root of a'''
        assert (0 <= a < self._n)

        pos = a
        children = []
        # Follow the path to the root
        while self._parent_or_size[pos] >= 0:
            children.append(pos)
            pos = self._parent_or_size[pos]
        else:
            root_pos = pos
        # Set the parent of child_pos to root_pos
        for child_pos in children:
            self._parent_or_size[child_pos] = root_pos
        return root_pos



    def merge(self, a, b):
        '''Merge the group of a and the group of b'''
        assert (0 <= a < self._n)
        assert (0 <= b < self._n)

        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a == root_b:
            return True
        else:
            # The size of the group of b should be larger
            if -self._parent_or_size[root_a] > -self._parent_or_size[root_b]:
                root_a, root_b = root_b, root_a
            # Merge the group of a with the group of b
            self._parent_or_size[root_b] += self._parent_or_size[root_a]
            self._parent_or_size[root_a] = root_b
            return False

    def same(self, a, b):
        '''See if the group of a and the group of b are the same'''
        assert (0 <= a < self._n)
        assert (0 <= b < self._n)

        root_a = self.find_root(a)
        root_b = self.find_root(b)
        return root_a == root_b

    def size(self, a):
        '''Return the size of the group of a'''
        assert (0 <= a < self._n)

        root_a = self.find_root(a)
        return -self._parent_or_size[root_a]

tree = UnionFindTree()
for i, j in l:
    tree.merge(i, j)

count = [0]*(10**6)
for i in range(1, 10**6-10):
    count[tree.find_root(i)] += 1

ans = 0
for i in count:
    if i > 0:
        ans += i-1

print(ans)
