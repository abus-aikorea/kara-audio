@echo off
setlocal enabledelayedexpansion

echo =========================================================================
echo.
echo   ABUS Launcher [Version 3.0]
echo   contact: abus.aikorea@gmail.com
echo.
echo =========================================================================
echo.

cd /D "%~dp0"
set PATH=%PATH%;%SystemRoot%\system32
echo "%CD%"| findstr /C:" " >nul && echo This script relies on Miniconda which can not be silently installed under a path with spaces. && goto end


:: Check for special characters in installation path
set "SPCHARMESSAGE="WARNING: Special characters were detected in the installation path!" "         This can cause the installation to fail!""
echo "%CD%"| findstr /R /C:"[!#\$%&()\*+,;<=>?@\[\]\^`{|}~]" >nul && (
	call :PrintBigMessage %SPCHARMESSAGE%
)
set SPCHARMESSAGE=


:: fix failed install when installing to a separate drive
set TMP=%cd%\installer_files
set TEMP=%cd%\installer_files

:: deactivate existing conda envs as needed to avoid conflicts
(call conda deactivate && call conda deactivate && call conda deactivate) 2>nul


:: config
set INSTALL_DIR=%cd%\installer_files
set CONDA_ROOT_PREFIX=%cd%\installer_files\conda
set INSTALL_ENV_DIR=%cd%\installer_files\env

:: ABUS miniconda fo python 3.9
set MINICONDA_DOWNLOAD_URL=https://repo.anaconda.com/miniconda/Miniconda3-py39_24.1.2-0-Windows-x86_64.exe
set MINICONDA_CHECKSUM=6128825cdcde8ec0c0a5a9ed3dc021cc920040905dee39e58e827bc27fea0bee
set conda_exists=F

:: figure out whether git and conda needs to be installed
call "%CONDA_ROOT_PREFIX%\_conda.exe" --version >nul 2>&1
if "%ERRORLEVEL%" EQU "0" set conda_exists=T


:: (if necessary) install git and conda into a contained environment
:: download conda
if "%conda_exists%" == "F" (
	echo Downloading Miniconda from %MINICONDA_DOWNLOAD_URL% to %INSTALL_DIR%\miniconda_installer.exe

	mkdir "%INSTALL_DIR%"
	call curl -Lk "%MINICONDA_DOWNLOAD_URL%" > "%INSTALL_DIR%\miniconda_installer.exe" || ( echo. && echo Miniconda failed to download. && goto end )

	for /f %%a in ('CertUtil -hashfile "%INSTALL_DIR%\miniconda_installer.exe" SHA256 ^| find /i /v " " ^| find /i "%MINICONDA_CHECKSUM%"') do (
		set "output=%%a"
	)

	if not defined output (
		echo The checksum verification for miniconda_installer.exe has failed.
		del "%INSTALL_DIR%\miniconda_installer.exe"
		goto end
	) else (
		echo The checksum verification for miniconda_installer.exe has passed successfully.
	)

	echo Installing Miniconda to %CONDA_ROOT_PREFIX%
	start /wait "" "%INSTALL_DIR%\miniconda_installer.exe" /InstallationType=JustMe /NoShortcuts=1 /AddToPath=0 /RegisterPython=0 /NoRegistry=1 /S /D=%CONDA_ROOT_PREFIX%

	:: test the conda binary
	echo Miniconda version:
	call "%CONDA_ROOT_PREFIX%\_conda.exe" --version || ( echo. && echo Miniconda not found. && goto end )

	:: delete the Miniconda installer
	del "%INSTALL_DIR%\miniconda_installer.exe"
)

:: ABUS python 3.9
:: create the installer env
set abus_genuine_installed=T
if not exist "%INSTALL_ENV_DIR%" (
	set abus_genuine_installed=F
	echo Packages to install: %PACKAGES_TO_INSTALL%
	call "%CONDA_ROOT_PREFIX%\_conda.exe" create --no-shortcuts -y -k --prefix "%INSTALL_ENV_DIR%" python=3.9 || ( echo. && echo Conda environment creation failed. && goto end )
)


:: check if conda environment was actually created
if not exist "%INSTALL_ENV_DIR%\python.exe" ( echo. && echo Conda environment is empty. && goto end )


:: environment isolation
set PYTHONNOUSERSITE=1
set PYTHONPATH=
set PYTHONHOME=
set "CUDA_PATH=%INSTALL_ENV_DIR%"
set "CUDA_HOME=%CUDA_PATH%"

:: activate installer env
call "%CONDA_ROOT_PREFIX%\condabin\conda.bat" activate "%INSTALL_ENV_DIR%" || ( echo. && echo Miniconda hook not found. && goto end )


:: setup installer env
echo Miniconda location: %CONDA_ROOT_PREFIX%
cd /D "%~dp0"
if "%abus_genuine_installed%" == "F" (
	call python -m pip install huggingface-hub==0.17.3
)

set LOG_LEVEL=DEBUG
call python start-abus.py %*

:: below are functions for the script   next line skips these during normal execution
goto end


:PrintBigMessage
echo. && echo.
echo *******************************************************************
for %%M in (%*) do echo * %%~M
echo *******************************************************************
echo. && echo.
exit /b

:end
pause