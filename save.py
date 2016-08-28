import json
import letters as le

def save():
    with open('letters.json', 'w') as pfile:
        pfile.write(json.dumps({
            "a":le.Letter.a,
            "b":le.Letter.b,
            "c":le.Letter.c,
            "d":le.Letter.d,
            "e":le.Letter.e,
            "f":le.Letter.f,
            "g":le.Letter.g,
            "h":le.Letter.h,
            "i":le.Letter.i,
            "j":le.Letter.j,
            "k":le.Letter.k,
            "l":le.Letter.l,
            "m":le.Letter.m,
            "n":le.Letter.n,
            "o":le.Letter.o,
            "p":le.Letter.p,
            "q":le.Letter.q,
            "r":le.Letter.r,
            "s":le.Letter.s,
            "t":le.Letter.t,
            "u":le.Letter.u,
            "v":le.Letter.v,
            "w":le.Letter.w,
            "x":le.Letter.x,
            "y":le.Letter.y,
            "z":le.Letter.z,
            " ":le.Letter.space,
            "?":le.Letter.question,
            "!":le.Letter.exclamation
            }))
        
if __name__=='__main__':
    save()
