app="docker.insidecode"
docker build -t ${app} .
docker run -d -p 12777:80 ${app}
