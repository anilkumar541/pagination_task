from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# Django provides a few classes that help you manage paginated data – that is, data that’s 
# split across several pages, with “Previous/Next” links.

#we created a seprate pagination file for we can use per view pagination

class MyPageNumberPagination(PageNumberPagination):

    page_size =10 #only 10 records will show per page
    page_query_param="zzz"  #will change the name of page=2 now we have to write zzz=2
    page_size_query_param ="records" #using this attribute client can decide how many records show per page 
                                # example: ?page=1&records=6 now client will see only 6 records per page
    max_page_size=5 #nobody can see more than 5 records per page                            
    last_page_strings="end" #to go the last page we need to  write page=end but by default page=last works

class TestLimitOffsetPagination(LimitOffsetPagination):
    # when we want to see the records from 10 number then we use offset pagination
    # /?limit=2&offset=5 will show only 2 records per page but from 6th record bcoz of offset=5
    default_limit=5 #will show only 2 records per page
    max_limit=3 #nobody can see more than 3 records per page  

class TestCursorPagination(CursorPagination):
    # we get ordering, next and previous features in cursor_pagination
    page_size=10 #3 records per page
    ordering="text" #order by text