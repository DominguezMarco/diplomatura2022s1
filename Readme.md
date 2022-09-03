# Trabajo Práctico Diplomatura GNU/Linux 2022S1

A continuación se detallan los pasos necesarios para realizar el despliegue de una aplicación en python en un contenedor docker. 

## Despliegue

- Paso 1: Clonado del proyecto. 
```
	# git clone https://github.com/DominguezMarco/diplomatura2022s1
	# cd diplomatura2022s1
``` 

- Paso 2: Instalación de ansible
  - Para distribuciones debian:
```
	# sudo apt install ansible
```
  - Para distribuciones redhat
```
	# sudo yum install ansible
```

- Paso 3: Definición del equipo anfitrión que ejecutará la aplicación y edición del inventario de ansible.
```
	vi hosts.yml
```
  - Si queremos desplegar la apliación en el host local podemos tener el siguiente inventario
```
all:
  vars:
    ansible_python_interpreter: /usr/bin/python3
  children:
    local:
local:
  vars:
    ansible_connection: local
  hosts:
    localhost
```
- Paso 4: Ejecución de la guía de ansible
``` 
	# ansible-playbook -i hosts.yml playbook/clockPlaybook.yaml
```