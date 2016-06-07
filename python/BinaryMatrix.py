import traceback

class BinaryMatrix:
  def __init__(self):
    self.m_Num = 0
    self.DEBUG = 1
    pass

  def ResetToN(self, N):
    self.m_Num = N
    self.m_matrix = [[0] * self.m_Num for row in range(self.m_Num)]

  def strIsTrue(self, str):
    return str == '1'

  def strIsFalse(self, str):
    return (str == '0') or (str == 'o')

  def strIsValid(self, str):
    return self.strIsTrue(str) or self.strIsFalse(str)

  def rowIsValid(self, row):
    return (0<=row) and (row<self.m_Num)
  def colIsValid(self, col):
    return (0<=col) and (col<self.m_Num)

  def clickCell(self, row, col):
    if not (self.rowIsValid(row)):
      return;

    if not (self.colIsValid(col)):
      return;

    ActionList = [
      [ 0, -1],
      [ 0,  1],
      [ 0,  0],
      [-1,  0],
      [ 1,  0],
    ]
    for action in ActionList:
      row_new = row + action[0]
      col_new = col + action[1]
      if (self.rowIsValid(row_new)) and (self.colIsValid(col_new)):
        self.m_matrix[row_new][col_new] = (self.m_matrix[row_new][col_new]+1)%2
    pass

  def validate(self):
    board = BinaryMatrix()
    board.ResetToN(self.m_Num)

    row_tmp = 0
    for row in self.m_matrix:
      col_tmp = 0
      for cell in row:
        if cell==1:
          board.clickCell(row_tmp, col_tmp)
        col_tmp=col_tmp+1
      row_tmp=row_tmp+1


    for row in board.m_matrix:
      for cell in row:
        if cell!=1:
          board.SaveToTxt('validate.board.N_{0}'.format(self.m_Num))
          return False
    return True

  def LoadFromTxt(self, filename):
    print 'LoadFromTxt : ', filename

    try:
      self.ResetToN(0)

      row_tmp = 0
      f = open(filename, 'r')
      while True:
        line = f.readline()
        line = line.rstrip('\r')
        line = line.rstrip('\n')

        if not line:
          break;

        if line:
          splitedList = line.split(',')

          # calc N
          if self.m_Num <= 0:
            Num_tmp = 0
            for item in splitedList:
              if self.strIsValid(item):
                Num_tmp = Num_tmp+1
            self.ResetToN(Num_tmp)

          # now, m_Num is ready
          col_tmp = 0
          for item in splitedList:
            if not item:
              continue

            if self.strIsTrue(item):
              self.m_matrix[row_tmp][col_tmp] = 1
            elif self.strIsFalse(item):
              self.m_matrix[row_tmp][col_tmp] = 0
            else:
              print 'ERROR : invalid char [{0}]'.format(item)
              pass
            col_tmp = col_tmp + 1
        row_tmp = row_tmp + 1
        pass

      f.close()
      if row_tmp != self.m_Num:
        print 'have NOT loaded enough row, should load [{0}] rows, only loaded [{1}]'.format(self.m_Num, row_tmp)

    except:
      print traceback.format_exc()
      pass

  def SaveToTxt(self, filename):
    # print '=========================================='
    print 'SaveToTxt : ', filename

    try:
      f = open(filename,'w+')
      for row in self.m_matrix:
        for cell in row:
          cell_str = 'o'
          if cell == 1:
            cell_str = '1'
          f.write(cell_str)
          f.write(',')
        f.write('\n')
      f.close()

    except:
      print traceback.format_exc()
      pass

if __name__ == '__main__':
  print 'main of class BinaryMatrix'
