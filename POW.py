import hashlib
import datetime
import time

class Block: 
    def __init__(self, data, previous_hash): 
        self.data = data 
        self.previous_hash = previous_hash 
        self.timestamp = datetime.datetime.now() 
        self.nonce = 0
        self.hash = self.calculate_hash() 
        
    def calculate_hash(self): 
        sha = hashlib.sha256() 
        sha.update(str(self.data).encode('utf-8') + 
                str(self.previous_hash).encode('utf-8') + 
                str(self.nonce).encode('utf-8')) 
        return sha.hexdigest() 
    
    def mine_block(self, target_difficulty, adding=False): 
        start = time.time()
        while self.hash[:len(target_difficulty)] != target_difficulty: 
            self.nonce += 1
            self.hash = self.calculate_hash() 
        end = time.time()
        if adding:
            print("Block added:", self.hash)
        else:
            print(f"Block mined: {self.hash} in {end-start} seconds")
        

class Blockchain: 
    def __init__(self): 
        self.chain = [self.create_genesis_block()] 
  
    def create_genesis_block(self): 
        return Block("Genesis Block", "0") 
  
    def add_block(self, new_block): 
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block("0000", adding=True) 
        self.chain.append(new_block)