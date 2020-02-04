from pathlib import Path

from dto import PluralFormsDto, DurationDto, CommandDto


class TelegramChatType:
    SUPER_GROUP = 'supergroup'


class TelegramParseMode:
    MARKDOWN = 'Markdown'
    HTML = 'HTML'


class TelegramMemberStatus:
    CREATOR = 'creator'
    ADMINISTRATOR = 'administrator'
    MEMBER = 'member'
    RESTRICTED = 'restricted'
    LEFT = 'left'
    KICKED = 'kicked'


class LoggingSettings:
    RECORD_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    DEFAULT_LEVEL = 'INFO'


class EnvVar:
    TELEGRAM_TOKEN = 'TELEGRAM_TOKEN'
    TELEGRAM_CHAT_ID = 'TELEGRAM_CHAT_ID'
    LOGGING_LEVEL = 'LOGGING_LEVEL'


class Command:
    RO = CommandDto(bot_command='!ro', text_command='read_only')
    TO = CommandDto(bot_command='!to', text_command='text_only')
    RW = CommandDto(bot_command='!rw', text_command='read_write')
    BAN = CommandDto(bot_command='!ban', text_command='ban_kick')
    PASS = CommandDto(bot_command='!pass', text_command='pass')
    TK = CommandDto(bot_command='', text_command='timeout_kick')
    SR = CommandDto(bot_command='', text_command='unauthorized_punishment')  # Self restrict


class BaseDuration:
    DEFAULT_DURATION = None
    DEFAULT_UNIT = None
    MIN_DURATION = None
    MAX_DURATION = None

    SECONDS_SETTINGS = dict(rate=1, plural_forms=PluralFormsDto(form_1='секунду', form_2='секунды', form_3='секунд'))
    MINUTES_SETTINGS = dict(rate=60, plural_forms=PluralFormsDto(form_1='минуту', form_2='минуты', form_3='минут'))
    HOURS_SETTINGS = dict(rate=3600, plural_forms=PluralFormsDto(form_1='час', form_2='часа', form_3='часов'))
    DAYS_SETTINGS = dict(rate=86400, plural_forms=PluralFormsDto(form_1='день', form_2='дня', form_3='дней'))
    YEARS_SETTINGS = dict(rate=31536000, plural_forms=PluralFormsDto(form_1='год', form_2='года', form_3='лет'))

    UNITS = dict(
        s=SECONDS_SETTINGS,
        m=MINUTES_SETTINGS,
        h=HOURS_SETTINGS,
        d=DAYS_SETTINGS,
        y=YEARS_SETTINGS,
    )


class PunishmentDuration(BaseDuration):
    DURATION = DurationDto(300, '5 минут')


class RestrictDuration(BaseDuration):
    DEFAULT_DURATION = 5
    DEFAULT_UNIT = 'm'

    UNSAFE_DURATION_SECONDS = 40

    MIN_DURATION = DurationDto(5, '5 секунд')
    MAX_DURATION = DurationDto(864000, '10 дней')


class BanDuration(BaseDuration):
    AUTO_KICK_DURATION_SECONDS = 60

    DEFAULT_DURATION = -1
    DEFAULT_UNIT = 's'

    MIN_DURATION = DurationDto(0, 'навсегда')
    MAX_DURATION = DurationDto(315360000, '10 лет')


class MessageSettings:
    SELF_DESTRUCT_TIMEOUT = 5


class NotificationTemplateList:
    READ_ONLY = [
        '{first_name} помещен в read-only на {duration_text}.',
        '{first_name} завалил ебало на {duration_text}.',
        '{first_name} выпил высокий стакан ебалозавалина, которого хватит на {duration_text}.',
        '{first_name} не будет пиздеть ещё {duration_text}.',
        '{first_name} сможет дальше пиздеть только через {duration_text}.',
    ]

    TEXT_ONLY = [
        '{first_name} помещен в text-only на {duration_text}.',
        '{first_name} не будет постить уебанские картиночки {duration_text}.',
    ]

    READ_WRITE = [
        '{first_name} может дальше пиздеть и постить уебанские картиночки.',
        '{first_name} слезает с бутылки.',
    ]

    TIMEOUT_KICK = [
        '{first_name} пиздует из чата, потому что не ответил на вопрос.',
        'Вопрос был довольно простой. {first_name} ведёт себя, как бот.',
        '{first_name} слишком долго тупит. Здесь таких не держат.',
    ]

    BAN_KICK = [
        '{first_name} идёт нахуй из чата {duration_text}.',
    ]

    UNAUTHORIZED_PUNISHMENT = [
        '{first_name} нажал не те кнопки и получает пизды в виде read-only.',
        '{first_name} дохуя о себе думает, поэтому теперь завалит ебало.',
    ]


class GreetingDefaultSettings:
    GREETING_QUESTIONS_FILE: Path = Path('resources/questions.yaml')
    DEFAULT_QUESTION_TEXT = '{mention}, are you ok?'
    DEFAULT_QUESTION_OPTION = 'Yep'
    DEFAULT_QUESTION_REPLY = 'Sure!'
    DEFAULT_QUESTION_TIMEOUT = 120
