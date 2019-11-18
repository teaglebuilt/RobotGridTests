*** Settings ***
Library    SeleniumLibrary
Library    UIRepository
Library    Collections
Library    String
Library    SeleniumLibrary  plugins=${CURDIR}/../lib/Testability;True;29 seconds;False


*** Keywords ***
Load UI Repository
    [Documentation]  Loads UI elements repository into suite variable
    ...              This keyword should be used in suite setup
    [Arguments]  ${repo_path}
    ${UI}=  Load Repository  ${repo_path}


Local Setup Test Environment
    [Arguments]  ${BROWSER}  ${PREFS}  ${SELENIUM_HUB}
    [Documentation]  normal test setup but with desired_capabilities added
    ${cap}=  Generate Capabilities with Logging Prefs  ${BROWSER}  ${PREFS}
    ${FF_PROFILE}=     Generate Firefox Profile
    Open Browser  ${URL}  browser=${BROWSER}  remote_url=${SELENIUM_HUB}  desired_capabilities=${cap}  ff_profile_dir=${FF_PROFILE.path}
    Wait For Document Ready

Generate Capabilities with Logging Prefs
    [Documentation]  Generates default_capabilities with browser all to given loging prefs
    [Arguments]   ${BROWSER}  ${PREFNAME}
    ${defaults}=  Get Default Capabilities  ${BROWSER}
    ${browser_all}=  Create Dictionary  browser=ALL
    ${logging}=  Create Dictionary  ${PREFNAME}  ${browser_all}
    ${cap}=  Create Dictionary  &{defaults}  &{logging}
    [return]  ${cap}