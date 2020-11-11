from collections import deque

class Item:
    '''
    Representation of items in PriorityQueue.
    For use internally in PriorityQueue class only.
    '''
    def __init__(self, label, key):
        self.label, self.key = label, key

class PriorityQueue:
    '''
    Heap-based priority queue implementation.

    '''
    def __init__(self):
        self.A = []
        self.label2idx = {}

    def min_heapify_up(self, c):
        '''
        Maintains the min-heap property by swapping the item at the given index upwards.
        (You SHOULD NOT call this function. It is used internally for maintaining the heap)
        '''
        if c == 0: return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_up(p)

    def min_heapify_down(self, p):
        '''
        Maintains the min-heap property by swapping the iteam at the given index downwards.
        (You SHOULD NOT call this function. It is used internally for maintaining the heap)
        '''
        if p >= len(self.A): return
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A): l = p
        if r >= len(self.A): r = p
        c = l if self.A[r].key > self.A[l].key else r
        if self.A[p].key > self.A[c].key:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)

    def size(self):
        '''
        Retrieves the number of elements in the priority queue
        Args:
            None
        Returns:
            Size of the priority queue
        '''
        return len(self.A)

    def insert(self, label, key):
        '''
        Inserts a new element into the priority queue
        Args:
            label: Identifying nformation to be stored along with the priority
            key: Priority of the element being inserted
        Returns:
            None
        '''
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)

    def extract_min(self):
        '''
        Removes and returns the minimum-priority element in the priority queue
        Args:
            None
        Returns:
            The identifier for the element removed.
        '''
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    def decrease_key(self, label, key):
        '''
        Decreases the priority of a given item in the queue
        Args:
            label: Identifying information stored along with priority
            key: New priority of the item with the specified label
        Returns:
            None
        '''
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)

'''
###################################################
### PLEASE DO NOT MODIFY ANY OF THE CODE ABOVE! ###
### This code is included for your convenience, ###
### but modifications may cause you a headache! ###
###################################################
'''

def bidi(adj, s, t):
    '''
    Implement bidirectional dijkstra.
    Args:
        adj: Routers are identified by unique integer id's. adj[u][v] is the latency between router u and router v.
        For a router, u, with no neighbor adj[u] = {}.
        s: Starting router id.
        t: Destination router id.
    Returns:
        The minimum weighted distance from s to t. If there is no path from s to t, return None.
    Note: Bidirectional dijkstra cuts down the number of nodes you visit. Only insert nodes into your priority queue (and whatever other data structures you may be maintaining)
    when you actually discover them through relaxation.
    '''
    infinity = float("inf")
    adjr = dict() #adjacency list dict for reverse
    d = dict() #distance from s
    dr = dict() #distance from t
    pq = PriorityQueue() #priority q for forward djiksta
    pqr = PriorityQueue() #priority q for backward djikstra
    seen = set() #useful for stopping conditions
    seenr = set() #useful for stopping conditions
    u = None

    #create reverse adjacency list mapping value to key
    for key in adj:
        adj_set = adj[key]
        if key not in adjr:#for nodes with only outgoing edges
            adjr[key] = dict()
        for k in adj_set:
            if k not in adjr:
                adjr[k] = dict()
            adjr[k][key] = adj_set[k]

    d[s] = 0
    dr[t] = 0

    pq.insert(s,0)
    pqr.insert(t,0)

    while max(pq.size(),pqr.size()) > 0:
        #forward djikstra step
        if pq.size() > 0:
            node = pq.extract_min()
        else:
            node = None

        if node is not None:
            for k in adj[node]:
                dist = adj[node][k] + d[node]
                if k not in d:
                    d[k] = dist
                    pq.insert(k,d[k])
                elif  d[k] > adj[node][k] + d[node]:
                    d[k] = adj[node][k] + d[node]
                    pq.decrease_key(k,d[k])

            if node in seenr:
                u = node
                break

            seen.add(node)



        #backward djikstra step
        if pqr.size() >0:
            noder = pqr.extract_min()
        else:
            noder = None

        if noder is not None:
            for k in adjr[noder]:
                dist = adjr[noder][k] + dr[noder]
                if k not in dr:
                    dr[k] = dist
                    pqr.insert(k,dr[k])
                elif  dr[k] > adjr[noder][k] + dr[noder]:
                    dr[k] = adjr[noder][k] + dr[noder]
                    pqr.decrease_key(k,dr[k])

            if noder in seen:
                u = noder
                break

            seenr.add(noder)


    #tracepath
    if u is not None:
        mu = d[u] + dr[u]

        for v in d.keys():
            if v in dr.keys():
                if mu > d[v] + dr[v]:
                    mu = d[v] + dr[v]

        return mu

    return None
