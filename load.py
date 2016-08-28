import letters as le
import json

def load_game():
    with open('letters.json', 'r') as pfile:
        j=json.load(pfile)
        le.Letters.a=j['a']
        le.Letters.b=j['b']
        le.Letters.c=j['c']
        le.Letters.d=j['d']
        le.Letters.e=j['e']
        le.Letters.f=j['f']
        le.Letters.g=j['g']
        le.Letters.h=j['h']
        le.Letters.i=j['i']
        le.Letters.j=j['j']
        le.Letters.k=j['k']
        le.Letters.l=j['l']
        le.Letters.m=j['m']
        le.Letters.n=j['n']
        le.Letters.o=j['o']
        le.Letters.p=j['p']
        le.Letters.q=j['q']
        le.Letters.r=j['r']
        le.Letters.s=j['s']
        le.Letters.t=j['t']
        le.Letters.u=j['u']
        le.Letters.v=j['v']
        le.Letters.w=j['w']
        le.Letters.x=j['x']
        le.Letters.y=j['y']
        le.Letters.z=j['z']
    #n=0
    #message = input("What is your message? >> ")
    #while n < len(message):
    #    sys.stdout.write(j[message[n]])
    #    n += 1

if __name__=='__main__':
    load_game()
