import sys
from optparse import make_option
from sys import stdout
from time import sleep

from django.core.management import BaseCommand
from ...decorators import task


@task
def echo_test(message):
    """
    Prints out the message to stdout
    """
    stdout.write("[Received] %s\n" % message)
    stdout.flush()


class Command(BaseCommand):
    """
    A management command that sends an echo test to the background tasker

    You can provide a custom message and optionally increase the count or modify the delay
    between successive messages
    """
    option_list = BaseCommand.option_list + (
        make_option('--count', dest='count', default=100,
                    help='The total number of messages to send.'),
        make_option('--delay', dest='delay', default=0.2, type="float",
                    help='The number of seconds to sleep between each message.'),
    )
    args = 'message'
    help = 'Sends a simple echo test to the background worker'

    def handle(self, message='Hello World', count=100, delay=0.2, **kwargs):
        try:
            for increment in xrange(0, count):
                self.stdout.write('Sending message %s of %s: %s' % (increment + 1, count, message))
                echo_test.async(message)
                sleep(delay)
        except KeyboardInterrupt:
            self.stderr.write("Stopping echo test")
            sys.exit(1)
