def search_char(s, c, index):
       
   if index >= len(s):
       return -1
   
   else:
       if s[index] == c:
           return index
       else:
           search_char(s, c, index+1)
       