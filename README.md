Thumbor Rackspace Adapters
==========================

Provides a [Thumbor](https://github.com/globocom/thumbor) result storage adapter for Rackscpace that stores files in Rackspace.

Installing
----------

Thumbor-Rackspace can be easily installed using `pip install thumbor_rackspace`.

Configuration
-------------

# Use rackspace for result storage.
# For more info on result storage: https://github.com/globocom/thumbor/wiki/Result-storage
RESULT_STORAGE = 'thumbor_rackspace.result_storages.cloudfile_storage'

# Pyrax Rackspace configuration file location
RACKSPACE_PYRAX_CFG = /var/thumbor/.pyrax.cfg

# Result Storage options
RACKSPACE_RESULT_STORAGE_EXPIRES = True # Set TTL on cloudfile objects
RACKSPACE_RESULT_STORAGES_CONTAINER = "cloudfile-container-name"
RACKSPACE_RESULT_STORAGES_CONTAINER_ROOT = "/"

## Since v.3
RACKSPACE_PYRAX_REGION = SYD
RACKSPACE_PYRAX_PUBLIC = True
