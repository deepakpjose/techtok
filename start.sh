app="docker.insidecode"
docker build -t ${app} .
docker run -d -p 80:80 -v /home/ubuntu/techtok/nginx.conf:/etc/nginx/nginx.conf ${app}
