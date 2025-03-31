import pandas as pd
from django.http import HttpResponse

def export_skills_report(request):
    skills = Skill.objects.all().select_related('employee', 'category')
    df = pd.DataFrame.from_records([
        {
            '員工姓名': s.employee.username,
            '技能類別': s.category.name,
            '當前等級': s.current_level,
            '狀態': s.status
        }
        for s in skills
    ])
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="skill_report.xlsx"'
    df.to_excel(response, index=False)
    return response