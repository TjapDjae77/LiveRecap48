from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q  # Untuk pencarian
from .models import Member, Video, Transcription
from .serializers import MemberSerializer, VideoSerializer, TranscriptionSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

# Endpoint untuk autentikasi pengguna
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': 'success',
                    'message': 'Login berhasil',
                    'data': {
                        'username': user.username,
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    }
                })
            return Response({
                'status': 'error',
                'message': 'Username atau password salah',
                'data': None
            }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e),
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({
                'status': 'error',
                'message': 'Username already exists',
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({
            'status': 'success',
            'message': 'Registration successful',
            'data': {'username': user.username}
        }, status=status.HTTP_201_CREATED)

class LogoutAPIView(generics.GenericAPIView):
    def post(self, request):
        request.user.auth_token.delete()  # Hapus token saat logout
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)




# Endpoint untuk Member
class MemberAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response({
            'status': 'success',
            'message': 'Members retrieved successfully',
            'data': serializer.data
        })

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Member created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class MemberDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
            serializer = MemberSerializer(member)
            return Response({
                'status': 'success',
                'message': 'Member retrieved successfully',
                'data': serializer.data
            })
        except Member.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Member not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
            serializer = MemberSerializer(member, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Member updated successfully',
                    'data': serializer.data
                })
            return Response({
                'status': 'error',
                'message': 'Invalid data',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Member not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
            member.delete()
            return Response({
                'status': 'success',
                'message': 'Member deleted successfully',
                'data': None
            }, status=status.HTTP_204_NO_CONTENT)
        except Member.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Member not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

# Endpoint untuk Video
class VideoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response({
            'status': 'success',
            'message': 'Videos retrieved successfully',
            'data': serializer.data
        })

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Video created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class VideoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            serializer = VideoSerializer(video)
            return Response({
                'status': 'success',
                'message': 'Video retrieved successfully',
                'data': serializer.data
            })
        except Video.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Video not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            serializer = VideoSerializer(video, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Video updated successfully',
                    'data': serializer.data
                })
            return Response({
                'status': 'error',
                'message': 'Invalid data',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Video.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Video not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            video.delete()
            return Response({
                'status': 'success',
                'message': 'Video deleted successfully',
                'data': None
            }, status=status.HTTP_204_NO_CONTENT)
        except Video.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Video not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

# Endpoint untuk Transcription
class TranscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            transcriptions = Transcription.objects.filter(video=video)
            if not transcriptions.exists():
                return Response({
                    'status': 'error',
                    'message': 'Transcriptions not found',
                    'data': None
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = TranscriptionSerializer(transcriptions, many=True)
            return Response({
                'status': 'success',
                'message': 'Transcriptions retrieved successfully',
                'data': serializer.data
            })
        except Video.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Video not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

class TranscriptionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            transcription = Transcription.objects.get(pk=pk)
            serializer = TranscriptionSerializer(transcription)
            return Response({
                'status': 'success',
                'message': 'Transcription retrieved successfully',
                'data': serializer.data
            })
        except Transcription.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Transcription not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            transcription = Transcription.objects.get(pk=pk)
            serializer = TranscriptionSerializer(transcription, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Transcription updated successfully',
                    'data': serializer.data
                })
            return Response({
                'status': 'error',
                'message': 'Invalid data',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Transcription.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Transcription not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            transcription = Transcription.objects.get(pk=pk)
            transcription.delete()
            return Response({
                'status': 'success',
                'message': 'Transcription deleted successfully',
                'data': None
            }, status=status.HTTP_204_NO_CONTENT)
        except Transcription.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Transcription not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

class VideoSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)

            # Cek apakah video sudah memiliki ringkasan
            if video.summary:
                return Response({
                    'status': 'success',
                    'message': 'Summary retrieved successfully',
                    'data': {
                        'video_id': str(video.id),
                        'title': video.title,
                        'summary': video.summary
                    }
                })
            else:
                return Response({
                    'status': 'error',
                    'message': 'No summary found for this video',
                    'data': None
                }, status=status.HTTP_404_NOT_FOUND)

        except Video.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Video not found',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

class VideoSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('q', '')
        member_id = request.query_params.get('member_id')
        live_type = request.query_params.get('live_type')

        # Buat query dasar
        videos = Video.objects.all()

        # Terapkan filter pencarian
        if query:
            videos = videos.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

        # Filter berdasarkan member jika ada
        if member_id:
            videos = videos.filter(member_id=member_id)

        # Filter berdasarkan tipe live jika ada
        if live_type:
            videos = videos.filter(live_type=live_type)

        # Urutkan berdasarkan tanggal terbaru
        videos = videos.order_by('-created_at')

        serializer = VideoSerializer(videos, many=True)
        
        if not videos.exists():
            return Response({
                'status': 'success',
                'message': 'No videos found matching the criteria',
                'data': []
            })

        return Response({
            'status': 'success',
            'message': 'Videos retrieved successfully',
            'data': serializer.data
        })

class MemberSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('q', '')
        type_member = request.query_params.get('type')

        # Buat query dasar
        members = Member.objects.all()

        # Terapkan filter pencarian
        if query:
            members = members.filter(
                Q(name__icontains=query) |
                Q(nickname__icontains=query)
            )

        # Filter berdasarkan tipe member jika ada
        if type_member:
            members = members.filter(type_member=type_member)

        # Urutkan berdasarkan nama
        members = members.order_by('name')

        serializer = MemberSerializer(members, many=True)

        if not members.exists():
            return Response({
                'status': 'success',
                'message': 'No members found matching the criteria',
                'data': []
            })

        return Response({
            'status': 'success',
            'message': 'Members retrieved successfully',
            'data': serializer.data
        })
