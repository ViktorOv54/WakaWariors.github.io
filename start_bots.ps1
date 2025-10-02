# Paths to Python and bot scripts
$python = "C:\Users\Viktor Orlov LBC\AppData\Local\Programs\Python\Python311\python.exe"
$customerBot = "C:\Users\Viktor Orlov LBC\OneDrive\Desktop\DTS (LBC)\AS 92005\Dragon Boating (working) - Done\customer_bot.py"
$devtoolsBot = "C:\Users\Viktor Orlov LBC\OneDrive\Desktop\DTS (LBC)\AS 92005\Dragon Boating (working) - Done\devtools_bot.py"

# Start Customer Bot in a new window
Start-Process $python -ArgumentList $customerBot -WindowStyle Normal

# Start Developer Tools Bot in a new window
Start-Process $python -ArgumentList $devtoolsBot -WindowStyle Normal

Write-Host "Both bots are starting..."
