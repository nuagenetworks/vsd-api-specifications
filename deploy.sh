#!/bin/bash

set -x
set -e

WORKSPACE=$(pwd)

function fetch_all_branches()
{
    # Keep track of where Travis put us.
    # We are on a detached head, and we need to be able to go back to it.
    XXX_BUILD_HEAD=$(git rev-parse HEAD)

    # Go back to the branch from which the detached head is from.
    git checkout -
    # Keep track of that branch
    XXX_BUILD_BRANCH=$(git rev-parse --abbrev-ref HEAD)

    # Fetch all the remote branches. Travis clones with `--depth`, which
    # implies `--single-branch`, so we need to overwrite remote.origin.fetch to
    # do that. See also http://stackoverflow.com/a/20338558/1836144
    git config --replace-all remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
    git fetch
    git fetch --tags

    # Track the remote branches, because monolithe only handles tracking branches.
    for branch in $(git branch -r|grep -v HEAD) ; do
        git checkout ${branch#origin/}
    done
}

function generate_sdk()
{
    local language=${1}
    local version=${2}

    # for Python and HTML, we want to generate SDKs from multiple branches
    if [ "${language}" == "python" -o "${language}" == "html" ] ; then
        case ${version} in
            5.0.*) local branches="master 4.0" ;;
            4.0.*) local branches="4.0 3.2" ;;
            3.2.*) local branches="3.2" ;;
            *)
                >&2 echo "Unexpected version number \"${version}\". Cannot chose which branche(s) to build."
                exit 1
                ;;
        esac
    else
        local branches="${ACTUAL_BRANCH}"
    fi
    branches=$(echo $branches | sed s/"${XXX_BUILD_BRANCH}"/"${XXX_BUILD_HEAD}"/g)

    generate-vspk \
        --generation-version ${version} \
        -b ${branches} \
        -f . \
        -L ${language}
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
    local last_tag=$(git describe --tags --abbrev=0)
    # tags look  like r4.0.6.1, we make the version 4.0.6.1
    local version=${last_tag:1}

    fetch_all_branches
    install_vspkgenerator

    for language in ${languages} ; do
        generate_sdk ${language} ${version}
        if [[ ${TRAVIS_PULL_REQUEST} == "false" ]] ; then
            update_repo ${language}
        fi
    done
    exit 0
}

# For builds triggered by a tagged commit, travis sets TRAVIS_BRANCH to the tag
# whereas we really need the branch name. See:
# https://github.com/travis-ci/travis-ci/issues/4745
if [ -n "${TRAVIS_TAG}" ] ; then
    case "${TRAVIS_TAG}" in
        r3.2*) ACTUAL_BRANCH=3.2 ;;
        r4.0*) ACTUAL_BRANCH=4.0 ;;
        r5.0*) ACTUAL_BRANCH=master ;;
        *)     echo "Invalid tag ${TRAVIS_TAG}" >&2 ; exit 1 ;;
    esac
else
    ACTUAL_BRANCH=${TRAVIS_BRANCH}
fi

main
