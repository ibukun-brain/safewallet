#!/bin/bash

git add . > /dev/null 2>&1

echo "Running pylint ..."
sleep 1
pylint $(git ls-files '*.py')
echo
echo "Pylint run complete"
echo

# echo "Running flake8 ..."
# sleep 1
# flake8
# echo
# echo "Flake8 run complete"
# echo


echo "Running tests"
sleep 1
UNIT_TEST_OUTPUT=`python manage.py test --keepdb -v 2`
echo "UNIT TEST RUN COMPLETE"
echo


# PYLINT_SCORE=$(echo $PYLINT_RESULT | grep -Eo 'at [0-9.]{0,4}' | grep -Eo '[0-9.]{0,4}')
# if [[ $PYLINT_SCORE = *10* && $UNIT_TEST_OUTPUT != *FAILED* ]]
if [[ $UNIT_TEST_OUTPUT != *FAILED* ]]
then
#     git add . > /dev/null 2>&1
#     BRANCH_NAME=$(git branch --show-current)
#     GIT_STATUS="$(git status -s)"

#     if [[ "$GIT_STATUS" = *'M'* ]]
#     then
#         echo "Please enter commit message for $BRANCH_NAME"
#         read COMMIT_MESSAGE
#         git commit -m "$COMMIT_MESSAGE"
#     fi

#     git push -u origin $BRANCH_NAME
    echo "ALL CHECKS PASSED"
    exit 0
else
    echo "FAILURE. Please check the comments above. Fix the issue and re-run script"
    exit 1
fi
