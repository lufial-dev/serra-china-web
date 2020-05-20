from django.contrib import admin
from dashboard import models
from django.contrib.auth.models import User


class ProdutoAdmin(admin.ModelAdmin):
    model = models.Produto
    list_display = ['nome', 'valor', 'status','id']


class IngredienteAdmin(admin.ModelAdmin):
    model = models.Ingrediente
    list_display = ['nome', 'status']


class ProdutoPedidoAdmin(admin.ModelAdmin):
    model = models.ProdutoPedido
    list_display = ['produto', 'quantidade', 'id']


class PedidoAdmin(admin.ModelAdmin):
    model = models.Pedido
    list_display = ['cliente', 'status', 'dataHoraPedido','id','cliente']

class UserAdmin(admin.ModelAdmin):
	model = models.Usuario
	list_display = ['nome','id']



admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Ingrediente, IngredienteAdmin)
admin.site.register(models.ProdutoPedido, ProdutoPedidoAdmin)
admin.site.register(models.Endereco)
admin.site.register(models.Usuario, UserAdmin)
admin.site.register(models.Pedido, PedidoAdmin)

