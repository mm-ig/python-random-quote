import random
last = 14
rnd = random.randint(0,last)
rnd2 = random.randint(0,last)

def primary(xx):
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[xx].rstrip("\n"))

if __name__== "__main__":
  primary(rnd)
  primary(rnd2)
