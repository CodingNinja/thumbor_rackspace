Thumbor Rackspace Adapters
=================

Provides a Thumbor result storage adapter for Rackscpace that stores files in Rackspace

A simple configuration involves adding the following configuration:

RESULT_STORAGE = 'thumbor_rackspace.result_storages.cloudfile_storage' # Use the cloud file adapter

RACKSPACE_PYRAX_CFG = /var/thumbor/.pyrax.cfg # The Pyrax rackspace configuration file location
RACKSPACE_RESULT_STORAGE_EXPIRES = True # Set TTL on cloudfile objects
RACKSPACE_RESULT_STORAGES_CONTAINER = "cloudfile-container-name"
RACKSPACE_RESULT_STORAGES_CONTAINER_ROOT = "/"
