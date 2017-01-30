#!/usr/bin/env python

from distutils.core import setup

setup(name='plantgateway',
      version='0.1.0',
      description='Bluetooth to mqtt gateway for Xiaomi Mi plant sensors',
      author='Christian Kühnel',
      author_email='christian.kuehnel@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['plantgw'],
      requires=['miflora', 'paho-mqtt', 'pyyaml'],
      scripts=['plantgw/plantgateway'],
      )