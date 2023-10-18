# Python3 ,By :- shridhan jadhav
# Que. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
 
