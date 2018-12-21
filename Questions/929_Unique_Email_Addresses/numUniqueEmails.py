class Solution(object):
    def emailBuidler(self, email):
        # do not need to check correctness because it is give we will have EXACTLY 1 @ sign
        local_name, domain_name = email.split('@')
        
        # split by + and take the first element in the split array
        # if there is no + the split array will have size 1 and this will work
        # if there is at least 1 + then taking the 0th element will still work
        remainder = local_name.split('+')
        # no_periods = "".join(remainder[0].split('.'))
        # better way
        no_periods = remainder[0].replace('.','')
            
        return no_periods + domain_name
    
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set([])
        
        for email in emails:
            correctEmail = self.emailBuidler(email)
            email_set.add(correctEmail)
        
        return len(email_set)
            
    
