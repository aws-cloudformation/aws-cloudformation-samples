FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-18.04

# get back to root because we like danger
USER 0
ENV HOME=/root

# Get to latest versions of all packages
RUN apt-get update && apt-get -y upgrade --no-install-recommends

# Install common dependencies
RUN apt-get -y install --no-install-recommends \
    build-essential \
    git \
    openssh-client \
    less \
    iproute2 \
    procps \
    curl \
    wget \
    unzip \
    nano \
    jq \
    lsb-release \
    ca-certificates \
    apt-transport-https \
    dialog \
    gnupg2 \
    libc6 \
    libgcc1 \
    libgssapi-krb5-2 \
    libicu[0-9][0-9] \
    liblttng-ust0 \
    libstdc++6 \
    zlib1g \
    locales

# Node.js
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - \
    && sudo apt-get install -y nodejs

# Python
RUN apt install -y software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get -y install --no-install-recommends python3.7 python3-pip

# Docker
RUN apt-get install -y apt-transport-https ca-certificates curl lsb-release \
    && curl -fsSL https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/gpg | apt-key add - 2>/dev/null \
    && echo "deb [arch=amd64] https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y docker-ce-cli \
    && LATEST_COMPOSE_VERSION=1.25.5 curl -sSL "https://github.com/docker/compose/releases/download/${LATEST_COMPOSE_VERSION}/docker-compose-Linux-x86_64" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws

# CDK
RUN npm install -g aws-cdk && npm install -g typescript

# SAM CLI & AWS CloudFormation Resource Provider TypeScript Plugin
RUN curl https://raw.githubusercontent.com/Homebrew/install/master/install.sh -o brew.sh \
    && sed -i "s/abort \"Don't run this as root\!\"/echo \"Don't run this as root\!\"/" brew.sh \
    && chmod +x brew.sh \
    && ./brew.sh \
    && rm -rf brew.sh \
    && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv) \
    && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile \
    && brew tap aws/tap \
    && brew install aws-sam-cli \
    && pip3 install setuptools \
    && pip3 install wheel \
    && pip3 install git+https://github.com/eduardomourar/cloudformation-cli-typescript-plugin.git@v0.5.0#egg=cloudformation-cli-typescript-plugin \
    && pip3 install cloudformation-cli==0.1.*

# Cleanup
 RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*