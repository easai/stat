""" Stat module """
def median(lst):
  """ Calculates median value of the given lst """
  lst=sorted(lst)
  n=len(lst)
  if n&1==0:
    res=(lst[(n>>1)-1]+lst[n>>1])*.5
  else:
    res=lst[n>>1]
  return res


if __name__=="__main__":
  print(median([5,4,4,5]))
