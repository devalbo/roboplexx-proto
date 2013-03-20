from distutils.core import setup

setup(
    name='RoboplexxProto',
    version='0.1dev',
    packages=['rpx_proto',],
    license='',
    long_description=open('README.md').read(),
    requires=['protobuf',],
    )