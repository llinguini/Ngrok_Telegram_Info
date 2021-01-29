#############################################################
#                                                           #
#                  Ngrok Status Link in Telegram            #
#                  Code by linguini                         #
#                  www.linguinielruso.com                   #
#                  @linguini (telegram and twitter)         #
#                                                           #
#############################################################
import botogram
from pyngrok import ngrok
bot = botogram.create("TU TOKEN DEL BOT")
tunnels = ngrok.get_tunnels()
ngrok.set_auth_token("TU TOKEN DE NGROK (dejar en blanco para no usar)")

#Custome ports for ngrok  (port, udp/tcp/HTML)
ssh_tunnel = ngrok.connect(21, "tcp")
vnc_tunnel = ngrok.connect(5200, "tcp")


tunnel_status = ' '.join([str(elem) for elem in ngrok.get_tunnels()]) 
  
@bot.command("status")
def tunerl_send(chat, message, args):
    chat.send("Done")
    chat.send(tunnel_status)
       
if __name__ == "__main__":
    bot.run()
