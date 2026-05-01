from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ActionForm, AgendaForm
from .models import Action, Agenda


class ActionListView(LoginRequiredMixin, ListView):
    model = Action
    template_name = 'core/action_list.html'


class ActionCreateView(LoginRequiredMixin, CreateView):
    model = Action
    form_class = ActionForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('action-list')


class ActionUpdateView(LoginRequiredMixin, UpdateView):
    model = Action
    form_class = ActionForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('action-list')


class ActionDeleteView(LoginRequiredMixin, DeleteView):
    model = Action
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('action-list')


class AgendaListView(LoginRequiredMixin, ListView):
    model = Agenda
    template_name = 'core/agenda_list.html'


class AgendaCreateView(LoginRequiredMixin, CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('agenda-list')


class AgendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('agenda-list')


class AgendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Agenda
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('agenda-list')
