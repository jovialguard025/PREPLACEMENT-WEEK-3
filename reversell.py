class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def reverseList(self, h):
        
        if h==None: return None
        p=None
        c=h
        while c!=None:
            tmp=c.next   
            c.next=p     # flip
            p=c
            c=tmp
        # hopefully new head
        return p