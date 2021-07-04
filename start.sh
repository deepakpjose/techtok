app="docker.insidecode"
docker build -t ${app} .
docker run -d -p http://www.insidecode.me -v nginx.conf:/etc/nginx/nginx.conf ${app}
