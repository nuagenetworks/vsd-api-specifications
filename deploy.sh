#!/bin/bash

set -x
set -e

WORKSPACE=$(pwd)

function generate_sdk()
{
    local language=${1}
    generate-vspk -f . -L ${language}
}

function update_repo()
{
    local language=${1}
    local codegen=${WORKSPACE}/codegen/${language}
    if [ ${language} == "html" ] ; then
        local repo=${WORKSPACE}/vsd-api-documentation
        local github_url=git@github.com:nuagenetworks/vsd-api-documentation.git
    else
        local repo=${WORKSPACE}/vspk-${language}
        local github_url=git@github.com:nuagenetworks/vspk-${language}.git
    fi

    git clone ${github_url} ${repo} -b ${ACTUAL_BRANCH}

    rm -rf ${repo}/*
    mv ${codegen}/* ${repo}
    cd ${repo}

    git add --all .
    # commit fails if nothing changed, which causes the script to exit.
    # to avoid this, we force this line to be always successful.
    git commit -m "Auto generated from specifications change." || true
    if [ -n "${TRAVIS_TAG}" ] ; then
        git tag -a ${TRAVIS_TAG} -m "Auto generated tag from specifications"
    fi
    git push --tags origin ${ACTUAL_BRANCH}
    cd ${WORKSPACE}
}

function install_vspkgenerator()
{
    pip install -U git+https://github.com/nuagenetworks/monolithe.git
    pip install -U git+https://github.com/nuagenetworks/vspkgenerator.git
}


function main()
{
    local language=
    local languages="python go java objj html vro"

    install_vspkgenerator
    for language in ${languages} ; do
        generate_sdk ${language}
        if [[ ${TRAVIS_PULL_REQUEST} == "false" ]] ; then
            update_repo ${language}
        fi
    done
    exit 0
}

# For builds triggered by a tag, travis set TRAVIS_BRANCH to the tag whereas we
# really need the branch name. See:
# https://github.com/travis-ci/travis-ci/issues/4745
#
# For now the logic is simple since we only build for master, but we'll need to
# update this for releases based on other branches.
if [ -n "${TRAVIS_TAG}" ] ; then
    ACTUAL_BRANCH=master
else
    ACTUAL_BRANCH=${TRAVIS_BRANCH}
fi
main
