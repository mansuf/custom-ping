::Custom Ping (CP) v1.1
::Customed Version for 'ping.exe'
::Written in Batch Language

::Checking for Debug Mode (You can do it too, type "Custom_Ping.bat" -debug)
::or You want to check your custom messages ?, type "Custom_Ping.bat" -debug-ping
set init_count=0
set loop_azure=1
set debug_azure=0
set debug_ping=0
if "%1"=="" (
    @echo off
    cls
) else (
    if "%1"=="-debug" echo on
    if "%1"=="-debug-ping" @echo off && set debug_ping=1 && goto debug_ping
    if "%1"=="-run-azure-pipelines" @echo off && set debug_azure=1 && goto debug_azure_pipelines
)
::Preparation from 'config.txt' file and 'custom_ping_messages' folder for Custom Ping
:init_preparation
set searched=0
set message_showed=0
:init
set missing_messages=0
if %debug_ping%==1 (
    set debug_ping=1
) else (
    timeout 1 /nobreak>NUL
)
if exist "config.txt" (
    goto preparation
) else (
    set ADDRESS_SERVER=8.8.8.8
    echo 'config.txt' file not found, recreating one.... (All config will return to Default)
    if not exist "custom_ping_messages" set missing_messages=1 && echo 'custom_ping_messages' folder not found, recreating one.... (All Output Ping Messages will return to Default)
    goto create_config
)
goto preparation

:debug_ping
set VAR_MODIFED_VERIFY_2=1
goto init_preparation
:loop
set /a VAR_MODIFED_VERIFY_2=VAR_MODIFED_VERIFY_2+1
if %VAR_MODIFED_VERIFY_2% LEQ 20 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_20%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 70 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_70%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 200 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_200%
    goto init
) 
if %VAR_MODIFED_VERIFY_2% LEQ 500 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_500%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 3000 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_3000%
    goto init
)
goto init_preparation

:preparation
set COM=NOT_FOUND
for /f "tokens=3" %%b in ('type config.txt ^| findstr change_output_message') do set COM=%%b
if "%COM%"=="1" goto open_editor
if "%COM%"=="0" set unknown=1
if "%COM%"=="NOT_FOUND" (
    echo ERROR : 'change_output_message' var not found in 'config.txt' file, recreating file....
    goto create_config
)
set ETTL=NOT_FOUND
for /f "tokens=3" %%b in ('type config.txt ^| findstr enable_ttl') do set ETTL=%%b
if "%ETTL%"=="1" set ETTL_VAR=1
if "%ETTL%"=="0" set ETTL=0 && set VAR_TTL_MODIFIED=
if "%ETTL%"=="NOT_FOUND" (
    echo ERROR : 'enable_ttl' var not found in 'config.txt' file, recreating file....
    goto create_config
)
for /f "tokens=3" %%b in ('type config.txt ^| findstr enable_count') do set EC=%%b
if "%EC%"=="1" set EC_VAR=1 && set count_messages=count=
if "%EC%"=="0" set count= && set count_messages=
if "%EC%"=="NOT_FOUND" (
    echo ERROR : 'enable_count' var not found in 'config.txt' file, recreating file....
    goto create_config
) 
if %message_showed%==1 goto preparation2
:find_address_server
for /f "tokens=3" %%b in ('type config.txt ^| findstr server_address') do set ADDRESS_SERVER=%%b
goto preparation2

:preparation2
goto preparation3

:preparation3
for /f "tokens=3" %%b in ('type config.txt ^| findstr server_address') do set ADDRESS_SERVER2=%%b
if not exist "custom_ping_messages" set missing_messages=1 && echo 'custom_ping_messages' folder not found, recreating one.... (All Output Ping Messages will return to Default) && goto write_custom_messages
if "%ADDRESS_SERVER%"=="%ADDRESS_SERVER2%" (
    goto 1time_message
) else (
    echo Host Address Changed!, from %ADDRESS_SERVER% to %ADDRESS_SERVER2%
    echo.
    echo Pinging %ADDRESS_SERVER2% with 32 bytes of data:
    set ADDRESS_SERVER=%ADDRESS_SERVER2%
    goto 1time_message
)

