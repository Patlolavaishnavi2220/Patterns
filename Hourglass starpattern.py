n=int(input())
#upper half
for i in range(n,0,-1):
    spaces=" "*(n-i)
    stars="* "*i
    print(spaces+stars)
#lower half
for i in range(2,n+1):
    spaces=" "*(n-i)
    stars="* "*i
    print(spaces+stars)
'''output:
4
* * * * 
 * * * 
  * * 
   * 
  * * 
 * * * 
* * * *
'''
