from rest_framework.response import Response

class Res():

    @classmethod
    def build(cls, status, msg, data):
        success = False
        if status == 200:
            success = True
        return Response({"success":success, "msg":msg, "data":data}, status=status)

    @classmethod
    def success(cls, msg, data):
        return cls.build(200, msg, data)

    @classmethod
    def fail(cls, status, msg):
        return cls.build(status, msg, None)
