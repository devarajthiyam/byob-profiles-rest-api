from django.db import models


class LodgeDetail(models.Model):
    """Detail information of Lodge"""

    lodge_name = models.CharField(max_length=255)
    lodge_address = models.CharField(max_length=255)
    lodge_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.lodge_name


class RoomDetail(models.Model):
    """Detail information of rooms of a Lodge"""

    lodge_detail = models.ForeignKey('LodgeDetail', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=3)
    room_type = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_no
