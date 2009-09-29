import simple
import moving_block
import two_moving_blocks
import four_moving_blocks
ALL = {}
for l in [simple, moving_block, two_moving_blocks, four_moving_blocks]:
  ALL[l.name] = l
