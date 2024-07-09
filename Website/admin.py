from .models import *
from .resources import *
from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# admin.site.unregister(Group)
# @admin.register(Group)
# class AnyName(ImportExportModelAdmin): == Starting Code For Mass Importing & Exporting the Data Models
#admin.site.register(Data_Model_Class_Name, Admin_Class_Name) == Ending Code For Mass Importing & Exporting the Data Models


# @admin.register(Pictures)
# class AdminPictures(admin.ModelAdmin):
class AdminPictures(ImportExportModelAdmin):
    fields = ('Name', 'Image', 'Custom_File')
    list_display = ('Name',)
    
# For Mass Importing & Exporting the Picture Data
admin.site.register(Pictures, AdminPictures)


# @admin.register(StoreProducts)
# class AdminProducts(admin.ModelAdmin):
class AdminProducts(ImportExportModelAdmin):
    resource_class = StoreProductImports
    # fields = ('Name', 'Brand', 'Price', 'UPC', 'SKU', 'Stock', 'Summary', 'Key_Feat_1', 'Key_Feat_2',
    #         'Key_Feat_3', 'Key_Feat_4', 'Key_Feat_5', 'Key_Feat_6', 'Key_Feat_7', 'Key_Feat_8', 'Key_Feat_9',
    #         'Key_Feat_10', 'Picture', 'Spec_Sheet', 'Coupon', 'Category', 'Discontinued')
    list_filter = ('Brand', 'Name', 'Stock', 'Coupon',)
    list_display = ('Brand', 'Name', 'Summary', 'Key_Feat_1', 'Category')
    ordering = ('Name',)
    search_fields = ('Name', 'Stock')

admin.site.register(StoreProducts, AdminProducts)

# #     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     Product = models.ForeignKey(StoreProducts, null=True, blank=False, on_delete=models.CASCADE)
#     Amount = models.IntegerField(default=0)
#     Added_To_Cart = models.DateTimeField(auto_now_add=True)
#     Payment_Date = models.DateTimeField(auto_now_add=True)
#     Payment_Status = models.CharField(max_length=255, blank=True)
    
class AdminShoppingCarts(ImportExportModelAdmin):
    fields = ('User', 'Products', 'Amount', 'Added_To_Cart', 'Payment_Date', 'Payment_Status')
    list_filter = ('User',)
    list_display = ('User', 'Amount', 'Added_To_Cart', 'Payment_Date', 'Payment_Status')
    ordering = ('User',)
    search_fields = ('User', 'Products',)
    
admin.site.register(ShoppingCart, AdminShoppingCarts)

# class AdminPayPalPayments(ImportExportModelAdmin):
#     fields = ('User', 'Amount', 'Payment_Status',)
#     list_filter = ('User', 'Payment_Status',)
#     list_display = ('User', 'Amount', 'Payment_Status',)
#     ordering = ('User',)
#     search_fields = ('User','Payment_Status',)
    
# admin.site.register(PayPalPayment, AdminPayPalPayments)



# @admin.register(StoreLocations)
# class AdminLocations(admin.ModelAdmin):
class AdminLocations(ImportExportModelAdmin):
    fields = ('Street', 'City', 'State', 'Zip', 'Phone', 'Opens', 'Closes', 'Store_Image')
    list_display = ('Street', 'City', 'State', 'Zip')
    ordering = ('Street', )
    
admin.site.register(StoreLocations, AdminLocations)


# @admin.register(CouponDiscount)
# class AdminCouponDiscount(admin.ModelAdmin):
class AdminCouponDiscount(ImportExportModelAdmin):
    fields = ('CouponName', 'Discount', 'Description', 'StartDate', 'EndDate', 'Promo_Code_Image')
    list_display = ('CouponName', 'Discount')
    ordering = ('CouponName', )
    
admin.site.register(CouponDiscount, AdminCouponDiscount)


# @admin.register(CustomerReviews)
# class AdminCustomerReviews(admin.ModelAdmin):
class AdminCustomerReviews(ImportExportModelAdmin):
    fields = ('ShoppingDate', 'ReviewScore', 'TotalReview',)
    list_display = ('ShoppingDate', 'ReviewScore')
    ordering = ('-ReviewScore', )

