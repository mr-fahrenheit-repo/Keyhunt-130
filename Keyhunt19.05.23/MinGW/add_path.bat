@echo off
powershell -command "[Environment]::SetEnvironmentVariable('Path', $env:Path + ';'+$pwd, [System.EnvironmentVariableTarget]::User);"