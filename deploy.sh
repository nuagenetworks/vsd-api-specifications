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

    git clone ${github_url} ${repo} -b ${TRAVIS_BRANCH}

    rm -rf ${repo}/*
    mv ${codegen}/* ${repo}
    cd ${repo}

    git add .
    git commit -m "Auto generated from specifications change."
    if [ -n "${TRAVIS_TAG}" ] ; then
        git tag -a ${TRAVIS_TAG} -m "Auto generated tag from specifications"
    fi
    git push --tags origin ${TRAVIS_BRANCH}
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
    local languages="python go java objj html"

    install_vspkgenerator
    for language in ${languages} ; do
        generate_sdk ${language}
        if [[ ${TRAVIS_PULL_REQUEST} == "false" ]] ; then
            update_repo ${language}
        fi
    done
    exit 0
}

main
