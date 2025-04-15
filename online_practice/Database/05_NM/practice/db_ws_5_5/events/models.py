from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    participants = models.ManyToManyField('Participant', through='Attendance')
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)
    num_of_participants = models.IntegerField()
    events = models.ManyToManyField('Event', through='Attendance')
    

    def __str__(self):
        return self.name

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    check_in = models.TimeField()
    check_out = models.TimeField()
    total_fee = models.IntegerField()

    def __str__(self):
        return f'{self.participant} - {self.event}'
    
    def save(self, *args, **kwargs):
        # 여기서 다른 모델(Product)의 필드(product.price)를 참조함
        self.total_fee = self.participant.num_of_participants * self.event.price
        super().save(*args, **kwargs)