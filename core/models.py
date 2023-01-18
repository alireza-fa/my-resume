from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from utils.managers import IsActiveManager


# About Me
class AboutMe(models.Model):
    name = models.CharField(max_length=34, verbose_name=_('name'))
    name_en = models.CharField(max_length=34, verbose_name=_('name english'))
    address = models.CharField(max_length=120, verbose_name=_('address'))
    address_en = models.CharField(max_length=120, verbose_name=_('address en'))
    profession = models.CharField(max_length=64, verbose_name=_('profession'))
    profession_en = models.CharField(max_length=64, verbose_name=_('profession english'))
    describe_short = models.CharField(max_length=200, verbose_name=_('describe short'))
    describe_short_en = models.CharField(max_length=200, verbose_name=_('describe short english'))
    describe = models.TextField(verbose_name=_('describe'))
    describe_en = models.TextField(verbose_name=_('describe english'))
    resume = models.FileField(verbose_name=_('resume'))
    image = models.ImageField(verbose_name=_('image'), help_text=_('recommended: Image(600X673)'))
    logo = models.ImageField(
        default='logo.png', verbose_name=_('logo'), help_text=_('recommended: Image(300X75)'))
    logo2 = models.ImageField(
        default='logo-2.png', verbose_name=_('logo 2'), help_text=_('recommended: Image(300X75)'))
    year_experience = models.PositiveSmallIntegerField(verbose_name=_('years of experience'))
    customer_count = models.PositiveIntegerField(verbose_name=_('customer count'))
    tea_count = models.PositiveIntegerField(verbose_name=_('tea count'))
    project_count = models.PositiveIntegerField(verbose_name=_('project count'))

    class Meta:
        verbose_name = _('About Me')
        verbose_name_plural = _('About Me')

    def __str__(self):
        return self.name


class MePhoneNumber(models.Model):
    me = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='phone_numbers', verbose_name=_('me'))
    phone_number = models.CharField(max_length=18, verbose_name=_('phone_number'))

    class Meta:
        verbose_name = _('Me Phone Number')
        verbose_name_plural = _('Me Phone Numbers')

    def __str__(self):
        return f'{self.me} - {self.phone_number}'


class MeEmailAddress(models.Model):
    me = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='emails', verbose_name=_('me'))
    email = models.EmailField(max_length=150, verbose_name=_('email'))

    class Meta:
        verbose_name = _('Me Email Address')
        verbose_name_plural = _('Me Email Addresses')

    def __str__(self):
        return f'{self.me} - {self.email}'


class Skill(models.Model):
    name = models.CharField(max_length=34, verbose_name=_('name'))
    name_en = models.CharField(max_length=34, verbose_name=_('name english'))
    percent = models.PositiveSmallIntegerField(
        verbose_name=_('percent'),
        validators=[validators.MinValueValidator(1, message=_('percent must be greater than 1')),
                    validators.MaxValueValidator(100, message=_('percent must be lesser than 100'))])

    class Meta:
        verbose_name = _('Skil')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return f'{self.name} - {self.percent}'


class Experience(models.Model):
    position = models.CharField(max_length=34, verbose_name=_('name'))
    position_en = models.CharField(max_length=34, verbose_name=_('name english'))
    company_name = models.CharField(max_length=64, verbose_name=_('academy'))
    company_name_en = models.CharField(max_length=64, verbose_name=_('academy english'))
    date = models.CharField(max_length=34, verbose_name=_('date'))
    date_en = models.CharField(max_length=34, verbose_name=_('date english'))

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')

    def __str__(self):
        return f'{self.position} - {self.company_name}'


class Education(models.Model):
    grade = models.CharField(max_length=34, verbose_name=_('name'))
    grade_en = models.CharField(max_length=34, verbose_name=_('name english'))
    academy = models.CharField(max_length=64, verbose_name=_('academy'))
    academy_en = models.CharField(max_length=64, verbose_name=_('academy english'))
    date = models.CharField(max_length=34, verbose_name=_('date'))
    date_en = models.CharField(max_length=34, verbose_name=_('date english'))

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')

    def __str__(self):
        return f'{self.grade} {self.academy}'


