# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0025_new_follow_pages_page_xpath_pagination_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checker',
            name='checker_type',
            field=models.CharField(choices=[('4', '404'), ('X', '404_OR_X_PATH')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='checker',
            name='scraped_obj_attr',
            field=models.ForeignKey(help_text='Attribute of type DETAIL_PAGE_URL, several checkers for same DETAIL_PAGE_URL attribute possible.', on_delete=django.db.models.deletion.CASCADE, to='dynamic_scraper.ScrapedObjAttr'),
        ),
        migrations.AlterField(
            model_name='log',
            name='level',
            field=models.IntegerField(choices=[(50, 'CRITICAL'), (40, 'ERROR'), (30, 'WARNING'), (20, 'INFO'), (10, 'DEBUG')]),
        ),
        migrations.AlterField(
            model_name='logmarker',
            name='mark_with_type',
            field=models.CharField(choices=[('PE', 'Planned Error'), ('DD', 'Dirty Data'), ('IM', 'Important'), ('IG', 'Ignore'), ('MI', 'Miscellaneous'), ('CU', 'Custom')], help_text='Choose "Custom" and enter your own type in the next field for a custom type', max_length=2),
        ),
        migrations.AlterField(
            model_name='requestpagetype',
            name='content_type',
            field=models.CharField(choices=[('H', 'HTML'), ('X', 'XML'), ('J', 'JSON')], default='H', help_text='Data type format for scraped pages of page type (for JSON use JSONPath instead of XPath)', max_length=1),
        ),
        migrations.AlterField(
            model_name='requestpagetype',
            name='dont_filter',
            field=models.BooleanField(default=False, help_text='Do not filter duplicate requests, useful for some scenarios with requests falsely marked as being duplicate (e.g. uniform URL + pagination by HTTP header).'),
        ),
        migrations.AlterField(
            model_name='requestpagetype',
            name='meta',
            field=models.TextField(blank=True, help_text='Optional Scrapy meta attributes as JSON dict (use double quotes!), see Scrapy docs for reference.'),
        ),
        migrations.AlterField(
            model_name='requestpagetype',
            name='method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST')], default='GET', help_text='HTTP request via GET or POST.', max_length=10),
        ),
        migrations.AlterField(
            model_name='requestpagetype',
            name='render_javascript',
            field=models.BooleanField(default=False, help_text='Render Javascript on pages (ScrapyJS/Splash deployment needed, careful: resource intense)'),
        ),
        migrations.AlterField(
            model_name='requestpagetype',
            name='request_type',
            field=models.CharField(choices=[('R', 'Request'), ('F', 'FormRequest')], default='R', help_text='Normal (typically GET) request (default) or form request (typically POST), using Scrapys corresponding request classes (not used for checker).', max_length=1),
        ),
        migrations.AlterField(
            model_name='requestpagetype',
            name='scraped_obj_attr',
            field=models.ForeignKey(blank=True, help_text='Empty for main page, attribute of type DETAIL_PAGE_URL scraped from main page for detail pages.', null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic_scraper.ScrapedObjAttr'),
        ),
        migrations.AlterField(
            model_name='schedulerruntime',
            name='runtime_type',
            field=models.CharField(choices=[('S', 'SCRAPER'), ('C', 'CHECKER')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='scrapedobjattr',
            name='attr_type',
            field=models.CharField(choices=[('S', 'STANDARD'), ('T', 'STANDARD (UPDATE)'), ('B', 'BASE'), ('U', 'DETAIL_PAGE_URL'), ('I', 'IMAGE')], max_length=1),
        ),
        migrations.AlterField(
            model_name='scrapedobjclass',
            name='checker_scheduler_conf',
            field=models.TextField(default='"MIN_TIME": 1440,\n"MAX_TIME": 10080,\n"INITIAL_NEXT_ACTION_FACTOR": 1,\n"ZERO_ACTIONS_FACTOR_CHANGE": 5,\n"FACTOR_CHANGE_FACTOR": 1.3,\n'),
        ),
        migrations.AlterField(
            model_name='scrapedobjclass',
            name='scraper_scheduler_conf',
            field=models.TextField(default='"MIN_TIME": 15,\n"MAX_TIME": 10080,\n"INITIAL_NEXT_ACTION_FACTOR": 10,\n"ZERO_ACTIONS_FACTOR_CHANGE": 20,\n"FACTOR_CHANGE_FACTOR": 1.3,\n'),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='max_items_read',
            field=models.IntegerField(blank=True, help_text='Max number of items to be read (empty: unlimited).', null=True),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='max_items_save',
            field=models.IntegerField(blank=True, help_text='Max number of items to be saved (empty: unlimited).', null=True),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='pagination_append_str',
            field=models.CharField(blank=True, help_text='Syntax: /somepartofurl/{page}/moreurlstuff.html', max_length=200),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='pagination_page_replace',
            field=models.TextField(blank=True, help_text="RANGE_FUNCT: uses Python range funct., syntax: [start], stop[, step], FREE_LIST: 'Replace text 1', 'Some other text 2', 'Maybe a number 3', ..."),
        ),
    ]
