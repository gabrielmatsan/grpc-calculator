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

    def Subtract(self, request, context):
        result = request.a - request.b
        print(f"Subtract: {request.a} - {request.b} = {result}")
        return calculator_pb2.SubtractResponse(result=result)

    def Multiply(self, request, context):
        result = request.a * request.b
        print(f"Multiply: {request.a} * {request.b} = {result}")
        return calculator_pb2.MultiplyResponse(result=result)

    def Divide(self, request, context):
        result = request.a / request.b
        print(f"Divide: {request.a} / {request.b} = {result}")
        return calculator_pb2.DivideResponse(result=result)


    def Fibonacci(self, request, context):
        a, b = 0, 1
        for _ in range(request.n):
            yield calculator_pb2.FibonacciResponse(result=a)
            a, b = b, a + b


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
