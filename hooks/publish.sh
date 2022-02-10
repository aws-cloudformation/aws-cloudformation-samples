#!/bin/bash

BETA=true
BUCKET=$1
BASE_DIR=$(pwd)
LOG_FILE=/tmp/hookpublisher.log

EXIT_CODE=0
for t in java python; do
  dir="${t}-hooks"
  cd "${BASE_DIR}"
  if [[ -d "${dir}" ]]; then
    for i in `ls -1 "${BASE_DIR}/${dir}"`; do
      if [[ -d "${BASE_DIR}/${dir}/${i}" ]] ; then
        cd "${BASE_DIR}/${dir}/${i}"
        echo "building ${dir}/${i} ..."
        TYPE_NAME=$(jq -r .typeName .rpdk-config)
        TYPE_NAME_DASHES=$(echo "$TYPE_NAME" | sed 's/::/-/g')
        TYPE_NAME_LOWER=$(echo "$TYPE_NAME_DASHES" | tr '[:upper:]' '[:lower:]')
        if [[ "${t}" == "java" ]] ; then
          mvn package >> $LOG_FILE || EXIT_CODE=1
          if [ $EXIT_CODE -eq 1 ] ; then
            echo "ERROR: failed to mvn package ${dir}/${i}"
            continue
          fi
        fi
        if [[ "${t}" == "python" ]] ; then
          if [[ ${BETA} ]] ; then
            cp ../../cloudformation_cli_python_lib-2.2.hooks-py2.py3-none-any.whl ./
          fi
        fi
        cfn generate || true
        cfn submit --dry-run || EXIT_CODE=1
        if [ $EXIT_CODE -eq 1 ] ; then
          echo "ERROR: failed to cfn submit --dry-run ${dir}/${i}"
          continue
        fi
        aws s3 cp "./${TYPE_NAME_LOWER}.zip" s3://${BUCKET}/ || EXIT_CODE=1
        if [ $EXIT_CODE -eq 1 ] ; then
          echo "ERROR: failed to s3 cp ${dir}/${i}"
          continue
        fi
      fi
    done
  fi
done
exit $EXIT_CODE
