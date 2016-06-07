import sys,os   
import time

import BinaryMatrix

# ---------------------------
def BinaryMatrix_LoadFromTxt(filename):
  print 'BinaryMatrix_LoadFromTxt : ', filename

  Num=0

  try:
    f = open(filename, 'r')
    while True:
      line = f.readline()
      if line:

          pass    # do something here
      else:
          break
    f.close()
    pass

  except:
    pass

def get_NOW_millisecond():
  return int(round(time.time() * 1000))

# ---------------------------
# start from here
for oneArg in sys.argv[1:]:
  t1 = get_NOW_millisecond()
  matrix1 = BinaryMatrix.BinaryMatrix()
  matrix1.LoadFromTxt(oneArg)
  t2 = get_NOW_millisecond()
  # matrix1.SaveToTxt('{0}.validate.result'.format(oneArg))

  print 'file [{0}], validate result=[{1}]'.format(oneArg, matrix1.validate())
  t3 = get_NOW_millisecond()
  
  print 'loadTime=[{0}], validateTime=[{1}]'.format(str(t2-t1), str(t3-t2))
  

