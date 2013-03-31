#!/bin/sh
cd proto
protoc common.proto descriptions.proto tasktypes.proto rpx.proto --python_out=../rpx_proto