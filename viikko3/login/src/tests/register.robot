*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register Succeeds When Password And Confirmation Match
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Welcome Page Should Be Open

Register Fails When Password And Confirmation Differ
    Set Username  kalle7
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Click  button >> text=Register
    Registration Should Fail With Message  Passwords do not match

Register With Password Containing Numbers
    Set Username  kalle3
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Welcome Page Should Be Open

Register With Password Containing Special Characters
    Set Username  kalle4
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Welcome Page Should Be Open

Register With Password Containing Only Lowercase Letters
    Set Username  kalle5
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Registration Should Fail With Message  Password must contain at least one non-letter character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  kalle6
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Registration Should Fail With Message  Password must contain at least one non-letter character

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Fail With Message  Username too short


Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  lyhyt
    Set Password Confirmation  lyhyt
    Click  button >> text=Register
    Registration Should Fail With Message  Password too short

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page should Be Open
    Get Text  body  *=  ${message}
