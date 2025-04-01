# Criar diretório temporário para o novo projeto
$novoRepoPath = "C:\Users\leona\Documents\coisas\SI\projets\todo-list-novo"
New-Item -ItemType Directory -Path $novoRepoPath -Force

# Copiar todos os arquivos relevantes (excluindo .git e problemas de submodules)
Get-ChildItem -Path . -Exclude .git,frontend,frontend-backup | Copy-Item -Destination $novoRepoPath -Recurse -Force

# Se você tiver o código frontend em algum lugar, copie-o também
if (Test-Path ".\frontend") {
    New-Item -ItemType Directory -Path "$novoRepoPath\frontend" -Force
    # Copie apenas os arquivos reais, não as referências de submodule
    Get-ChildItem -Path .\frontend -Exclude .git | Copy-Item -Destination "$novoRepoPath\frontend" -Recurse -Force
}

# Navegue para o novo diretório
cd $novoRepoPath

# Inicialize um novo repositório Git
git init

# Adicione e faça commit de tudo
git add .
git commit -m "Versão inicial limpa do projeto todo-list"

# Instruções para configurar o repositório remoto
Write-Host "Novo repositório criado com sucesso em: $novoRepoPath" -ForegroundColor Green
Write-Host "Para adicionar um repositório remoto, execute:" -ForegroundColor Yellow
Write-Host "git remote add origin https://github.com/seu-usuario/nome-do-repo.git" -ForegroundColor Yellow
Write-Host "git push -u origin main" -ForegroundColor Yellow
