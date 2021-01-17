
import sendMessage
import user

try:
    sendMessage.login()
    i = 0
    while i < len(user.attackUsers):
        sendMessage.sendMassage(user.attackUsers[i], user.sms, 1)
        i = i+1

except Exception as ex:
    print(ex)
finally:
    sendMessage.close()



