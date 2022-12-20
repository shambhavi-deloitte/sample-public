*** Settings ***
Documentation       Connecting to Java Remote Library

*** Variables ***
${ADDRESS}    127.0.0.1
${PORT}       8270

*** Test Cases ***
Run Remote Library
    Import Remote Library

*** Keywords ***
Import Remote Library
       Import Library   Remote   http://localhost:8270/   WITH NAME   MyRemoteLibrary
       Clear Queue
       Add To Queue   ${42}
       Add To Queue   ${3.14}
       Add To Queue   Hail to the robots
       Log Queue