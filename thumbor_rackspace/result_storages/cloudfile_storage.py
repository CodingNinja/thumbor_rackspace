#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 theiconic.com.au development@theiconic.com.au

from datetime import datetime
from uuid import uuid4
from shutil import move

from os.path import exists, dirname, join, getmtime, expanduser

from thumbor.result_storages import BaseStorage
from thumbor.utils import logger
import pyrax

class Storage(BaseStorage):
    def __init__(self, context):
        self.context = context
        if(self.context.config.RACKSPACE_PYRAX_REGION):
            pyrax.set_default_region(self.context.config.RACKSPACE_PYRAX_REGION)

        pyrax.set_credential_file(expanduser(self.context.config.RACKSPACE_PYRAX_CFG))

        self.cloudfiles = pyrax.connect_to_cloudfiles(public=self.context.config.RACKSPACE_PYRAX_PUBLIC)


    @property
    def is_auto_webp(self):
        return self.context.config.AUTO_WEBP and self.context.request.accepts_webp

    def put(self, bytes):
        cf = self.cloudfiles
        cont = cf.get_container(self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER)
        file_abspath = self.normalize_path(self.context.request.url)
        obj = cont.store_object(file_abspath, bytes)
        logger.debug("[RESULT_STORAGE] putting in %s/%s" % (self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER, file_abspath))
        if(self.context.config.RACKSPACE_RESULT_STORAGE_EXPIRES):
            cont.delete_object_in_seconds(obj=obj,seconds=str(self.context.config.RESULT_STORAGE_EXPIRATION_SECONDS))


    def get(self):
        cf = self.cloudfiles
        cont = cf.get_container(self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER)
        file_abspath = self.normalize_path(self.context.request.url)
        try:
            logger.debug("[RESULT_STORAGE] getting from %s/%s" % (self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER, file_abspath))
            obj = cont.get_object(file_abspath)
            if obj:
                logger.debug("[RESULT_STORAGE] Found object at %s/%s" % (self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER, file_abspath))
                if(self.context.config.RACKSPACE_RESULT_STORAGE_EXPIRES):
                    cont.delete_object_in_seconds(obj=obj,seconds=str(self.context.config.RESULT_STORAGE_EXPIRATION_SECONDS))

                return obj.get()
            else:
                logger.warning("[RESULT_STORAGE] Unable to find object %s/%s" % (self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER, file_abspath ))
        except:
            return None
        return None



    def normalize_path(self, path):
        if self.is_auto_webp:
            path = join(self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER_ROOT.rstrip('/'), path.lstrip('/'))
        else:
            path = join(self.context.config.RACKSPACE_RESULT_STORAGES_CONTAINER_ROOT.rstrip('/'), "webp", path.lstrip('/'))

        path = path.replace('http://', '')
        return path
