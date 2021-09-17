from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Service(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})

class joinus(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    mobile= PhoneNumberField()
    message= models.CharField(max_length=500, blank=True)
    resume = models.ImageField(upload_to='joinus', default='default.jpg', blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-home')

service = [

('Bencho Youth Club', (
        ('1', 'Digital Service'),
        ('2', 'Business Service'),
        ('3', 'Constructions Service'),
        ('1', 'Education Help'),
        ('2', 'Research & Development'),
        ('1', 'Projects')
        )
    ),

    ('Student', (
        ('1', 'Admission'),
        ('2', 'Jobs'),
        ('3', 'Online Mentor'),
        ('1', 'Apply Online'),
        ('2', 'Jobs'),
        ('3', 'Online Learning'),
        ('1', 'NIOS Registration'),
        ('2', 'Open Distance Learning'),
        ('3', 'Online Courses'),

        )
    ),
    ('Common', (
        ('2', 'Loan Services'),
        ('2', 'Insurance Services'),
        ('3', 'Passport Services'),
        ('3', 'Bill Payments'),
        ('2', 'IRCTC, Air and Bus Ticket Services'),
        ('3', 'Aadhar Enrollment Services'),
        ('3', 'Money Transfer'),
        ('3', 'Driving Licences'),
        ('1', 'PAN Card'),
        ('1', 'Voter Id Card Services'),
        ('3', 'Bank Services'),
        ('1', 'Premium Collection Services of Insurance Companies like LIC, SBI, ICICI'),
        ('2', 'Prudential, AVIVA DHFL and Others'),
        ('3', 'E-Nagrik & E- District Services {Birth/ Death Certificate etc.}'),
        ('2', 'Pension Services'),
        ('3', 'Mobile and DTH Recharge'),
        ('3', 'CSC Bazaar'),
        ('3', 'Agriculture Services'),
        ('3', 'Apollo Telemedicine'),

        )
    ),
    ('Other', (
        ('3', 'GST/ITR Filling'),
        ('3', 'Business Startup'),
        ('3', 'Business Idea Map'),
        ('3', 'Finance'),
        ('3', 'Account Manager'),
        ('3', 'Company Name/Logo Registrations'),
        ('3', 'Entrepreneur'),
        ('3', 'Business Loan'),
        ('3', 'Business Help'),
    )
     ),
    ('Scheme', (
        ('1', 'Atmanirbhar Bharat Abhyan'),
        ('2', 'Pradhan Mantri Jan Dhan Yojana'),
        ('3', 'Pradhan Mantri Kisan Samman Nidhi Yojana (PM-Kisan Yojana)'),
        ('4', 'Pradhan Mantri Kisan Maan-Dhan Yojana'),
        ('5', 'Pradhan Mantri Shram Yogi Man-Dhan'),
        ('6', 'One Nation- One Ration Card'),
        ('7', 'Pradhan Mantri Kisan Urja Suraksha evam Utthaan Mahabhiyan (PM-KUSUM)'),
        ('8', 'Pradhan Mantri Laghu Vyapari Maan-Dhan Yojana'),
        ('9', 'Jal Jeevan Mission Scheme'),
        ('10', 'Food Safety Mitra Scheme'),
        ('11', 'Skills Acquisition and Knowledge Awareness for Livelihood (SSANKALP)'),
        ('12', 'POSHAN Abhiyan'),
        ('13', 'eSamvad portal'),
        ('14', 'Mahila e-Haat portal'),
        ('15', 'e-Krishi Samvad'),
        ('16', 'Pradhan Mantri Matru Vandana Yojana'),
        ('17', 'Vatsalya – Maatri Amrit Kosh’'),
        ('18', 'LaQshya'),
        ('19', 'Pradhan Mantri Kaushal Vikas Yojana'),
        ('20', 'Pradhan Mantri Garib Kalyan Yojana (PMGKY)'),
        ('21', 'Skill India'),
        ('22', 'PRASAD Scheme (Pilgrimage Rejuvenation And Spirituality Augmentation Drive)'),
        ('23', 'Pradhan Mantri Jan Aushadhi Yojana'),
        ('24', 'Pradhan Mantri Swasthya Suraksha Yojana'),
        ('25', 'Pradhan Mantri Mudra Yojana'),
        ('26', 'Atal Pension Yojana'),
        ('27', 'Deen Dayal Upadhyaya Gram Jyoti Yojana'),
        ('28', 'Digital India'),
        ('29', 'Make in India'),
        ('30', 'Swachh Bharat Abhiyan'),
        ('31', 'Rashtriya Gokul Mission'),
        ('32', 'Atal Pension Yojana'),
    )
     ),
    ('Digital', (
        ('1', 'Digital Marketing'),
        ('2', 'Graphic Designer'),
        ('3', 'Cloud Computing/ Cloud Hosting'),
        ('4', 'Machine Learning/Data Science/Ai/Deep learning Projects '),
        ('5', 'E-commerce/Wordpress/Templates Design/Developer'),
        ('6', 'Website/App/Software Design/Developer'),
        ('7', 'Conversion Rate Optimization (CRO)'),
        ('8', 'Social Media Management & Advertising'),
        ('9', 'Content Marketing'),
        ('10', 'Search Engine Optimization (SEO)'),
        ('11', 'Video/Photo Editing'),
        ('12', 'Affiliate Marketing'),
        ('13', 'Logo/Company Name Design'),
        ('14', 'Digital- Research & Development'),

    )
     ),
    ('Offline', (
        ('1', 'Computer Repair Service'),
        ('2', 'Production House- Services'),
        ('3', 'Constructions Work'),
        ('4', 'Interior Design'),
        ('5', 'Video/Photo Shoot'),
        ('6', 'Research & Development'),
        ('7', 'Electrician'),
        ('8', 'Plumber Work'),
        ('9', 'Event Manager'),
        ('10', 'Photographer/ videographer'),
        ('11', 'Mechanical Engineer'),
        ('12', 'Market Research'),
    )
     ),
]

class Dataform(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    sender = models.EmailField(blank=True)
    message = models.CharField(max_length=1000)
    servic = models.CharField(max_length = 20, choices = service, default = '1')
    upload = models.ImageField(upload_to ='uploads', default='default.jpg', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-home')


class track(models.Model):
    bookid = models.IntegerField(primary_key=True)
    tra = models.ForeignKey(Dataform, on_delete=models.CASCADE)
    trackmsg= models.CharField(max_length=500)
    link = models.URLField(max_length=200, blank=True)
    images = models.ImageField(upload_to='images', default='default.jpg')

    def __str__(self):
        return self.trackmsg