import classes as cl
import json
author="jajaio"
def load_game():
    with open('player.json', 'r') as pfile:
        j=json.load(pfile)
        cl.Player.hp=j['hp']
        cl.Player.agi=j['agi']
        cl.Player.deff=j['deff']
        cl.Player.att=j['att']
        cl.Player.mp=j['mp']
        cl.Player.xp=j['xp']
        cl.Player.name=j['name']
        cl.Player.lvl=j['lvl']
        cl.Player.dragon=j['dragon']
        cl.Player.xpreq=j['xpreq']
        cl.Player.skulls=j['skulls']
        cl.Player.wname=j['wname']
        cl.Player.bcomp=j['bcomp']
        cl.Player.ecomp=j['ecomp']
        cl.Player.dcomp=j['dcomp']
if __name__=='__main__':
    load_game()
    cl.show_player()