::An editor for Custom Ping Messages (ECM = Editor Custom Messages)
:open_editor
set message_showed=0
cls
title Editor for Custom Ping
echo type Anything for ping less than 20
echo press enter if you want to leave it Default
set PING_20=Your internet IS UNBELIEVEABLE!!!
set /p "PING_20=>"
if "%PING_20%"=="" set PING_20=Your internet IS UNBELIEVEABLE!!!
cls
echo type Anything for ping less than 70
echo press enter if you want to leave it Default
set PING_70=Your internet is EXCELLENT
set /p "PING_70=>"
if "%PING_70%"=="" set PING_70=Your internet is EXCELLENT
cls
echo type Anything for ping less than 200
echo press enter if you want to leave it Default
set PING_200=Your internet is GOOD
set /p "PING_200=>"
if "%PING_200%"=="" set PING_200=Your internet is GOOD
cls
echo type Anything for ping less than 500
echo press enter if you want to leave it Default
set PING_500=Your internet is BAD
set /p "PING_500=>"
if "%PING_500%"=="" set PING_500=Your internet is BAD
cls
echo type Anything for ping less than 3000
echo press enter if you want to leave it Default
set PING_3000=Your internet is VERY BAD
set /p "PING_3000=>"
if "%PING_3000%"=="" set PING_3000=Your internet is VERY BAD
cls
echo type Anything if ping 'timed out'
echo press enter if you want to leave it Default
set PING_TIMED_OUT=Your internet is NOT RESPONDING!!!
set /p "PING_TIMED_OUT=>"
if "%PING_TIMED_OUT%"=="" set PING_TIMED_OUT=Your internet is NOT RESPONDING!!!
cls
echo type Anything if ping 'Destination net unreachable'
echo press enter if you want to leave it Default
set PING_DNU=Connected but no internet.
set /p "PING_DNU=>"
if "%PING_DNU%"=="" set PING_DNU=Connected but no internet.
cls
echo type Anything if ping 'General Failure'
echo press enter if you want to leave it Default
set PING_GENERAL_FAILURE=Something not right...
set /p "PING_GENERAL_FAILURE=>"
if "%PING_GENERAL_FAILURE%"=="" set PING_GENERAL_FAILURE=Something not right...
cls
goto write_custom_messages
::if 'custom_ping_messages' is missing, recreating a new one with Default value (Example : 'Ping less than 20' printing 'Your internet IS UNBELIEVEABLE!!!')
:write_custom_messages
if %missing_messages%==1 (
    set PING_20=Your internet IS UNBELIEVEABLE!!!
    set PING_70=Your internet is EXCELLENT
    set PING_200=Your internet is GOOD
    set PING_500=Your internet is BAD
    set PING_3000=Your internet is VERY BAD
)
if not exist "custom_ping_messages" (
    md custom_ping_messages>NUL
)
echo %PING_20% > custom_ping_messages\messages20.txt
echo %PING_70% > custom_ping_messages\messages70.txt
echo %PING_200% > custom_ping_messages\messages200.txt
echo %PING_500% > custom_ping_messages\messages500.txt
echo %PING_3000% > custom_ping_messages\messages3000.txt
echo %PING_TIMED_OUT% > custom_ping_messages\messagesTO.txt
echo %PING_DNU% > custom_ping_messages\messagesDNU.txt
echo %PING_GENERAL_FAILURE% > custom_ping_messages\messagesGF.txt
goto search_custom_messages


::Search Custom Messages from 'custom_ping_messages' folder (SCM)
:search_custom_messages
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages20.txt"') do set PING_20=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages70.txt"') do set PING_70=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages200.txt"') do set PING_200=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages500.txt"') do set PING_500=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages3000.txt"') do set PING_3000=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messagesTO.txt"') do set PING_TIMED_OUT=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messagesDNU.txt"') do set PING_DNU=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messagesGF.txt"') do set PING_GENERAL_FAILURE=%%b

set searched=1
if %debug_azure%==1 goto loop_azure
if %missing_messages%==1 goto 1time_message
if "%ADDRESS_SERVER%"=="" call :scm_find_server_address
echo # Host / Server Address > config.txt
echo server_address = %ADDRESS_SERVER% >> config.txt
echo. >> config.txt
echo # Change the output Messages ping (1 = yes , 0 = no) >> config.txt
echo change_output_message = 0 >> config.txt
if "%ETTL%"=="1" goto scm_server_write1
:scm_server2
if "%EC%"=="1" goto scm_server_write2
echo. >> config.txt
echo # Enable TTL (Time To Live) (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_ttl = 0 >> config.txt
echo. >> config.txt
echo # Enable Count Ping (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_count = 0 >> config.txt
:scm_server3
if %message_showed%==1 goto 1time_message
echo.
echo Pinging %ADDRESS_SERVER2% with 32 bytes of data:
set message_showed=1
goto 1time_message

::Recreating Config if 'config.txt' not found
:create_config
echo # Host / Server Address > config.txt
echo server_address = 8.8.8.8 >> config.txt
echo. >> config.txt
echo # Change the output Messages ping (1 = yes , 0 = no) >> config.txt
echo change_output_message = 0 >> config.txt
echo. >> config.txt
echo # Enable TTL (Time To Live) (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_ttl = 0 >> config.txt
echo. >> config.txt
echo # Enable Count Ping (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_count = 0 >> config.txt
echo Using Default Host (8.8.8.8) / Google DNS 
if %missing_messages%==1 goto write_custom_messages
echo.
echo Pinging %ADDRESS_SERVER2% with 32 bytes of data:
goto 1time_message

