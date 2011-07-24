from django.views.debug import ExceptionReporter
from django.conf import settings
import sys
import datetime

class PedanticLogging(object):
    def process_exception(self, request, exception):
        e = sys.exc_info()                               
        reporter = ExceptionReporter(request, *e)
        log = open(settings.PEDANTIC_LOG_DIR+str(datetime.datetime.now())+'.html', 'w')
        log.write(reporter.get_traceback_html())
        log.close()
        return None