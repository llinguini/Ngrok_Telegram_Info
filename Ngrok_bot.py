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
bot = botogram.create("1185600306:AAGBGVetBBb4qD_p_akhf-kAwynR_Ysdj7U")
tunnels = ngrok.get_tunnels()
ngrok.set_auth_token("1ngAAGJIWhNSGkJpp8ObYEFgO6u_mVmd3GxYMFPTGSHxUUJZ")

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
