from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    path('AboutUs', views.AboutUsPage, name="AboutUsPage"),
    path('Products', views.ProductsPage, name="ProductsPage"),
    path('Services/Careers', views.Services_Careers, name="Careers"),
    path('Services/Careers/<Job_ID>', views.Services_Careers_Applying, name="JobApplication"),
    path('Services/Laboratory', views.Services_Laboratory, name="LaboratoryPage"),
    path('Services/TechSupport', views.Services_TechSupport, name="TechSupportPage"),
    path('Services/TechConsultation', views.Services_TechConsultation, name="TechConsultationPage"),
    path('Locations', views.LocationsPage, name="LocationPages"),
    path('ReviewForm', views.CustomerReviewFormPage, name="CustomerReviewsPage"),
    path('ShowLocation/<Location_ID>', views.ShowLocation, name="ShowLocationPage"),
    path('UpdateLocation/<Location_ID>', views.UpdateLocation, name="UpdateLocation"),
    path('DeleteLocation/<Location_ID>', views.DeleteLocation, name="DeleteLocation"),
    path('LocationPDFFile', views.LocationsPDF , name = 'LocationPDFFile'),
    path('ShowProduct/<Product_ID>', views.ShowProduct, name="ShowProductPage"),
    path('Reports', views.ReportsPage, name="Reports"),
    path('ProductTextFile', views.ProductText, name='ProductTextFile'),
    path('ProductCSVFile', views.ProductCSV, name='ProductCSVFile'),
    path('UpdateProduct/<Product_ID>', views.UpdateProduct, name="UpdateProduct"),
    path('DeleteProduct/<Product_ID>', views.DeleteProduct, name="DeleteProduct"),
    path('ProductSearch', views.ProductSearchPage, name="ProductSearchResultPage"),
    path('ProductAdd', views.ProductAddPage, name="AddProductPage"),
    path('ShoppingCart', views.ShoppingCart, name="ShoppingCart"),
    path('AdminDash/ECommerce', views.AdminDashECommerce, name="AdminDashECommerce"),
    path('AdminDash/RetailStores', views.AdminDashRetailStores, name="AdminDashRetailStores"),
    path('AdminDash/CustomerSupport', views.AdminDashCustomerSupport, name="AdminDashCustomerSupport"),
    path('AdminDash/HumanResources', views.AdminHumanResources, name="AdminHumanResources"),
    path('CustomerSupport', views.CustomerTechSupport, name="CSRPage")
]
