import os
import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps
check_path='.'
LOG_DIR = os.path.join(check_path, 'log')

file_stream = False
log_path='E:\\chemofang\\Log_book'
if not os.path.exists(log_path):
    os.makedirs(log_path)
    file_stream = True
def get_logger(name='jiekou', file_log=file_stream, level=''):
    """ get logger Factory function """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(log_path, '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)
LOG = get_logger(file_log=file_stream, level='INFO')

def logger(param):
    """ fcuntion from logger meta """
    def wrap(function):
        """ logger wrapper """
        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            LOG.info("当前执行:{}".format(param))
            # LOG.info("全部args参数参数信息 , {}".format(str(args)))
            # LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
            return function(*args, **kwargs)
        return _wrap
    return wrap



@logger('ceshi')
def a_s():

    print('zj')
a_s()