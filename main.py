import logging
import threading
import time
import random

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#Global Variables (totals and whatnot for threads)
startingMoney = 100
betAmount = 0.01





#--------------------------------------------
#Thread Function
#args: num_mines - the number of mines on the board out of 25 squares
def thread_function(num_mines):
  #4% chance (1 in 25) of mine to 96% chance (24 in 25)
  threshold = num_mines/25 
  winMtp = 
  bank=startingMoney

  
  rng = random.random()

  if bank>betAmount:
    #subtracting bet from bank
    bank=bank-betAmount
  #win
    if rng > threshold:
      #winnings
      bank=bank+(betAmount * winMtp)


  #nothing on lose
    
      
    
  
#=============================================================
#Main function
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()

  
    logging.info("Main    : all done")











  
#==============================================================