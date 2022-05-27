# login-counter

This repository is used to automate the deployment of AlphaClient and AlphaServer containers. AlphaClient will provide API about login count when someone log in with ssh, hostname or Container ID and ip address of the container. AlphaServer will read that API

<div><h1>📜 Table of Contents</h1></div>

- [login-counter](#login-counter)
- [Generic Setup](#generic-setup)
  - [Prerequisites](#prerequisites)
- [Clone The Repo](#clone-the-repo)
- [Deployment](#deployment)
- [Testing AlphaClient](#testing-alphaclient)
- [Testing AlphaServer](#testing-alphaserver)


# Generic Setup
## Prerequisites
- Docker. you can install [here][docker-url] or [Docker Desktop][docker-desktop-url]
- Docker compose. Docker Desktop for Windows or Mac includes Compose along with other Docker apps, so most Windows users or Mac users do not need to install Compose separately. if you don't have docker compose, you can go [here][docker-compose-url]


# Clone The Repo
clone this repository using git command:

```sh
git clone https://github.com/fachryfathurahman/login-counter.git
```

# Deployment
now deploy with docker compose:

```sh
docker-compose up
```

# Testing AlphaClient
After deployment, now you have 2 node AlphaClient and one 1 AlphaServer in the form of a container. Go to web browser and type [localhost:8080/info][url-node-abc] for nodeABC:

```JSON
{
  "count": 0,
  "hostname": "51463dfb78d8",
  "IPAddr": "172.30.0.3"
}
```
and [localhost:8081/info][url-node-xyz] for nodeXYZ:
```JSON
{
  "count": 0,
  "hostname": "83b4889f4041",
  "IPAddr": "172.30.0.4"
}
```

# Testing AlphaServer
you can login to AlphaServer with two ways, first with `exec` command:

```sh
docker exec -it <YOUR CONTAINER ID> bash
```
```sh
docker exec -it login-counter-nodeXYZ-1 bash
```


or with `ssh` with password `mypassword`:
```sh
ssh root@localhost -p 2024
```

after login, run bash script on `/code` with command:
```sh
./start.sh
```

script will ask you and you can answer:
```sh
How many AlphaClient do you have?: 2
```

and the next question about IP address that AlphaClients have, for me, the IP address is:
```sh
Enter IP Address 1:
172.30.0.3
Enter IP Address 2:
172.30.0.4
```

and AlphaServer will request API periodically and the output will be:
```sh
{"count":0,"hostname":"51463dfb78d8","IPAddr":"172.30.0.3"}
{"count":0,"hostname":"83b4889f4041","IPAddr":"172.30.0.4"}
```

because nodeABC (172.30.0.3) expose port 22 through 2022, you can log in on your command prompt with ssh with password `mypassword`:

```sh
ssh root@localhost -p 2022
```
and the output of AlphaServer will be:
```sh
{"count":1,"hostname":"51463dfb78d8","IPAddr":"172.30.0.3"}
{"count":0,"hostname":"83b4889f4041","IPAddr":"172.30.0.4"}
```

[docker-url]: https://docs.docker.com/engine/install/ubuntu/
[docker-desktop-url]: https://www.docker.com/products/docker-desktop/
[docker-compose-url]: https://docs.docker.com/compose/install/
[url-node-abc]: https://localhost:8080/info
[url-node-xyz]: https://localhost:8081/info