# FQA
class QuestionAnswer(models.Model):
    question = models.CharField(max_length=150, verbose_name=_('question'))
    answer = models.TextField(verbose_name=_('answer'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Question And Answer')
        verbose_name_plural = _('Questions And Answers')

    def __str__(self):
        return self.question


# Service
class Profession(models.Model):
    LAPTOP = 'fa-laptop-code'
    OBJECT = 'fa-object-ungroup'
    PALETTE = 'fa-palette'
    CAMERA = 'fa-camera-retro'
    FILM = 'fa-film'
    BULLHORN = 'fa-bullhorn'

    PROFESSION_TYPE_CHOICES = (
        (LAPTOP, _('Laptop, programming and ...')),
        (OBJECT, _('Object, UI Designer and ...')),
        (PALETTE, _('Palette, Logo Designer and ...')),
        (CAMERA, _('Camera, Photography and ...')),
        (FILM, _('Film, Movie Edit and ...')),
        (BULLHORN, _('Bullhorn, Social Media and ...')),
    )

    name = models.CharField(max_length=34, verbose_name=_('name'))
    name_en = models.CharField(max_length=34, verbose_name=_('name english'))
    type = models.CharField(max_length=34, choices=PROFESSION_TYPE_CHOICES, verbose_name=_('type'))
    description = models.CharField(max_length=250, verbose_name=_('description'))

    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Professions')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=34, verbose_name=_('name'))
    name_en = models.CharField(max_length=34, verbose_name=_('name english'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    price_one_project = models.CharField(max_length=10, verbose_name=_('price based on a project'))
    price_one_project_en = models.CharField(max_length=10, verbose_name=_('price based on a project *dollar*'))

    price_many_project = models.CharField(max_length=10, verbose_name=_('price based on many project'))
    price_many_project_en = models.CharField(max_length=10, verbose_name=_('price based on many project *dollar*'))

    price_one_day = models.CharField(max_length=10, verbose_name=_('price based on the day'))
    price_one_day_en = models.CharField(max_length=10, verbose_name=_('price based on the day *dollar*'))

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name


class StartProject(models.Model):
    name = models.CharField(max_length=34, verbose_name=_('name'))
    phone_number = models.CharField(max_length=18, verbose_name=_('phone number'))
    email = models.EmailField(max_length=150, verbose_name=_('email'))
    subject = models.CharField(max_length=34, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    created = models.DateTimeField(default=timezone.now(), verbose_name=_('created'))
    is_read = models.BooleanField(default=False, verbose_name=_('is read'))

    class Meta:
        verbose_name = _('Start Project')
        verbose_name_plural = _('Start Projects')
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name} - {self.subject}'


# Gallery
class PhotoGallery(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    image = models.ImageField(verbose_name=_('image'))
    is_active = models.BooleanField(verbose_name=_('is active'))

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Photo Gallery')
        verbose_name_plural = _('Photo Galleries')

    def __str__(self):
        return self.name


# Contact
class Contact(models.Model):
    fullname = models.CharField(max_length=64, verbose_name=_('fullname'))
    phone_number = models.CharField(max_length=18, verbose_name=_('phone number'))
    email = models.CharField(max_length=150, verbose_name=_('email'))
    subject = models.CharField(max_length=120, error_messages=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    is_read = models.BooleanField(default=False, verbose_name=_('is read'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_created=True)

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        ordering = ('-created',)

    def __str__(self):
        return f'{self.fullname} - {self.subject}'


# Portfolio
class Category(models.Model):
    name = models.CharField(max_length=34, verbose_name=_('name'))
    name_en = models.CharField(max_length=34, verbose_name=_('name english'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class WorkSamples(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('title'))
    title_en = models.CharField(max_length=64, verbose_name=_('title'))
    category = models.OneToOneField(
        Category, on_delete=models.CASCADE, related_name='work_sample', verbose_name=_('category'))
    image = models.ImageField(verbose_name=_('image'), help_text=_('recommended: Image(420X260)'))
    start_at = models.CharField(max_length=34, verbose_name=_('start at'))
    end_at = models.CharField(max_length=34, verbose_name=_('end at'))
    rate = models.PositiveSmallIntegerField(
        verbose_name=_('rate'),
        validators=[validators.MinValueValidator(1, 'rate must be greater than or equal 0'),
                    validators.MaxValueValidator(5, 'rate must be lesser than or equal 5')]
    )
    website_url = models.CharField(max_length=250, verbose_name=_('website url'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Work Sample')
        verbose_name_plural = _('Work Samples')

    def __str__(self):
        return self.title


class LogoPartner(models.Model):
    name = models.CharField(max_length=34, verbose_name=_('name'))
    image = models.ImageField(verbose_name=_('image'), help_text=_('recommended: Image(180X17)'))

    class Meta:
        verbose_name = _('Logo Partner')
        verbose_name_plural = _('Logo Partners')

    def __str__(self):
        return self.name


class ClientSayAboutMe(models.Model):
    fullname = models.CharField(max_length=34, verbose_name=_('fullname'))
    position = models.CharField(max_length=64, verbose_name=_('position'))
    image = models.ImageField(verbose_name=_('image'), help_text=_('recommended: Image(400X400)'))
    description = models.TextField(verbose_name=_('description'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created = models.DateTimeField(auto_now_add=True)

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Client Says About Me')
        verbose_name_plural = _('Clients Says About Me')

    def __str__(self):
        return f'{self.fullname} - {self.position}'
