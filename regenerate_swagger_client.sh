#!/bin/sh
# ref: https://github.com/swagger-api/swagger-codegen/blob/master/README.md
#
# pre-requisite: ensure swagger-codegen is installed (on Mac, brew install swagger-codegen)

swagger-codegen generate -i https://assets.zuora.com/zuora-documentation/swagger-codegen-workaround.yaml -l python -c config.json

