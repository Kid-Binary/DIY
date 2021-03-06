# act_project/act/website/urls_api.py
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import (
    IntroContentSingular, AboutContentSingular,
    GoalContentSingular, DisclaimerContentSingular,
    SponsorList, SponsorDetail,
    SocialList, SocialDetail,
    ActivityList, ActivityDetail,
    PartnerList,
    ProjectAreaList, ProjectAreaDetail,
    ProjectList, ProjectDetail,
    EventCategoryList, EventCategoryDetail,
    EventList, EventDetail,
    CityList, ParticipantList, ContactList, ContactDetail,
    CentreList, CentreDetail,
    CentreSubpageList, CentreSubpageDetail,
    WorksheetList,
    ScrapingList,
)

urlpatterns = [
    # Content
    url(
        r'^intro_content$',
        IntroContentSingular.as_view(),
        name='intro_content_singular'
    ),
    url(
        r'^about_content$',
        AboutContentSingular.as_view(),
        name='about_content_singular'
    ),
    url(
        r'^goal_content$',
        GoalContentSingular.as_view(),
        name='goal_content_singular'
    ),
    url(
        r'^disclaimer_content$',
        DisclaimerContentSingular.as_view(),
        name='disclaimer_content_singular'
    ),
    # Sponsor
    url(r'^sponsors$', SponsorList.as_view(), name='sponsors_list'),
    url(
        r'^sponsors/(?P<pk>[0-9]+)$',
        SponsorDetail.as_view(),
        name='sponsors_detail',
    ),
    # Social
    url(r'^socials$', SocialList.as_view(), name='socials_list'),
    url(
        r'^socials/(?P<pk>[0-9]+)$',
        SocialDetail.as_view(),
        name='socials_detail',
    ),
    # Activity
    url(r'^activities$', ActivityList.as_view(), name='activities_list'),
    url(
        r'^activities/(?P<pk>[0-9]+)$',
        ActivityDetail.as_view(),
        name='activities_detail',
    ),
    # Partner
    url(r'^partners$', PartnerList.as_view(), name='partners_list'),
    # ProjectArea
    url(
        r'^projects_areas$',
        ProjectAreaList.as_view(),
        name='projects_areas_list',
    ),
    url(
        r'^projects_areas/(?P<pk>[0-9]+)$',
        ProjectAreaDetail.as_view(),
        name='projects_areas_detail',
    ),
    # Project
    url(r'^projects$', ProjectList.as_view(), name='projects_list'),
    url(
        r'^projects/(?P<pk>[0-9]+)$',
        ProjectDetail.as_view(),
        name='projects_detail',
    ),
    # EventCategory
    url(
        r'^events_categories$',
        EventCategoryList.as_view(),
        name='events_categories_list',
    ),
    url(
        r'^events_categories/(?P<pk>[0-9]+)$',
        EventCategoryDetail.as_view(),
        name='events_categories_detail',
    ),
    # Event
    url(r'^events$', EventList.as_view(), name='events_list'),
    url(
        r'^events/(?P<pk>[0-9]+)$',
        EventDetail.as_view(),
        name='events_detail',
    ),
    # City
    url(
        r'^cities$', CityList.as_view(), name='cities_list',
    ),
    # Participant
    url(
        r'^participants$', ParticipantList.as_view(), name='participants_list',
    ),
    # Contact
    url(r'^contacts$', ContactList.as_view(), name='contacts_list'),
    url(
        r'^contacts/(?P<pk>[0-9]+)$',
        ContactDetail.as_view(),
        name='contacts_detail',
    ),
    # Centre
    url(
        r'^centres$', CentreList.as_view(), name='centres_list',
    ),
    url(
        r'^centres/(?P<pk>[0-9]+)$',
        CentreDetail.as_view(),
        name='centres_detail',
    ),
    # CentreSubpage
    url(
        r'^centres_subpages$',
        CentreSubpageList.as_view(),
        name='centres_subpages_list',
    ),
    url(
        r'^centres_subpages/(?P<pk>[0-9]+)$',
        CentreSubpageDetail.as_view(),
        name='centres_subpages_detail',
    ),
    # Worksheet
    url(
        r'^worksheets$',
        WorksheetList.as_view(),
        name='worksheets_list',
    ),
    # Scraping
    url(
        r'^scrapings$',
        ScrapingList.as_view(),
        name='scrapings_list',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
