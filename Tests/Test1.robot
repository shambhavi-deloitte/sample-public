*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Variables           ../Constant/Constants.py
Force Tags         allure.feature:Abstract Layer
Library            ../Libraries/DriverHandler.py
Library             ../Libraries/AllureReport.py
Force Tags             allure.feature:Abstract

*** Variables ***
${base url}=    https://admin-demo.nopcommerce.com/Admin
${browser_name}= edge

*** Keywords ***
Launch Browser And Naviagte To Url
    ${path}=         generate categories
    log to console      ${path}
    ${driver_path}=    browser driver path            ${browser_name}
    open browser        ${base url}     ${browser_name}     executable_path=${driver_path}
    Maximize Browser Window

#Launch And Naviagte To Url
#    open browser        ${base url}     ${browser_name}
#    Fail

*** Test Cases ***
Validate login page
    Launch Browser And Naviagte To Url

#Failing Example
#    Launch And Naviagte To Url

