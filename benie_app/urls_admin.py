from django.contrib import admin 
from django.urls import path, re_path as url 
from benie_app import views 

# url patterns/configurations 
urlpatterns = [
    url(r'^contacts/all$',views.Contacts.as_view(),name='contacts'),
    url(r'^contact/details/(\d+)$',views.ContactDetails.as_view(),name='contact-details'),
    url(r'^subscriber/details/(\d+)$',views.SubscriberDetails.as_view(),name='subscriber-details'),
    url(r'^stories/add$',views.AddStory.as_view(),name='add-story'),
    url(r'^story/update/(\d+)$',views.UpdateStory.as_view(),name='update-story'),
    url(r'^chapters/add$',views.AddChapter.as_view(),name='add-chapter'),
    url(r'^chapter/update/(\d+)$',views.UpdateChapter.as_view(),name='update-chapter'),
    url(r'^pages/all$',views.AllPages.as_view(),name='all-pages'),
    url(r'^pages/add$',views.AddPage.as_view(),name='add-page'),
    url(r'^page/update/(\d+)$',views.UpdatePage.as_view(),name='update-page'),
    url(r'^tags/add$',views.AddTag.as_view(),name='add-tag'),
    url(r'^tag/details/(\d+)$',views.TagDetails.as_view(),name='tag-details'),
    url(r'^poems/add$',views.AddPoem.as_view(),name='add-poem'),
    url(r'^poem/update/(\d+)$',views.UpdatePoem.as_view(),name='update-poem'),
    url(r'^notification/details/(\d+)$',views.NotificationDetails.as_view(),name='notification-details'),
    url(r'^reaction/details/(\d+)$',views.ReactionDetails.as_view(),name='reaction-details'),
]