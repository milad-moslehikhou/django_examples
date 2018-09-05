from channels import Group


def ws_connect(message):
    Group('clients').add(message.reply_channel)


def ws_disconnect(message):
    Group('clients').discard(message.reply_channel)
