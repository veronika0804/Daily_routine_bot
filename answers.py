from event import Event

hello_string = \
'''Здравствуйте, дорогой друг! Я - ваш личный помощник!
Вы можешь составить себе расписание дня, а я буду вам переодически напоминать 
соблюдать его. Команды по составлению можно посмотреть, введя "/help"'''
help_string = \
'''/start - приветствие;
/show_events - посмотреть расписание;
/add_event - добавить пункт в распорядок;
/del_event - удалить пункт из распорядка;
/edit_event - изменить пункт в распорядке;
/help - список команд.'''

show_events = \
'''Ниже представлен весь распорядок дня:'''
show_nothing = \
'''Вы пока не внесли мероприятия в свой распорядок. Вы можете сделать это командой /add_event'''

insert_string = \
'''Добавить новую запись в расписание...'''
ask_event = \
'''Введите название мероприятия:'''
ask_time = \
'''Введите время мероприятия в формате <hh:mm-hh:mm> :'''
entered_time_error = \
'''Строка не соответствует требуемому формату. Попробуйте ещё раз'''

event_added = \
'''Отлично! Строка успешно добавлена!'''
del_string = \
'''Удалим запись из вашего расписания...'''
ask_del_number = \
'''Введите порядковый номер мероприятия на удаление:'''
event_deleted = \
'''Мероприятие успешно удалено из распорядка дня'''

edit_string = \
'''Изменить запись в распорядке...'''
ask_edit_number = \
'''Введите порядковый номер мероприятия для изменения:'''
ask_edit_name = \
'''Введи новое название мероприятия:'''

def make_event_message(event_list):
    result = '\n'.join(event.name for event in event_list)
    return result