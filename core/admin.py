from django.contrib import admin

from core.models import (AboutMe, MePhoneNumber, MeEmailAddress, Skill, Experience, Education,
                         QuestionAnswer, Profession, Project, StartProject, PhotoGallery,
                         Contact, Category, WorkSamples, LogoPartner, ClientSayAboutMe)


class MePhoneNumberInline(admin.TabularInline):
    model = MePhoneNumber
    extra = 1


class MeEmailAddressInline(admin.TabularInline):
    model = MeEmailAddress
    extra = 1


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'year_experience')
    inlines = (MePhoneNumberInline, MeEmailAddressInline)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'percent')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company_name', 'date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('grade', 'academy', 'date')


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question', 'answer')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


@admin.register(StartProject)
class StartProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'is_read')
    list_filter = ('is_read',)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'fullname', 'is_read', 'is_active')
    list_filter = ('is_active', 'is_read')
    search_fields = ('fullname', 'phone_number', 'email', 'subject', 'message')


@admin.register(Category)
class CategoryWorkSampleAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    prepopulated_fields = {"filter_tag": ('name_en',)}


@admin.register(WorkSamples)
class WorkSampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'rate')
    list_filter = ('is_active',)


@admin.register(LogoPartner)
class LogoPartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ClientSayAboutMe)
class ClientSayAboutMeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'is_active')
    list_filter = ('is_active',)
