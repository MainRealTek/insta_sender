from protocol import INSTA_SENDER_DM
from os import name,system
from colorama import Fore,Back,Style
from sys import argv
from time import sleep

banner = """
▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌               ▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
     ▐░▌     ▐░▌ ▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌▐░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░▌ ▀▀▀▀▀▀█░▌      ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌       ▐░▌               ▐░▌▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
 ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌      ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                             
"""



def p_green(string):
    print(Fore.GREEN+Style.BRIGHT+string+Fore.RESET+Style.RESET_ALL)

def p_red(string):
    print(Fore.RED+Style.BRIGHT+string+Fore.RESET+Style.RESET_ALL)

def clear(self):
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)


def main():
    print(banner)
    try:
        p_green(banner)
        p_green('\nwhith proxy\nExample : python username password target-nick user-proxy password-proxy hub-ip-proxy port message\n\n')
        try:
            if len(argv) == int(9):
                user_p, password_p, target_nick , user_proxy , password_proxy , ip_hub_proxy , port_proxy, msg_text =argv[1],argv[2],argv[3],argv[4],argv[5],argv[6],argv[7],argv[8]
                ig = INSTA_SENDER_DM(username=str(user_p),password=str(password_p),
                                        target_user=str(target_nick),proxy=True,
                                        user_p=str(user_proxy),pasw_p=str(password_proxy),
                                        ip_p=str(ip_hub_proxy),port_p=int(port_proxy))
                result = ig.main_send_dm(dm_message=msg_text)
                if result is True:
                    p_green('Message Sent with succes to {}'.format(target_nick))
                else:
                    p_red('Something wrong')
                    exit()
        except IndexError:
            pass

    except Exception as i:
        print(i)
        pass


if __name__ == '__main__':
    main()