admin.site.register(CustomerReviews, AdminCustomerReviews)
    
    
# @admin.register(FAQ)
# class AdminFAQ(admin.ModelAdmin):
class AdminFAQ(ImportExportModelAdmin):
    # resource_class = AdminFAQImports
    fields = ('Question_Type', 'Question', 'Answer')
    list_display = ('Question_Type', 'Question', 'Answer',)
    
admin.site.register(FAQ, AdminFAQ)
    
    
# @admin.register(CustomerSupportTickets)
# class AdminCustomerSupportTickets(admin.ModelAdmin):
class AdminCustomerSupportTickets(ImportExportModelAdmin):
    fields = ('Email', 'Inquiry', 'Answered')
    list_display = ('Email', 'Answered')
    ordering = ('Answered',)
    
admin.site.register(CustomerSupportTickets, AdminCustomerSupportTickets)
    
    
# @admin.register(CustomerTestimonials)
# class AdminCustomerTestimonials(admin.ModelAdmin):
class AdminCustomerTestimonials(ImportExportModelAdmin):
    fields = ('First_Name', 'About', 'Testimonial')
    list_display = ('About',)
    
admin.site.register(CustomerTestimonials, AdminCustomerTestimonials)
    
    
# @admin.register(ReusableData)
# class AdminConstEmploymentData(admin.ModelAdmin):
class AdminKeyRespons(ImportExportModelAdmin):
    fields = ('Title', 'EEOS', 'First_Benefit', 'Second_Benefit', 'Third_Benefit')
    list_display = ('Title',)
    
admin.site.register(ReusableData, AdminKeyRespons)    

# @admin.register(Key_Respons)
# class AdminKeyRespons(admin.ModelAdmin):
class AdminKeyRespons(ImportExportModelAdmin):
    fields = ('Job', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth')
    list_display = ('Job',)
    ordering = ('Job',)

admin.site.register(Key_Respons, AdminKeyRespons)
    
# @admin.register(JobApplications)
# class AdminJobApplications(admin.ModelAdmin):
class AdminJobApplications(ImportExportModelAdmin):
    fields = ('First_Name', 'Last_Name', 'DesiredJob', 'Phone_Number', 'Email_Address', 'Resume', 'Cover_Letter')
    list_display = ('First_Name', 'Last_Name', 'Email_Address',)
    ordering = ('First_Name',)
    
admin.site.register(JobApplications, AdminJobApplications)
    
# @admin.register(Employment)
# class AdminEmployment(admin.ModelAdmin):
class AdminEmployment(ImportExportModelAdmin):
    fields = ('Title', 'Description', 'EEOS_And_Benefits', 'Key_Responsibilities', 'Salary', 'Location_Type', 'Store_Location', 'Filled')
    list_display = ('Title', 'Filled', 'Location_Type', 'Store_Location')
    ordering = ('Filled',)

admin.site.register(Employment, AdminEmployment)
    
    
# @admin.register(EmergencyContact)
# class AdminEmergencyContacts(admin.ModelAdmin):
class AdminEmergencyContacts(ImportExportModelAdmin):
    fields = ('First_Name', 'Last_Name', 'Phone_Number', 'Email_Address')
    list_display = ('First_Name', 'Last_Name', 'Phone_Number', 'Email_Address')
    ordering = ('First_Name',)
    
admin.site.register(EmergencyContact, AdminEmergencyContacts)

# @admin.register(CurrentEmployees)
# class AdminCurrentEmployees(admin.ModelAdmin):
class AdminCurrentEmployees(ImportExportModelAdmin):
    fields = ('First_Name', 'Last_Name', 'Job', 'Date_Of_Birth', 'Social_Security', 'Street_Address', 'City_Address', 'State_Address', 'W2_Tax_Information', 'Emergency_Contact', 'Employment_Contract')
    list_display = ('First_Name', 'Last_Name', 'Job',)
    ordering = ('First_Name',)
    
admin.site.register(CurrentEmployees, AdminCurrentEmployees)