::Example Ping Result
::Reply from 8.8.8.8: bytes=32 time=217ms TTL=54
::Pinging 8.8.8.8 with 32 bytes of data

:1time_message
title Custom Ping by trollfist20 , Server: %ADDRESS_SERVER%
if %debug_azure%==1 goto search_custom_messages
if %debug_ping%==1 goto loop
if %message_showed%==1 goto Module_Ping
echo Ping Customed Version v1.0 
echo Server Address : %ADDRESS_SERVER%
echo.
echo Pinging %ADDRESS_SERVER% with 32 bytes of data:
set message_showed=1
goto Module_Ping


::Unique Module Custom Ping (UMCP)
:Module_Ping
set VAR=NOT_FOUND
set VAR_MODIFIED=NOT_FOUND
set VAR_MODIFED_VERIFY=NOT_FOUND
set VAR_MODIFED_VERIFY_2=NOT_FOUND
for /f "tokens=*" %%b in ('ping %ADDRESS_SERVER% -n 1 ^| findstr /C:Reply /C:General /C:Destination /C:Request') do set VAR=%%b
for /f "tokens=5" %%b in ("%VAR%") do set VAR_MODIFIED=%%b
for /f "delims=time tokens=1" %%b in ('echo %VAR_MODIFIED% ^| findstr [0-9]') do set VAR_MODIFED_VERIFY=%%b
for /f "delims=time tokens=1" %%b in ('echo %VAR_MODIFED_VERIFY%') do set VAR_MODIFED_VERIFY_2=%%b
if "%ETTL%"=="1" for /f "tokens=6" %%b in ("%VAR%") do set VAR_TTL_MODIFIED=%%b
set /a init_count=init_count+1
if "%EC%"=="1" set count=%init_count%
if %VAR_MODIFED_VERIFY_2%==NOT_FOUND (
    goto Module_Ping_Error
) else (
    goto Module_Ping_Success
)
goto Module_Ping


:Module_Ping_Success
::if SCM (Search Custom Messages) has finished search, return variable 'searched' to 1 (Finished Searching)
::And Redirecting to Module_Ping_Success2 Label/Function
if %searched%==1 goto Module_Ping_Success2
goto search_custom_messages


:Module_Ping_Success2
if %VAR_MODIFED_VERIFY_2% LEQ 20 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_20% %VAR_TTL_MODIFIED% %count_messages%%count%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 70 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_70% %VAR_TTL_MODIFIED% %count_messages%%count%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 200 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_200% %VAR_TTL_MODIFIED% %count_messages%%count%
    goto init
) 
if %VAR_MODIFED_VERIFY_2% LEQ 500 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_500% %VAR_TTL_MODIFIED% %count_messages%%count%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 3000 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_3000% %VAR_TTL_MODIFIED% %count_messages%%count%
    goto init
)
echo Return ERROR : Result not Found, Make sure you type correctly host or server address
goto init

:Module_Ping_Error
set VAR_ERROR=NOT_FOUND
for /f "tokens=1" %%b in ("%VAR%") do set VAR_ERROR=%%b
if %VAR_ERROR%==General (
    echo [General Failure] %PING_GENERAL_FAILURE% %count_messages%%count%
    goto init
)
if %VAR_ERROR%==Reply (
    echo [Destination net unreachable] %PING_DNU% %count_messages%%count%
    goto init
)
if %VAR_ERROR%==Request (
    echo [Timed Out] %PING_TIMED_OUT% %count_messages%%count%
    goto init
)
echo Return ERROR : Result not Found, Make sure you type correctly host or server address
goto init


::Debugging in Azure Pipelines
:debug_azure_pipelines
goto init_preparation
:loop_azure
if 20 LEQ 20 echo [20] %PING_20%
if 70 LEQ 70 echo [70] %PING_70%
if 200 LEQ 200 echo [200] %PING_200%
if 500 LEQ 500 echo [500] %PING_500%
if 3000 LEQ 3000 echo [3000] %PING_3000%
echo [Timed Out] %PING_TIMED_OUT%
echo [Destination net unreachable] %PING_DNU%
echo [General Failure] %PING_GENERAL_FAILURE%
pause
exit

:scm_server_write1
echo. >> config.txt
echo # Enable TTL (Time To Live) (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_ttl = 1 >> config.txt
goto scm_server2

:scm_server_write2
echo. >> config.txt
echo # Enable Count Ping (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_count = 1 >> config.txt
goto scm_server3

:scm_find_server_address
for /f "tokens=3" %%b in ('type config.txt ^| findstr server_address') do set ADDRESS_SERVER=%%b
set ADDRESS_SERVER2=%ADDRESS_SERVER%