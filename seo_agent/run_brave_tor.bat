@echo off
echo Launching Brave Browser with Tor network...

rem Set the path to Brave Browser
set BRAVE_PATH="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

rem Check if Brave exists
if not exist %BRAVE_PATH% (
    echo ERROR: Brave browser not found at %BRAVE_PATH%
    echo Please make sure Brave is installed or update the path in this script.
    pause
    exit /b 1
)

rem Launch Brave with Tor arguments
echo Starting Brave with Tor...
start "" %BRAVE_PATH% --incognito --tor-profile

echo Brave launched with Tor network. Check the Tor icon in the browser to confirm connection.
echo Close this window when done. 