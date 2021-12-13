from rest_framework.pagination import PageNumberPagination

# Django provides a few classes that help you manage paginated data – that is, data that’s 
# split across several pages, with “Previous/Next” links.

#we created a seprate pagination file for we can use per view pagination

class MyPageNumberPagination(PageNumberPagination):
    page_size =10
    page_query_param="zzz"  #will change the name of page=2 now we have to write zzz=2
    page_size_query_param ="records" #using this attribute client can decide how many records show per page 
                                # example: ?page=1&records=6 now client will see only 6 records per page
    max_page_size=5 #nobody can see more than 5 records per page                            
    last_page_strings="end" #to go the last page we need to  write page=end but by default page=last works