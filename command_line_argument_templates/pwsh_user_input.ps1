param(
        [Parameter()]
        [string]$def_str="this is a string",
        [int]$def_int=31337,
        [switch]$Help
)
function print_help(){
Write-Host @"

pwsh ./pwsh_user_input.ps1 -help

pwsh ./pwsh_user_input.ps1
pwsh ./pwsh_user_input.ps1 -def_str 'updated_string' -def_int 9001
"@ -f DarkYellow
}
if($Help){
	print_help
	break
}else{
	Write-Host "`r`nThis is the string you set: $def_str"
	Write-Host "This is the int you set: $def_int"
}
