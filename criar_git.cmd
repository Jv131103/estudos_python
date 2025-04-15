@echo off
setlocal enabledelayedexpansion

call :print_msg amarelo "Acessando git e gerando no GitHub..."
call :print_msg amarelo "NÃO ESQUEÇA DE GERAR SEU REPOSITÓRIO NO GITHUB TAMBÉM..."

:: Inputs interativos
set /p usuario=Digite seu nome de usuário do GitHub: 
set /p repositorio=Digite o nome do repositório: 

if "%usuario%"=="" (
    call :print_msg vermelho "Usuário não informado. Encerrando script."
    exit /b 1
)

if "%repositorio%"=="" (
    call :print_msg vermelho "Repositório não informado. Encerrando script."
    exit /b 1
)

call :print_msg amarelo "Iniciando git init..."
git init
if errorlevel 1 (
    call :print_msg vermelho "Erro ao iniciar o repositório local."
    exit /b 1
)
call :print_msg verde "Repositório iniciado com sucesso!"

call :print_msg amarelo "Adicionando arquivos e realizando commit..."
git add .
git commit -m "feat/initial_project"
if errorlevel 1 (
    call :print_msg vermelho "Erro ao adicionar/commitar arquivos."
    exit /b 1
)
call :print_msg verde "Commit realizado com sucesso!"

call :print_msg amarelo "Adicionando repositório remoto..."
git remote add origin https://github.com/%usuario%/%repositorio%.git
if errorlevel 1 (
    call :print_msg vermelho "Erro ao adicionar o remoto. Já existe?"
    exit /b 1
)
call :print_msg verde "Repositório remoto adicionado com sucesso!"

call :print_msg amarelo "Enviando projeto para o GitHub (forçado)..."
git branch -M main
git push -u origin main --force
if errorlevel 1 (
    call :print_msg vermelho "Erro ao realizar push."
    exit /b 1
)
call :print_msg verde "Projeto enviado com sucesso para o GitHub!"

call :print_msg verde "FIM DA EXECUÇÃO."
pause
exit /b

:: ---- Função de mensagem (deixe no final do arquivo) ----
:print_msg
set "color=%~1"
set "msg=%~2"
if "%color%"=="verde" (
    echo [OK] %msg%
) else if "%color%"=="vermelho" (
    echo [ERRO] %msg%
) else if "%color%"=="amarelo" (
    echo [INFO] %msg%
) else (
    echo %msg%
)
goto :eof
