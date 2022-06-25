from django.urls import path
import reviews.views


urlpatterns = [
    path('', reviews.views.index),
    path('book-search', reviews.views.book_search),

]
