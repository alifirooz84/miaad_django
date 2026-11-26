from django.urls import path
from . import views

urlpatterns = [
    # فایل‌های سئو برای موتورهای جستجو و گوگل
    path('robots.txt', views.robots_txt_view, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml_view, name='sitemap_xml'),

    # محصولات
    path('products/carbon-s195/', views.carbon_s195_view, name='carbon_s195'),
    path('products/carbon-h128/', views.carbon_h128_view, name='carbon_h128'),
    path('products/carbon-h118/', views.carbon_h118_view, name='carbon_h118'),
    path('products/ceramic-liner/', views.ceramic_liner_view, name='ceramic_liner'),
    path('products/wind-turbine/', views.wind_turbine_view, name='wind_turbine'),
    path('products/grid-resistor/', views.grid_resistor_view, name='grid_resistor'),
    
    # مقالات تخصصی و دانشنامه مهندسی
    path('articles/dc-motor-carbon/', views.article_dc_motor_view, name='article_dc_motor'),
    path('articles/ceramic-liner/', views.article_ceramic_liner_view, name='article_ceramic_liner'),
    path('articles/belaz-wheel-motor/', views.article_belaz_wheel_motor_view, name='article_belaz_wheel_motor'),

    # صفحات اصلی
    path('', views.home_fa, name='home'),          # صفحه اصلی فارسی
    path('fa/', views.home_fa, name='home_fa'),     # لینک برگشت از سوییچر زبان
    path('en/', views.home_en, name='home_en'),
]
