from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """
    BaseUserManager에서 정보 가져와서 필요한 부분 수정
    """
    def create_user(self, email, car_number, phone_number, parking_number, password=None):
        if not phone_number:
            raise ValueError('must have user email')
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            car_number=car_number,
            parking_number=parking_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, car_number, phone_number, parking_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            email=self.normalize_email(email),
            car_number=car_number,
            parking_number = parking_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """
    실제 생성할 User 테이블 설정, 위에 만든 UserManager 참고함

    phone_number : 전화번호, 최대길이 20, 중복불가, - 없이 입력
    email : 이메일, 최대길이 255, 중복불가, 이메일 형식 지켜야함
    car_number : 차량번호, 최대길이 20, 공백없음 + replace(" ", "")으로 공백제거
    parking_number : 주차공간번호, 외래키, Parking 테이블과 연결, 삭제되면 NULL로 변경, NULL 저장 가능, 폼 양식 비우기 가능
    """
    phone_number = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=255,unique=True)
    car_number = models.CharField(max_length=20)
    parking_number = models.ForeignKey("Parking", on_delete=models.SET_NULL, db_column='parking_number', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','car_number','parking_number']
    
    def __str__(self):
        return self.phone_number
        
def has_perm(self, perm, obj=None):
    """
    True를 반환하여 권한이 있음을 알림
    Ojbect를 반환하는 경우 해당 Object로 사용 권한을 확인하는 절차가 필요
    """
    return True

def has_module_perms(self, app_label):
    """
    True를 반환하여 주어진 앱(App)의 모델(Model)에 접근 가능하도록 함
    """
    return True

@property
def is_staff(self):
    """
    True가 반환되면 장고(django)의 관리자 화면에 로그인 할 수 있음
    """
    return self.is_admin


class Parking(models.Model):
    """
    주차공간 테이블 생성

    parking_number : 주차공간번호, 최대길이 20, 기본키(=NULL안됨, 중복안됨)
    lat : 위도, 최대길이 20
    lon : 경도, 최대길이 20
    res_state : 예약가능상태, 최대길이 20, ON/OFF로 상태 표기
    detail_add : 상세주소, 최대길이 255, NULL 저장 가능, 폼 양식 비우기 가능
    finish_car_number : 등록된 차량번호, 최대길이 20, NULL 저장 가능
    parking_car_number : 주차된 차량번호, 최대길이 20, NULL 저장 가능
    """
    parking_number = models.CharField(max_length=20, primary_key=True)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    res_state = models.CharField(max_length=20)
    detail_add = models.CharField(max_length=255, null=True, blank=True)
    finish_car_number = models.CharField(max_length=20, null=True)
    parking_car_number = models.CharField(max_length=20, null=True)


class Res(models.Model):
    """
    예약 테이블 생성

    phone_number : 전화번호, 외래키, User 테이블과 연결
    """
    phone_number = models.ForeignKey("User", on_delete=models.SET_NULL, db_column='phone_number', null=True, blank=True)
    parking_number = models.ForeignKey("Parking", on_delete=models.SET_NULL, db_column='parking_number', null=True, blank=True)
    time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=100)
    res_car_number = models.CharField(max_length=20)
