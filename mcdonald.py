from strings import indef

def printverse(animal, sound):
    animal = indef(animal)
    sound = indef(sound)
    print('Old MacDonald had a farm')
    print('E-I-E-I-O')
    print('And on this farm he had', animal)
    print('E-I-E-I-O')
    print('With', sound, sound, 'here')
    print('With', sound, sound, 'there')
    print('Here', sound, 'there', sound)
    print('Everywhere', sound, sound)
    print('Old MacDonald had a farm')
    print('E-I-E-I-O')

def printsong():
    printverse('cow', 'moo')
    printverse('duck', 'quack')
    printverse('horse', 'neigh')
    printverse('pig', 'oink')
    printverse('sheep', 'baa')
    printverse('owl', 'who')

x = 5
x = 2 * x
y = x
x = x - 3

for n in range(4,6):
    print(n)
    print(n*n)
    
printsong()

