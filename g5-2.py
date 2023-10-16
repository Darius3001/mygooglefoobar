"""
1. precalc

2. build columns and count them

"""

class BlockCalculator:
  def __init__(self) -> None:
    # TODO fill precalc
    self.precalc = {}
  
  def possiblePastBlocks(self, currentBlock, previousBlock=[[None, None],[None,None]]):
    #TODO
    pass

class ColumnCalculator:
  def __init__(self) -> None:
    pass

  def possiblePastColumns(self, currentColumn, previousColumn=None):
    if previousColumn is None:
      # first column
      pass
    pass

def solution(g):
  precalc = BlockCalculator()
  