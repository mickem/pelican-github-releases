#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals, print_function

import logging
import os
import re
import requests
import json

from blinker import signal

from pelican import signals
from pelican import generators
from pelican.utils import mkdir_p

logger = logging.getLogger(__name__)

def sizeof_fmt(num):
    for unit in ['','Kb','Mb','Gb','Tb','Pb','Eb','Zb']:
        if abs(num) < 1024.0:
            return "%3.1f%s" % (num, unit)
        num /= 1024.0
    return "%.1f%s" % (num, 'Yi')

class GitHubReleaseGenerator(generators.Generator):

    def __init__(self, *args, **kwargs):
        super(GitHubReleaseGenerator, self).__init__(*args, **kwargs)
        signals.static_generator_init.send(self)
        self.releases = []

    def generate_context(self):
        self.releases = ['0.4.4.1', '0.4.4.2', '0.4.3.4']
        self._update_context(('releases', ))
        self.versions = self.settings.get("GITHUB_MAJOR_VERSIONS", [])
        self.promoted_release = self.settings.get("GITHUB_PROMOTED_VERSION", '')
        self.template = self.settings.get("GITHUB_TEMPLATE", 'release')
        self.promoted_template = self.settings.get("GITHUB_PROMOTED_TEMPLATE", 'promoted-release')
        self.save_as = self.settings.get("GITHUB_RELEASE_SAVE_AS", 'release.html')
        self.promoted_save_as = self.settings.get("GITHUB_RELEASE_PROMOTED_SAVE_AS", 'promoted-release.html')
        
        self.env.filters.update({'sizeformat': sizeof_fmt})
        
        
        
        r = requests.get(self.settings.get("GITHUB_RELEASE_URL", 'https://api.github.com/repos/mickem/nscp/releases'))
        r.encoding = 'utf8'
        if(r.ok):
            self.releases = json.loads(r.text or r.content)
        
        signals.static_generator_finalized.send(self)

    def generate_output(self, writer):
        for rel in self.releases:
            if rel['name'] == self.promoted_release:
                logger.info("Found promoted release: %s"%rel['name'])
                writer.write_file(self.promoted_save_as, self.get_template(self.promoted_template),
                    self.context, release=rel,
                    relative_urls=self.settings['RELATIVE_URLS'])
        for base_version in self.versions:
            releases = []
            for rel in self.releases:
                if rel['name'].startswith(base_version):
                    releases.append(rel)

            logger.debug("Creating release: %s"%base_version)
            writer.write_file(self.save_as.replace('{version}', base_version), self.get_template(self.template),
                self.context, releases=releases, version=base_version,
                relative_urls=self.settings['RELATIVE_URLS'])
        signals.page_writer_finalized.send(self, writer=writer)

def get_generators(_):
    return GitHubReleaseGenerator

def register():
    signals.get_generators.connect(get_generators)
1