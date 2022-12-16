import numpy as np

class SlidingPuzzle:
  "Initialize the SlidingPuzzle with N, M and State"
  def __init__(self, nrows, ncols, state):
    self.nrows = nrows
    self.ncols = ncols
    self.state = np.array(list(state))
  
  "Print the Puzzle"
  def print_board(self):
    print(self.state)
  
  "Get the State"
  def get_state(self):
    return self.state
  
  "Check if the neighbour cell is a block cell or not"
  def block_cell(self, ind):
    if self.state[ind] == -1:
      return True 
    return False

  "Get all the neigbours(getting the ind number and creating the new puzzle states) of the current state"
  def get_neighbours(self):
    ind = np.argwhere(self.state == 0)[0, 0]
    swap_inds = []
    ncols = self.ncols
    if ind - self.ncols >= 0 and not self.block_cell(ind - ncols):
        swap_inds.append(ind - ncols)
    if ind + self.ncols < self.nrows * self.ncols and not self.block_cell(ind + ncols):
        swap_inds.append(ind + ncols)
    if ((ind - 1) // self.ncols) == ((ind) // self.ncols) and not self.block_cell(ind - 1):
        swap_inds.append(ind - 1)
    if ((ind + 1) // self.ncols) == ((ind) // self.ncols) and not self.block_cell(ind + 1):
          swap_inds.append(ind + 1)
    return [self.get_swapped_puzzle(ind, sind) for sind in swap_inds]


  "Get the swapped puzzle by swapping the index of the zero and it's neighbour index"
  def get_swapped_puzzle(self, zero_ind, swap_ind):
        state = self.state.copy()
        state[zero_ind], state[swap_ind] = state[swap_ind], state[zero_ind]
        return SlidingPuzzle(nrows=self.nrows,
                             ncols=self.ncols,
                             state=state)
  
  "Get the reshapped puzzle"
  def get_reshaped_state(self):
        return np.reshape(self.state, (self.nrows, self.ncols))

  "Get the moves of the zero"
  def get_zero_index_position(self):
    matrix = np.reshape(self.state, (self.nrows, self.ncols))
    ind = np.argwhere(matrix == 0)[0]
    return ind

  def __eq__(self, other):
      return len(self.state) == len(other.state) and (self.state == other.state).all()

  def __str__(self):
      return str(self.get_reshaped_state())

  def __hash__(self):
      return hash(tuple(self.state))