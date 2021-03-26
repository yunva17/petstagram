import json
import re
import bcrypt
import jwt

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.db.models import Q

from users.models import (User)
from config.settings import SECRET_KEY, ALGORITHM

email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            name = data['name']
            email = data['email']
            username = data['username']
            password = data['password']

            if name == "":
                return JsonResponse({"message": "REQUIRED_NAME"}, status=400)
            if email == "":
                return JsonResponse({"message": "REQUIRED_PHTON_OR_EMAIL"}, status=400)
            if username == "":
                return JsonResponse({"message": "REQUIRED_USERNAME"}, status=400)
            if password == "":
                return JsonResponse({"message": "REQUIRED_PASSWORD"}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "EXISTS_EMAIL"}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"message": "EXISTS_USERNAME"}, status=400)

            if not email_regex.search(email):
                return JsonResponse({"message": "EMAIL_VALIDATION"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode(
                'utf-8'), bcrypt.gensalt()).decode('utf-8')

            print(hashed_password)
            User.objects.create(
                name=name,
                email=email,
                password=hashed_password,
                username=username
            )

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEYERROR"}, status=400)


class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)

        try:
            email = data.get('email', None)
            username = data.get('username', None)
            password = data.get('password', None)

            if not((email or username) and password):
                return JsonResponse({"message": "REQURIED"}, status=400)

            if User.objects.filter(Q(email=email) | Q(username=username)):
                user = User.objects.get(Q(email=email) | Q(username=username))
                bytes_input_pw = password.encode(
                    'utf-8')
                bytes_db_pw = user.password.encode('utf-8')
                if bcrypt.checkpw(bytes_input_pw, bytes_db_pw):
                    access_token = jwt.encode(
                        {'user': user.pk}, SECRET_KEY, algorithm=ALGORITHM)
                    return JsonResponse({"message": "SUCCESS", "TOKEN": access_token}, status=200)

                return JsonResponse({"message": "UNAUTHORIZED_APPROACH"}, status=401)

            return JsonResponse({"message": "INVALID_USER"}, status=401)

        except KeyError as ex:
            return JsonResponse({"message": "KEYERROR"+str.upper(ex.args[0])}, status=400).decode('utf-8')
