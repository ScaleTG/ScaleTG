from modules.auth import Auth
from config import bot_username
from modules.core import Response

DEFINED_COMMANDS = [
    'addauth',
    'removeauth',
    'isauth',
    'listauth',
]
def process(u):
    """ An app for managing authorization through the bot itself. """

    # Message-only processor
    if u.type != 'message':
        return
    msg = u.message
    # Text-message-only processor
    if msg.text is None:
        return
    # Command-only processor
    if msg.text[0] != '/':
        return
    # Ignore messages not directed at our bot
    if '@' in msg.text and not msg.text.endswith('@' + bot_username):
        return
    elif '@' in msg.text:
        msg.text = msg.text.replace('@' + bot_username, '')
    # Defined commands only
    if msg.text[1:].split(' ')[0] not in DEFINED_COMMANDS:
        return
    
    # Authorized-user only
    if not Auth().isAuthorized(msg.sender.id):
        return msg.respond('You are not authorized to do that!')
    
    # Attach user id 
    if msg.reply_to_message is not None and len(msg.text.split(' ')) == 1:
        msg.text += ' {}'.format(msg.reply_to_message.sender.id)
    # Add Authorized Member
    if msg.text.startswith('/addauth'):
        text = msg.text.split(' ')
        # Usage /addauth <user_id>
        if len(text) == 2:
            if not text[1].isdigit():
                return msg.respond('Only user ids and replies are supported as of now.')
            else:
                Auth().addAuthorized(int(text[1]))
                return msg.respond('Added `{}` to authorized members.'.format(text[1]), parse_mode='markdown')
        else:
            return msg.respond('Invalid command, usage: `/addauth <user id>`', parse_mode='markdown')
    elif msg.text.startswith('/removeauth'):
        text = msg.text.split(' ')
        # Usage /removeauth <user_id>
        if len(text) == 2:
            if not text[1].isdigit():
                return msg.respond('Only user ids and replies are supported as of now.')
            else:
                Auth().removeAuthorized(int(text[1]))
                return msg.respond('Removed `{}` from authorized members.'.format(text[1]), parse_mode='markdown')
        else:
            return msg.respond('Invalid command, usage: `/removeauth <user id>`', parse_mode='markdown')
    elif msg.text.startswith('/isauth'):
        text = msg.text.split(' ')
        # Usage /isauth <user_id>
        if len(text) == 2:
            if not text[1].isdigit():
                return msg.respond('Only user ids and replies are supported as of now.')
            else:
                is_auth = Auth().isAuthorized(int(text[1]))
                if is_auth:
                    return msg.respond('User with ID `{}` is authorized.'.format(text[1]), parse_mode='markdown')
                else:
                    return msg.respond('User with ID `{}` is not authorized.'.format(text[1]), parse_mode='markdown')
        else:
            return msg.respond('Invalid command, usage: `/isauth <user id>`', parse_mode='markdown')
    elif msg.text.startswith('/listauth'):
        text = 'All authorized members are listed below:\n```\n'
        authorized = Auth().getAllAuthorized()
        for member in authorized:
            text += '{}\n'.format(member)
        text += '```'
        return msg.respond(text, parse_mode='markdown')