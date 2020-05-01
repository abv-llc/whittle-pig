#!/bin/bash

export PKG_DIR="python"

rm -rf ${PKG_DIR} && mkdir -p ${PKG_DIR}

docker run --rm -v $(pwd):/lambda-src -w /lambda-src lambci/lambda:build-python3.7 \
    pip install -r requirements.txt --no-deps -t ${PKG_DIR}
