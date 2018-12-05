Для работы необходимо наличие в системе: docker, docker-compose, git.

  Если их нет.

    Для Ubuntu 18.04.

    - docker: 
        $ sudo apt update
        $ sudo apt install apt-transport-https ca-certificates curl software-properties-common
        $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
        $ sudo apt update
        $ apt-cache policy docker-ce
        $ sudo apt install docker-ce
        
        проверяем:
            $ sudo systemctl status docker
           
   - docker-compose:
       $ sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
       $ sudo chmod +x /usr/local/bin/docker-compose
       
       проверяем:
           $ docker-compose --version
           
   - git:
       $ sudo apt install git
       
В папке, в которой планируем размещать проект:
    
    $ git clone https://github.com/KiChi88/company_base.git
    
Затем выполняем:
    
    $ cd company_base
    $ sudo docker-compose build
    $ sudo docker-compose run project python3 manage.py migrate
    
    если нужна тестовая база (файл company_base/project/db.json):
        $ sudo docker-compose run project python3 manage.py loaddata db.json
        
    если необходимо создать суперпользователя:
        $ sudo docker-compose run project python3 manage.py createsuperuser
        дальше по инструкциям
        
    $ sudo docker-compose run project python3 manage.py collectstatic
    $ sudo docker-compose up
