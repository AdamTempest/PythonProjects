# take two normal list
# reverse them
# add them
# return the reversed list of result

def addTwoNumbers(l1, l2):
	sumNum = 0
    numlist = [l1,l2]
    for i in numlist:
        strNum = ''
        for j in i:
            strNum = str(j) + strNum
        sumNum += int(strNum)
    sumlist = [int(k) for k in str(sumNum)[::-1]]
    return sumlist;


###################### Real Deal ##########################
## Take two ListNode and convert them into ordinary list ##
##      reverse the lists and convert them into int      ##
##                       add them                        ##
##          return the ListNode of reversed sum          ##
###########################################################
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [l1,l2]
        lists = [[],[]] 
        sumNum = 0
        nodeslen=len(nodes)
        for i in range(nodeslen):
            value = nodes[i]
            while value:
                lists[i].insert(0,value.val)
                value = value.next

        for i in lists:
            # Converts list type numbers to int and add them to sum.
            sumNum += sum(d * 10**j for j, d in enumerate(i[::-1])) 
        
        # Converts int sum to reversed list
        strSum = str(sumNum)
        sumlist = [int(k) for k in strSum[::-1]] 
        
        # Converts sumlist to nodelist
        head = ListNode(sumlist[0])
        tail = head
        length = len(sumlist);
        for e in range(1,length):
            tail.next = ListNode(sumlist[e])
            tail = tail.next

        return head;
############# Performance #############
## Runtime: 146 ms # Memory: 13.9 MB ##
#######################################



############ Ideal solution ##########
## Runtime: 61 ms # Memory: 13.9 MB ##
######################################

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], extra: int = 0) -> Optional[ListNode]:
        val = l1.val + l2.val + extra
        l3 = ListNode(val % 10)
        extra = val // 10
        if l1.next or l2.next or extra:
            l3.next = self.addTwoNumbers(l1.next or ListNode(0), l2.next or ListNode(0), extra)
        return l3
