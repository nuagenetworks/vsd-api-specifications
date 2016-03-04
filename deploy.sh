#!/bin/bash

GIT_BRANCH=`git rev-parse --abbrev-ref HEAD`

pip install -U git+https://github.com/nuagenetworks/monolithe.git && \
pip install -U git+https://github.com/nuagenetworks/vspkgenerator.git && \
\
mkdir -p repos && \
cd repos && \
\
git clone git@github.com:nuagenetworks/vspk-python.git -b ${GIT_BRANCH} && \
rm -rf vspk-python/* && \
\
git clone git@github.com:nuagenetworks/vspk-go.git -b ${GIT_BRANCH} && \
rm -rf vspk-go/* && \
\
git clone git@github.com:nuagenetworks/vsd-api-documentation.git -b gh-pages && \
rm -rf vsd-api-documentation/* && \
\
cd .. && \
\
generate-vspk -f . -L python && \
mv codegen/python/* repos/vspk-python && \
cd repos/vspk-python && \
git add --all && \
cd - && \
\
generate-vspk -f . -L go && \
mv codegen/go/* repos/vspk-go && \
cd repos/vspk-go && \
git add --all && \
cd - && \
\
generate-vspk -f . -L html && \
mv codegen/html/* repos/vsd-api-documentation && \
cd repos/vsd-api-documentation && \
git add --all && \
cd -

if [[ $? != 0 ]]; then
    exit 2
fi

cd repos/vspk-python
git commit -a -m "Auto generated from specifications change."
git push origin $GIT_BRANCH
cd -

cd repos/vspk-go
git commit -a -m "Auto generated from specifications change."
git push origin $GIT_BRANCH
cd -

cd repos/vsd-api-documentation
git commit -a -m "Auto generated from specifications change."
git push origin gh-pages
cd -

exit 0
