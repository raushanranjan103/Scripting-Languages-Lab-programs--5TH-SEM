AtomicDictionary = {'Na':'Sodium' , 'Cr':'Chromium' , 'Kr':'Krypton'}

def atomic_dictionary():

    flag = True

    print('1. Insert Atomic Element')
    print('2. Display Elements')
    print('3. Search Elements')
    print('4. Exit')

    while True:
        x = (int)(input('Enter your choice : '))

        if x == 1:
            Atname = input('Enter Element Name : ')
            Atsymb = input('Enter Element Symbol : ')
            AtomicDictionary[Atsymb] = Atname

        elif x == 2:
            print(AtomicDictionary)

        elif x == 3:
            srh = input('Enter Search Element Name : ')
            if srh in AtomicDictionary.values():
                print('Element Found.')
            else:
                print('Element not found.')

        elif x == 4:
            break;

        else:
            print('Invalid Input')
            
