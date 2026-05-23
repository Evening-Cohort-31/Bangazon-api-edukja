from rest_framework import serializers
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from bangazonapi.models import Store, Customer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import HttpResponseServerError


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for stores"""

    class Meta:
        model = Store
        url = serializers.HyperlinkedIdentityField(view_name="store", lookup_field="id")
        fields = ("id", "url", "name", "description", "customer")


class Stores(ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """
        @api {POST} /stores POST new store
        @apiName CreateStore
        @apiGroup Store

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {String} name Short form name of the store
        @apiParam {String} description Long Form description of store
        @apiParamExample {json} Input
            {
                "name": "My Store",
                "description": "A place to buy things from me"
            }

        @apiSuccess (201) {Object} store Created store
        @apiSuccess (201) {id} store.id Store Id
        @apiSuccess (201) {String} store.name Name of the store
        @apiSuccess (201) {String} store.description The stores' description
        @apiSuccess (201) {String} product.customer Customer URI
        @apiSuccessExample {json} Success
            {
                "id": 50,
                "name": "My Store",
                "description": "A place to buy things from me",
                "customer": "https://localhost:8000/customers/5
            }
        """

        new_store = Store()
        new_store.name = request.data["name"]
        new_store.description = request.data["description"]

        customer = Customer.objects.get(user=request.auth.user)
        new_store.customer = customer

        new_store.save()

        serializer = StoreSerializer(new_store, context={"request": request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """
        @api {GET} /stores/:id GET Store
        @apiName GetStore
        @apiGroup Store

        @apiParam {id} id Store Id

        @apiSuccess (200) {Object} store Store object
        @apiSuccess (200) {id} store.id Store Id
        @apiSuccess (200) {String} store.url Store URI
        @apiSuccess (200) {String} store.name Short form store name
        @apiSuccess (200) {String} store.description Long form description of store
        @apiSuccess (200) {String} store.customer Customer URI
        @apiSuccessExample {json} Success
            {
            "id": 101,
            "name": "My Store",
            "description": "A place to buy stuff from me",
            "customer": "http://localhost:8000/customers/9"
            }
        """
        try:
            store = Store.objects.get(pk=pk)
            serializer = StoreSerializer(store, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)