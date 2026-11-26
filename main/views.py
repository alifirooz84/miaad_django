from django.shortcuts import render
from django.http import HttpResponse


def carbon_s195_view(request):
    return render(request, 'products/carbon-s195.html')

def carbon_h128_view(request):
    return render(request, 'products/carbon-h128.html')

def carbon_h118_view(request):
    return render(request, 'products/carbon-h118.html')

def ceramic_liner_view(request):
    return render(request, 'products/ceramic-liner.html')

def wind_turbine_view(request):
    return render(request, 'products/wind-turbine-blade.html')

def grid_resistor_view(request):
    return render(request, 'products/grid-resistor.html')

# مقالات تخصصی مهندسی و متالورژی
def article_dc_motor_view(request):
    return render(request, 'articles/dc-motor-carbon-brush.html')

def article_ceramic_liner_view(request):
    return render(request, 'articles/ceramic-liner-vs-hardox.html')

def article_belaz_wheel_motor_view(request):
    return render(request, 'articles/belaz-wheel-motor-carbon.html')

# سئو: فایل robots.txt برای خزنده‌های گوگل
def robots_txt_view(request):
    content = """User-agent: *
Allow: /
Disallow: /admin/

Sitemap: https://miaadsanatsirjan.ir/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")

# سئو: نقشه سایت sitemap.xml برای ایندکس سریع تمام صفحات و مقالات
def sitemap_xml_view(request):
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://miaadsanatsirjan.ir/</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://miaadsanatsirjan.ir/en/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <!-- محصولات -->
    <url>
        <loc>https://miaadsanatsirjan.ir/products/carbon-s195/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://miaadsanatsirjan.ir/products/carbon-h128/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://miaadsanatsirjan.ir/products/carbon-h118/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://miaadsanatsirjan.ir/products/ceramic-liner/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <!-- مقالات تخصصی و دانشنامه -->
    <url>
        <loc>https://miaadsanatsirjan.ir/articles/dc-motor-carbon/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.85</priority>
    </url>
    <url>
        <loc>https://miaadsanatsirjan.ir/articles/ceramic-liner/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.85</priority>
    </url>
    <url>
        <loc>https://miaadsanatsirjan.ir/articles/belaz-wheel-motor/</loc>
        <changefreq>weekly</changefreq>
        <priority>0.85</priority>
    </url>
</urlset>
"""
    return HttpResponse(xml_content, content_type="application/xml")

def home_fa(request):
    return render(request, 'index.html')

def home_en(request):
    return render(request, 'indexen.html')
