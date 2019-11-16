*** Settings ***
Library    SeleniumLibrary
Library    UIRepository
Library    Collections
Library    String


*** Keywords ***
Load UI Repository
    [Documentation]  Loads UI elements repository into suite variable
    ...              This keyword should be used in suite setup
    [Arguments]  ${repo_path}
    ${UI}=  Load Repository  ${repo_path}