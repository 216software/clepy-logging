# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import logging
import logging.config
import sys

import clepylogconfig

log = logging.getLogger("clepy")

def f():
	return g()

def g():
	return h()

def h():
	1/0


def log_uncaught_exceptions(ex_cls, ex, tb):

    log.critical(''.join(traceback.format_tb(tb)))
    log.critical('{0}: {1}'.format(ex_cls, ex))

if __name__ == "__main__":

	# THIS IS WHERE THE CONFIGURATION HAPPENS!
	logging.config.dictConfig(clepylogconfig.LOGGING)

	# This line logs uncaught exceptions.  Remind me to talk about this
	# later.
	sys.excepthook = log_uncaught_exceptions

	log.debug("DEBUG!")
	log.info("INFO!")
	log.warn("WARN!")
	log.error("ERROR!")
	log.critical("CRITICAL!")

	try:
		f()
	except Exception as ex:
		log.exception("OH NOES")

	1/0

	log.info("All done!")

