from django.db import models
from django.contrib.auth.models import User

class SkillCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)  # 技能類別名稱 (最多10種)
    description = models.TextField(blank=True)

class Skill(models.Model):
    LEVEL_CHOICES = [(i, str(i)) for i in range(5)]  # 0~4級
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    current_level = models.IntegerField(choices=LEVEL_CHOICES, default=0)
    target_level = models.IntegerField(choices=LEVEL_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('draft', '草稿'),
        ('pending', '待審核'),
        ('approved', '已通過'),
        ('rejected', '已拒絕')
    ], default='draft')
    applied_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(User, null=True, blank=True, 
                                   on_delete=models.SET_NULL, 
                                   related_name='approved_skills')