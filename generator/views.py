from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, "generator/home.html")


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {'password':thepassword})



def about(request):
    return render(request, "generator/about.html")


def cipher(request):
    # Implementation of Affine Cipher in Python

    key = [17,20]

    def egcd(a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y

    def modinv(a, m):
        gcd, x, y = egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m


    # affine cipher encrytion function
    # returns the cipher text
    def affine_encrypt(thetext, key):
        '''
        C = (a*P + b) % 26
        '''
        return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                      + ord('A')) for t in thetext.upper().replace(' ', '') ])


    # affine cipher decryption function
    # returns original text
    def affine_decrypt(cipher, key):
        '''
        P = (a^-1 * (C - b)) % 26
        '''
        return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                        % 26) + ord('A')) for c in cipher ])


    # Driver Code to test the above functions
    def main():
        # declaring text and key

        #text = 'text'#input('Print your text: ')
        #key = [17,20]

        # calling encryption function
        #affine_encrypted_text = affine_encrypt(thetext, key)

        print('Encrypted Text: {}'.format( affine_encrypted_text ))

        # calling decryption function
        print('Decrypted Text: {}'.format
        ( affine_decrypt(affine_encrypted_text, key) ))



    if __name__ == '__main__':
        main()

    thetext= str(request.GET.get('thetext'))

    affine_encrypted_text = affine_encrypt(thetext, key)


    return render(request, "generator/cipher.html", {'cipher': affine_encrypted_text})
    return render(request, "generator/home.html", {'text': thetext})

def decrypted(request):

    return render(request, "generator/decrypted.html", {'text': thetext})
