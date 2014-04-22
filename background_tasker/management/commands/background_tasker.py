import logging
import sys

import zmq
from zmq.eventloop import ioloop
from django.core.management import BaseCommand
from ...context import context
from ...conf import settings


class Command(BaseCommand):
    """
    The management command to start the background tasker worker
    """
    args = ''
    help = 'Start the zero task server'
    logger = logging.getLogger('background_worker')

    def handle(self, **options):

        puller = context.socket(zmq.PULL)
        puller.bind(settings.BACKGROUND_TASKER_URL)

        def _callback(socket, *args, **kwargs):
            try:
                func, args, kwargs = socket.recv_pyobj()
                func(*args, **kwargs)
            except Exception, e:
                self.logger.exception(u'Error in calling function: %s' % e)

        loop = ioloop.IOLoop.instance()
        loop.add_handler(puller, _callback, loop.READ)

        try:
            loop.start()
        except KeyboardInterrupt:
            self.logger.info("Stopping background tasker worker")
            loop.stop()
            sys.exit(1)
