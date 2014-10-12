#!/usr/bin/env python2
import json
import os

class Config(object):
    PATHNAME = os.path.join(os.getenv('HOME'), '.homekeeper.json')
    DEFAULTS = {
        'base': None,
        'directory': os.path.join(os.getenv('HOME'), 'dotfiles'),
        'excludes': ['.git', '.gitignore', 'LICENSE', 'README.md'],
        'override': False
    }

    def __init__(self, pathname=None):
        self.data = self.DEFAULTS
        self.pathname = pathname or self.PATHNAME
        if os.path.exists(self.pathname):
            try:
                print 'found homekeeper configuration at %s' % self.pathname
                self.data = json.loads(open(self.pathname).read())
            except ValueError:
                print 'homekeeper configuration invalid; assuming defaults'
        else:
            print 'homekeeper configuration not found; assuming defaults'
        if 'dotfiles_directory' in self.data:
            self.data['directory'] = self.data['dotfiles_directory']
            del self.data['dotfiles_directory']

    def save(self):
        with open(self.pathname) as cfile:
            cfile.write(json.dumps(self.data))

    @property
    def base(self):
        return self.data.get('base', self.DEFAULTS['base'])

    @property
    def excludes(self):
        return self.data.get('excludes', self.DEFAULTS['excludes'])

    @property
    def override(self):
        return self.data.get('override', self.DEFAULTS['override'])

    @property
    def directory(self):
        return self.data.get('directory', self.DEFAULTS['directory'])

