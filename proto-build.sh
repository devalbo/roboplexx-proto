#!/bin/sh
cd proto
protoc common.proto descriptions.proto configurations.proto commands.proto --python_out=../rpx_proto