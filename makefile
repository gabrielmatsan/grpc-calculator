PROTO_DIR := .
PROTO_FILES := $(wildcard $(PROTO_DIR)/*.proto)
GENERATED := $(PROTO_FILES:.proto=_pb2.py) $(PROTO_FILES:.proto=_pb2.pyi) $(PROTO_FILES:.proto=_pb2_grpc.py)

.PHONY: proto server client clean help
# uv run python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. *.proto
help:
	@echo "Targets:"
	@echo "  proto   - Generate Python code from .proto files"
	@echo "  server  - Run the gRPC server"
	@echo "  client  - Run the gRPC client"
	@echo "  clean   - Remove generated proto files"

proto:
	uv run python -m grpc_tools.protoc \
		-I$(PROTO_DIR) \
		--python_out=$(PROTO_DIR) \
		--pyi_out=$(PROTO_DIR) \
		--grpc_python_out=$(PROTO_DIR) \
		$(PROTO_FILES)

server:
	uv run python server.py

client:
	uv run python client.py

clean:
	rm -f $(GENERATED)
