from rest_framework.response import Response

class Res():

    @classmethod
    def build(cls, status, success, msg, data):
        return Response({"success":success, "msg":msg, "data":data}, status=status)

    @classmethod
    def success(cls, msg, data):
        return cls.build(200, True, msg, data)

    @classmethod
    def fail(cls, status, msg):
        return cls.build(status, False, msg, None)
