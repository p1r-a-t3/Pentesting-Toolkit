# read data
data = []
with open('hidden-message.pcap', 'rb') as f:
data = f.read()

# get bits
bits = ''
for i in xrange(75, len(data), 81):
 bits += '0' if data[i:i+1]=='I' else '1'
# convert to chars
flag = ''
for i in xrange(0, len(bits), 8):
 flag += chr(int(bits[i:i+8], 2))
print flag
