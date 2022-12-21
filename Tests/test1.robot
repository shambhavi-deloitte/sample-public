*** Settings ***
Documentation   To validate the Login form
Library         SeleniumLibrary
Library         ../Libraries/DriverHandler.py

*** Test Cases ***
Validate UnSuccesful Login
    open the browser with the Mortgage payment url
    Fill the login Form
#    wait until it checks and display error message
#    verify error message is correct

*** Keywords ***
open the browser with the Mortgage payment url
     ${driver_path}=    browser driver path            headlesschrome
    open browser        https://rahulshettyacademy.com/loginpagePractise/   headlesschrome    executable_path=${driver_path}
Fill the login Form
    Input Text          id:username     priyashambhavi
    Input Password      id:password     2345677
    Click Button        signInBtn
    close browser

#wait until it checks and display error message
#    Wait Until Element Is Visible       ${Error_Message_Login}
#
#verify error message is correct
#   ${result}=   Get Text    ${Error_Message_Login}
#   Should Be Equal As Strings     ${result}     Incorrect username/password.
#   Element Text Should Be       ${Error_Message_Login}      Incorrect username/password.
















