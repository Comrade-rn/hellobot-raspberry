from relayer import Relayer 
from time import sleep

relayer = Relayer()

relayer.print_keys()

print "connected?", relayer.check_connection()

print ("connecting...")
relayer.connect()

print "connected?", relayer.check_connection()

while True:

  x = raw_input("F B L R A H D X:")
  
  if x == 'F':
    relayer.command("forward")

  if x == 'B':
    relayer.command("reverse")

  if x == 'L':
    relayer.command("left")

  if x == 'R':
    relayer.command("right")

  if x == 'F':
    relayer.command("move arms")

  if x == 'F':
    relayer.signal("listening")

  if x == 'F':
    relayer.signal("message decoded")

  if x == 'X':
    break
