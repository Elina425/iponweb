# class ItemCategoryView(View):
#
#     @staticmethod
#     def data_status(data):
#         return HttpResponse(
#             json.dumps({"data":data, "status":"ok"}),
#             status=200,
#             content_type="application/json",
#         )
#
#
#     def get(self, request):
#         items = ItemCategory.objects.all()
#         data=[]
#         for item in items:
#             data.append({"name":item.name, "price":item.price})
#         return self.data_status(data)
#
#     def post(self, request):