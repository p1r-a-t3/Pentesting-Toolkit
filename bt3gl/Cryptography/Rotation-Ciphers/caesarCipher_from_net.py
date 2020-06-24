def caesar(plaintext,shift):

	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	#Create our substitution dictionary
	dic={}
	for i in range(0,len(alphabet)):
		dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

	#Convert each letter of plaintext to the corrsponding
	#encrypted letter in our dictionary creating the cryptext
	ciphertext=""
	for l in plaintext.lower():
		if l in dic:
			l=dic[l]
		ciphertext+=l

	return ciphertext

#Example useage
plaintext="the cat sat on the mat"
print "Plaintext:", plaintext
print "Cipertext:",caesar(plaintext,3)
#This will result in:
#Plaintext: the cat sat on the mat
#Cipertext: wkh fdw vdw rq wkh pdw
