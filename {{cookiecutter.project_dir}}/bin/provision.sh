#!/bin/bash

PGSQL_VERSION=9.5
PROJECT_DIR="/home/vagrant/{{ cookiecutter.project_dir }}"
PROVISIONING="${PROJECT_DIR}/etc"
DBUSER="vagrant"
DB="{{ cookiecutter.project_dir }}"
DISTRO=$(lsb_release --codename --short)

# create dirs
mkdir -p "${PROJECT_DIR}"
mkdir -p /home/vagrant/.cache/vim
mkdir -p /home/vagrant/.config/mc
mkdir -p /etc/etckeeper

# set config files

cat > /etc/apt/sources.list << EOF
deb http://ftp.ubuntu.com/ubuntu/ ${DISTRO} main restricted universe multiverse
deb-src http://ftp.ubuntu.com/ubuntu/ ${DISTRO} main restricted universe multiverse
deb http://ftp.ubuntu.com/ubuntu/ ${DISTRO}-updates main restricted universe multiverse
deb-src http://ftp.ubuntu.com/ubuntu/ ${DISTRO}-updates main restricted universe multiverse
deb http://ftp.ubuntu.com/ubuntu/ ${DISTRO}-backports main restricted universe multiverse
deb-src http://ftp.ubuntu.com/ubuntu/ ${DISTRO}-backports main restricted universe multiverse
deb http://security.ubuntu.com/ubuntu ${DISTRO}-security main restricted universe multiverse
deb-src http://security.ubuntu.com/ubuntu ${DISTRO}-security main restricted universe multiverse
deb http://archive.canonical.com/ubuntu ${DISTRO} partner
deb-src http://archive.canonical.com/ubuntu ${DISTRO} partner
deb http://extras.ubuntu.com/ubuntu ${DISTRO} main
deb-src http://extras.ubuntu.com/ubuntu ${DISTRO} main
EOF

echo "Europe/Rome" > /etc/timezone
cp -a "${PROVISIONING}/etckeeper/etckeeper.conf" /etc/etckeeper/etckeeper.conf

cp -a "${PROVISIONING}/mc/ini" /home/vagrant/.config/mc/ini
cp -a "${PROVISIONING}/vim" /home/vagrant/.config/vim
cp -a "${PROVISIONING}/bash/bashrc" /home/vagrant/.bashrc
cp -a "${PROVISIONING}/bash/profile" /home/vagrant/.profile
cp -a "${PROVISIONING}/bash/inputrc" /home/vagrant/.inputrc
cp -a "${PROVISIONING}/bash/selected_editor" /home/vagrant/.selected_editor

# postgresql
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ ${DISTRO}-pgdg main" > /etc/apt/sources.list.d/postgresql.list

# nodejs
wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
echo "deb https://deb.nodesource.com/node_5.x ${DISTRO} main" > /etc/apt/sources.list.d/nodejs.list

apt-add-repository -y ppa:git-core/ppa
apt-add-repository -y ppa:nginx/stable

export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get dist-upgrade -y
apt-get autoremove --purge -y

apt-get install -y \
    postgresql-${PGSQL_VERSION} libpq-dev postgresql-${PGSQL_VERSION}-postgis-2.2 \
    python3.4-dev python3-lxml \
    python-dev python \
    libjpeg-dev libpng12-dev libtiff4-dev \
    nodejs \
    git \
    openssl-blacklist zip unrar \
    ssh htop etckeeper rsync mc vim sqlite3 xz-utils build-essential

# Postgresql setup for project
su postgres -c "createuser --user postgres --createdb --no-createrole --no-superuser ${DBUSER}"
su postgres -c "createdb --user postgres --owner ${DBUSER} ${DB}"

apt-get install -y python-pip python3-pip
pip2 install --upgrade pip
pip3 install --upgrade pip

pip2 install --upgrade grin
pip2 install --upgrade hg-git
pip2 install --upgrade mercurial
pip2 install --upgrade fabric

pip3 install --upgrade scripts
pip3 install --upgrade django-scripts

pip3 install --upgrade psycopg2
pip3 install --upgrade ipython
pip3 install --upgrade pillow
pip3 install --upgrade python3-memcached
pip3 install --upgrade libsass
pip3 install --upgrade awscli
pip3 install --upgrade uwsgi
pip3 install --upgrade invoke

# nodejs setup
npm install -g less

# mercurial setup
mkdir -p /home/vagrant/.local/mercurial
cp -a "${PROVISIONING}/mercurial/hgrc" /home/vagrant/.local/mercurial
cp -a "${PROVISIONING}/mercurial/style" /home/vagrant/.local/mercurial
(cd /home/vagrant/.local/mercurial \
  && hg clone https://www.mercurial-scm.org/repo/evolve/ \
  && hg clone https://www.mercurial-scm.org/repo/topic-experiment/ \
)

chown -R vagrant:vagrant /home/vagrant

(cd /etc && hg init && hg addremove && hg ci -m init -u root)
