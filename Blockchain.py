from POW import *

# create a new blockchain 
blockchain = Blockchain() 
  
# create and add three blocks to the blockchain 
block1 = Block("Transaction Data 1", "") 
blockchain.add_block(block1) 
  
block2 = Block("Transaction Data 2", "") 
blockchain.add_block(block2) 
  
block3 = Block("Transaction Data 3", "") 
blockchain.add_block(block3)
print("-----------------------------------------")
block1.mine_block("0000")