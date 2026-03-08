# Wrapper PowerShell script to activate project's .venv
$script = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $script) {
    & $script
} else {
    Write-Host "Virtual environment not found: .venv" -ForegroundColor Red
    exit 1
}
