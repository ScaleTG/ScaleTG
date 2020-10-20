from datetime import datetime
import inspect
from flask import jsonify
from json import dumps

# Misc functions 
def unixToDatetime(unix_date):
    return datetime.fromtimestamp(unix_date)

# Classes
class Response:
    def __init__(self, method):
        self.method = method
    
    def getResponse(self, attach_method=True, flask_response=True, dump=False):
        # Making sure the defaults are always set
        if attach_method is None:
            attach_method = True
        if flask_response is None:
            flask_response = True
        if dump is None:
            dump = False
        
        raw_attributes = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        attributes = [a for a in raw_attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        result = dict(attributes)

        result = {k: v for k, v in result.items() if v is not None}
        result.pop('getResponse', None)
        if attach_method:
            result['method'] = self.method
        if flask_response:
            result = jsonify(result)
        elif dump:
            result = dumps(result)
        return result

class TelegramObject:
    def __init__(self, telegramDict, parameters):
        self._obj = telegramDict
        name = 0
        required = 1
        c = 2
        for parameter in parameters:
            # Compatiblity
            if len(parameter) == 1:
                parameter.append(False)
            # Cases:
            # Not present (Required / Not Required)
            if parameter[name] not in self._obj:
                if parameter[required]:
                    raise ValueError(parameter[0] + ' is required but not provided')
                else:
                    setattr(self, parameter[name], None)
            # Present and no class
            elif len(parameter) == 2:
                setattr(self, parameter[name], self._obj[parameter[name]])
            # Present and has class
            else:
                setattr(self, parameter[name], parameter[c](self._obj[parameter[name]]))
class Update(TelegramObject):
    def __init__(self, telegramDict):
        super().__init__(telegramDict, [
            ['update_id', True],
            ['message', False, Message],
            ['edited_message', False, Message],
            ['channel_post', False, Message],
            ['edited_channel_post', False, Message],
            ['inline_query', False,],
            ['chosen_inline_result', False],
            ['callback_query', False],
            ['shipping_query', False],
            ['pre_checkout_query', False],
            ['poll', False],
            ['poll_answer', False],
        ])
        self.id = self.update_id

        # Setting type
        for k in telegramDict:
            if k != 'update_id':
                self.type = k
class User(TelegramObject):
    def __init__(self, telegramDict):
        super().__init__(telegramDict, [
           #[param_name, required (optional), class (optional) ]
           ['id', True],
           ['is_bot', True],
           ['first_name', True],
           ['last_Name', False],
           ['username', False],
           ['language_code', False],
           ['can_join_groups', False],
           ['can_read_all_group_messages', False],
           ['supports_inline_queries', False]
        ])

class Chat(TelegramObject):
    def __init__(self, telegramDict):
        super().__init__(telegramDict, [
            ['id', True],
            ['type', True],
            ['username', False],
            ['first_name', False],
            ['last_name', False],
            ['photo', False], # Class yet to be created
            ['description', False],
            ['invite_link', False],
            ['pinned_message', False, ], # Class yet to be created
            ['permissions', False, ], # Class yet to be created
            ['slow_mode_delay', False],
            ['sticker_set_name', False],
            ['can_set_sticker_set', False]
        ])

class Message(TelegramObject):
    def __init__(self, telegramDict):
        if 'from' in telegramDict:
            telegramDict['sender'] = telegramDict['from']
            telegramDict.pop('from')
        
        super().__init__(telegramDict, [
            ['message_id', True],
            ['sender', False, User],
            ['date', True, unixToDatetime],
            ['chat', True, Chat],
            ['forward_from', False, User],
            ['forward_from_chat', False, Chat],
            ['forward_from_message_id', False],
            ['foward_signature', False],
            ['forward_sender_name', False],
            ['forward_date', False, unixToDatetime],
            ['reply_to_message', False, Message],
            ['via_bot', False, User],
            ['edit_date', False, unixToDatetime],
            ['media_group_id', False],
            ['author_signature',],
            ['text', ],
            ['entities', ], # Class yet to be developed
            ['animation',],
            ['audio',],
            ['document', ],
            ['photo', ],
            ['sticker', ],
            ['video', ],
            ['video_note', ],
            ['voice', ],
            ['caption', ],
            ['caption_entities', ],
            ['contact', ],
            ['dice', ],
            ['game', ],
            ['poll', ],
            ['venue', ],
            ['location', ],
            ['new_chat_members', ],
            ['left_chat_member', False, User],
            ['new_chat_photo', ],
            ['delete_chat_photo', ],
            ['group_chat_created', ],
            ['supergroup_chat_created', ],
            ['channel_chat_created', ],
            ['migrate_to_chat_id', ],
            ['migrate_from_chat_id', ],
            ['pinned_message', False, Message],
            ['invoice', ],
            ['successful_payment', ],
            ['connected_website', ],
            ['passport_data', ],
            ['reply_markup', ],
        ])
        self.id = self.message_id
        self.respond = self.respondText
    
    def respondText(self, text, reply=True, attach_method=None, flask_response=None, dump=None, **kwargs):
        r = Response('sendMessage')
        r.text = text
        r.chat_id = self.chat.id
        if reply and 'reply_to_message_id' not in kwargs:
            r.reply_to_message_id = self.id
        
        for k, v in kwargs.items():
            setattr(r, k, v)
        return r.getResponse(attach_method, flask_response, dump)
