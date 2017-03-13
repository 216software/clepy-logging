# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import logging
import logging.config

import clepylogconfig

log = logging.getLogger("clepy")

def f():
	return g()

def g():
	return h()

def h():
	1/0

if __name__ == "__main__":

	# THIS IS WHERE THE CONFIGURATION HAPPENS!
	logging.config.dictConfig(clepylogconfig.LOGGING)

	log.debug("DEBUG!")
	log.info("INFO!")
	log.warn("WARN!")
	log.error("ERROR!")
	log.critical("CRITICAL!")

	try:
		f()
	except Exception as ex:
		log.exception("OH NOES")

	log.info("All done!")
