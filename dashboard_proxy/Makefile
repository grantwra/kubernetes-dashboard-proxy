# kubernetes-dashboard-proxy Makefile

# ============================================================================
# Globals
# ============================================================================
CONTAINER_NAME:=kubernetes-dashboard-proxy
.DEFAULT_GOAL := build

# ============================================================================
# Local Development Commands
# ============================================================================
.PHONY: run
run:
	docker-compose stop
	docker-compose up

.PHONY: build
build:
	docker build -t $(CONTAINER_NAME) .

# ============================================================================
# Variables
# ============================================================================
NETWORK_HASH:=$(shell openssl rand -hex 6)

TAG:=$(shell git log -1 --pretty=format:"%H")

DOCKERHUB:=grantwra/
CONTAINER_URL:=$(DOCKERHUB)$(CONTAINER_NAME)

# ============================================================================
# Upload image
# ============================================================================
.PHONY: pushcontainer
pushcontainer:
	docker build -t $(CONTAINER_NAME) .

	docker tag $(CONTAINER_NAME):latest $(CONTAINER_URL):$(TAG)
	docker tag $(CONTAINER_URL):$(TAG) $(CONTAINER_URL):latest

	docker push $(CONTAINER_URL):latest
	docker push $(CONTAINER_URL):$(TAG)
