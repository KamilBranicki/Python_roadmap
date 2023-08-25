#stowrzenie virtualnego środowiska: CTRL + shift + p > Python:Create Virtual Enviroment > venv > select folder

# dodanie zmiennej środowiskowej

import os

password = os.environ["MY_USERNAME"]
print(password)

#bash:
#  source .venv/Scripts/activate
#  export MY_USERNAME="Pumpek" - stworzy zmienną tylko w sesji

# env variable as const > go to activate file > inser there