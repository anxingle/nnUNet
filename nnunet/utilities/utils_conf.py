# coding: utf-8
import yaml
import socket
import logging
import logging.config


if len(logging.getLogger().handlers) == 0:
	logging.basicConfig(level=logging.DEBUG)

class ConfigLoader(object):
	def __init__(self, config_path=None, mode="offline_logging"):
		super(ConfigLoader, self).__init__()
		# self._config_path = config_path or self._absolute_path('../../conf/config.yaml')
		self._config_path = config_path
		self._load()
		# self._check_dir()
		try:
			logging.config.dictConfig(self._conf[mode])
		except Exception as e:
			print("exception occur！")
			print(e)
			pass

	def _load(self):
		with open(self._config_path, 'rb') as f:
			self._conf = yaml.load(f)

	@property
	def conf(self):
		return self._conf
