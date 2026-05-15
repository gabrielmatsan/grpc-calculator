import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50052")
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel=channel)

    request = calculator_pb2.SumRequest(a=1, b=22)

    response = stub.Sum(request=request)

    print(f"Response: {response.result}")

    fib_request = calculator_pb2.FibonacciRequest(n=10)
    print("Fibonacci stream:")
    for fib_response in stub.Fibonacci(fib_request):
        print(fib_response.result)


if __name__ == "__main__":
    run()
