from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Listing
from .serializers import ListingSerializer

class ManageListingView(APIView):
    #Getting listings
    def get(self, request):
        try:
            user = request.user
            if not user.is_realtor:
                return Response(
                    {'error':'User does not have the permissions to create a listing.'},
                    status= status.HTTP_403_FORBIDDEN,
                )
            slug = request.query_params.get('slug')
            if not slug:
                listing = Listing.objects.order_by('-date_created').filter(
                    realtor = user.email
                )
                listing = ListingSerializer(listing, many = True)

                return Response(
                    {'listings': listing.data},
                    status=status.HTTP_200_OK
                )
            if not Listing.objects.filter(
                realtor = user.email,
                slug = slug
            ).exists():
                return Response(
                    {'error':'Listing not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            listing = Listing.objects.get(realtor=user.email, slug = slug)
            listing = ListingSerializer(listing)
            return Response(
                    {'listings': listing.data},
                    status=status.HTTP_200_OK
                )
        
        except:
            return Response(
                {'error':'Something went wrong when retrieving data.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
#Posting listings
    def post(self, request):
        try:
            user = request.user
            if not user.is_realtor:
                return Response(
                    {'error':'User does not have the permissions to create a listing.'},
                    status= status.HTTP_403_FORBIDDEN,
                )
            data = request.data

            title = data['title']
            slug = data['slug']
            if Listing.objects.filter(slug=slug).exists:
                return Response(
                    {'error':'Listing with this slug already exist.'},
                    status = status.HTTP_400_BAD_REQUEST
                )
            address = data['address']
            city = data['city']
            region = data['region']
            campus = data['campus']
            description = data['description']

            payment_method = data['payment_method']
            if payment_method == 'MOBILE_MONEY':
                payment_method = 'Mobile money'
            elif payment_method == 'BANK':
                payment_method = 'Bank'
            elif payment_method == 'DEBIT_CARD':
                payment_method = 'Debit or credit card'
            else:
                payment_method = 'In person'

            distance = data['distance']
            if distance == 'FAR':
                distance = 'Hostel is far from campus'
            elif distance == 'CLOSE':
                distance = 'Hostel is close to campus'
            else:
                distance = 'Hostel is a normal distance away from campus'

            hometype= ['hometype']
            if hometype == 'HOMESTEL':
                hometype = 'Homestel'
            else:
                hometype = 'Hostel'

            price = data['price']
            try:
                price = int(price)

            except:
                return Response(
                    {'error':'Price must be an integer.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            rooms = data['rooms']
            try:
                rooms = int(rooms)

            except:
                return Response(
                    {'error':'Number of rooms must be an integer.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            room_capacity = data['room_capacity']
            try:
                room_capacity = int(room_capacity)
                if room_capacity == 1:
                    room_capacity = 'One in a room'
                else:
                    room_capacity = 'Two in a room'

            except:
                return Response(
                    {'error':'Room capacity must be an integer.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            bathroom = ['bathroom']
            if bathroom == 'True':
                bathroom = True
            else:
                bathroom = False

            kitchen = ['kitchen']
            if kitchen == 'True':
                kitchen = True
            else:
                kitchen = False

            is_published = ['is_published']
            if is_published == 'True':
                is_published = True
            else:
                is_published = False

            date_created = ['date_created']
            hostel_class = ['hostel_class']
            photo1 = data['photo1']
            photo2 = data['photo2']
            photo3 = data['photo3']



            if kitchen == True and bathroom == True:
                if distance == 'Close':
                    hostel_class = 'A'
                elif distance == 'Normal':
                    hostel_class = 'B'
                else:
                    hostel_class = 'C'
            Listing.objects.create(
                realtor = user.email,
                title = title,
                slug = slug,
                address = address,
                region = region,
                city = city,
                campus = campus,
                description = description,
                hometype = hometype,
                hostel_class = hostel_class,
                price = price,
                rooms = rooms,
                room_capacity = room_capacity,
                distance = distance,
                kitchen = kitchen,
                bathroom = bathroom,
                photo1 = photo1,
                photo2 = photo2,
                photo3 = photo3,
                is_published = is_published,
            )
            return Response(
                {'success':'Listing craeted successfully.'},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {'error':'Something went wrong.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
