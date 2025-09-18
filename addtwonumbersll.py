class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, h1, h2):
        # reverse both? maybe
        def rev(x):
            p=None
            c=x
            while c:
                nxt=c.next
                c.next=p
                p=c
                c=nxt
            return p
        
        h1=rev(h1)
        h2=rev(h2)

        carry=0
        d=None
        ans=None
        
        while h1 or h2 or carry:
            v1=h1.data if h1 else 0
            v2=h2.data if h2 else 0
            s=v1+v2+carry
            carry=s//10
            s=s%10
            
            nn=Node(s)
            if ans==None:
                ans=nn
                d=nn
            else:
                d.next=nn
                d=nn
                
            if h1: h1=h1.next
            if h2: h2=h2.next
        
        # oops,
        return rev(ans)
