from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['current_level']
    template_name = 'skill_form.html'

    def get_object(self):
        # 只能修改自己的技能
        return Skill.objects.get(employee=self.request.user, 
                               category_id=self.kwargs['category_id'])
    
    def form_valid(self, form):
        form.instance.status = 'draft'  # 修改後重置狀態
        return super().form_valid(form)


from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

class SkillRequestView(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['target_level']
    template_name = 'request_form.html'

    def form_valid(self, form):
        form.instance.status = 'pending'
        form.instance.applied_at = timezone.now()
        return super().form_valid(form)

class ApprovalListView(UserPassesTestMixin, ListView):
    model = Skill
    template_name = 'approval_list.html'

    def test_func(self):
        return self.request.user.has_perm('skills.approve_skill')

    def get_queryset(self):
        return Skill.objects.filter(status='pending')