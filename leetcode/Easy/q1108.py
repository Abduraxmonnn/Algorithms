class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")


if __name__ == '__main__':
    address = "255.100.50.0"
    print(Solution().defangIPaddr(address))

# address.replace(".", "[.]") bu addresdagi (.)larni ([.])ga almawtiradi (replace)bu ishni qberadi
# https://leetcode.com/problems/defanging-an-ip-address/
