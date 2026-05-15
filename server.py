from concurrent import futures
import time
import grpc
import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServiceServicer):
    def Sum(self, request, context):
        result = request.a + request.b
        print(f"Sum: {request.a} + {request.b} = {result}")
        return calculator_pb2.SumResponse(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(
        CalculatorServicer(), server
    )

    server.add_insecure_port("[::]:50052")
    server.start()
    print("Server started on port 50052")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped")


if __name__ == "__main__":
    serve()
