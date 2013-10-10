#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 David Mann codingninja@theiconic.com.au

# HBASE STORAGE OPTIONS
from thumbor.config import Config
Config.define('RACKSPACE_PYRAX_CFG', '~/.pyrax.cfg', 'Pyrax configuration file location', 'RESULT_STORAGE')
Config.define('RACKSPACE_PYRAX_REGION', 'SYD', 'Whether to connect to the private rackspace network', 'RESULT_STORAGE')
Config.define('RACKSPACE_PYRAX_PUBLIC', True, 'Whether to connect to the private rackspace network', 'RESULT_STORAGE')
Config.define('RACKSPACE_RESULT_STORAGES_CONTAINER', 'thumbor-test', 'Rackspace cloudfiles container', 'RESULT_STORAGE')
Config.define('RACKSPACE_RESULT_STORAGES_CONTAINER_ROOT', '/products/', 'Root storage path', 'RESULT_STORAGE')
Config.define('RACKSPACE_RESULT_STORAGE_EXPIRES', True, 'Whether to set expires headers on the cloudfiles objects', 'RESULT_STORAGE')
__version__ = "0.3"
