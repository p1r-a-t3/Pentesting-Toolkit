import sys
from pygenere import Vigenere, VigCrack


def get_key(msg):
  # Vigenere Cypher
  key =  VigCrack(msg).crack_codeword()
  dec_msg = VigCrack(msg).crack_message()
  dec_msg =  dec_msg.replace(" ", "")
  return key, dec_msg


def solve(msg, key):
  dec_msg = Vigenere(msg).decipher(key)
  dec_msg =  dec_msg.replace(" ", "")
  return dec_msg



if __name__ == '__main__':

  # getting the key
  with open('cipher', 'r') as f:
        msg = f.readlines()
        msg_in = msg[0].strip()
        key, answer = get_key(msg_in)
        print 'Message: ' + msg_in
        print
        print 'Answer: ' + answer
        print '(key: ' + key + ')'
  

  # deciphering                                 
  key = 'FREKEY'
  with open('pass', 'r') as f:
	msg = f.readlines()
	answer = solve(msg[0].strip(), key)
	print
	print "The answer is: " + answer
