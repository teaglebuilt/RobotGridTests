*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/common.robot


Suite Setup  Load UI Repository  ${REPO_PATH}
Test Teardown  Close All Browsers


*** Test Cases ***
Authentication
    Open Browser  ${HOST}  ${BROWSER}  remote_url=${SELENIUM_HUB}