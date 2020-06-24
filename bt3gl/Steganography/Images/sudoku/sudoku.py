from PIL import Image


# solved sudoku
sudoku = '''
964127538
712385694
385496712
491578263
238614975
576239841
627843159
153962487
849751326
'''
s = sudoku.replace('\n', '')

image = Image.open('image.png').convert('RGB')
out = Image.new('RGB', image.size)

for j in range(9):
    for i in range(9):
      img_cell = image.crop((i * 50, j * 50, i * 50 + 50, j * 50 + 50))
      c = (int(s[j * 9 + i]) - 1) * 50
      out.paste(img_cell, (c, j * 50))

out.save('out_image.png')
