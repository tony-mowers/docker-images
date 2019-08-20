#
# Docker image demonstrating how to use SDKMAN to setup JVM related tools 
#
FROM ubuntu:18.04

ENV JAVA_VERSION="8.0.222-zulu" \
    MAVEN_VERSION="3.6.1" \
    SDKMAN_DIR="/root/.sdkman"

#
# Add some common packages
#
RUN set -ex && \
    apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    wget \
    unzip \
    zip \
    && rm -rf /var/lib/apt/lists/*

RUN curl -s "https://get.sdkman.io" | bash && \
    bash -c ". ${SDKMAN_DIR}/bin/sdkman-init.sh && \
    sdk install java ${JAVA_VERSION} && \
    sdk install maven ${MAVEN_VERSION}"

CMD ["bash"]