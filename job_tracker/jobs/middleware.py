import datetime

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log before processing view
        now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        method = request.method
        path = request.path
        print("-" * 40)
        print(f"Time : {now}")
        print(f"Method : {method}")
        print(f"Path : {path}")
        print("-" * 40)
        response = self.get_response(request)
        return response