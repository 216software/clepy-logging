# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

LOGGING = {

    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': "ERROR",
        'handlers': ['console', "tmpfile"],
    },

    'formatters': {
        'basic': {
            'format': "%(asctime)-22s [%(process)d] %(name)-30s %(lineno)-5d %(levelname)-8s %(message)s",
        },

        'colorfmt': {
            'format': "%(log_color)s%(asctime)-22s [%(process)d] %(name)-30s %(lineno)-5d %(levelname)-8s %(message)s",
            '()': "colorlog.ColoredFormatter"
        },
    },

    'handlers': {

        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'colorfmt',
            # 'level': 'DEBUG',
        },

        "tmpfile": {
            "class":"logging.FileHandler",
            "formatter": "basic",
            "level": "DEBUG",
            "filename": "/tmp/clepy.log",
            "mode": "a",
        },
    },
    'loggers': {

		"clepy": {
			"handlers": ["console", "tmpfile"],
			"level": "DEBUG",
			"propagate": False
		},

        "boto": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },

    },

}

