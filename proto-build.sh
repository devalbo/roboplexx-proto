#!/bin/sh
cd proto
protoc rpx.common.proto rpx.descriptions.proto rpx.configurations.proto rpx.commands.proto --python_out=../rpx_proto