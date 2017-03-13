# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import logging
import logging.config

import boto

import clepylogconfig

log = logging.getLogger("clepy")

if __name__ == "__main__":

	logging.config.dictConfig(clepylogconfig.LOGGING)

	log.debug("Trying to access Amazon S3 with obviously bad credentials...")

	# These are obviously bad credentials
	s3conn = boto.connect_s3("abc", "def")

	# This is gonna blow up...
	all_buckets = s3conn.get_all_buckets()

	log.info("All done!")

